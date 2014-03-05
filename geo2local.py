#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Converts table of geographic cartesian coordinates to local azimuth/elevation

# Default behavior: print values based on current date/time and exit
# Optional: specify date/time or export entire table to file
# Graph with gnuplot
# Specify frequency for doppler shift

# GEO: Geographic coordinates
# Z axis passes through Earth's poles
# X axis goes through the Prime Meridian


from math import *
import argparse
import datetime

# Constants
earth_rad = 6371.0	# Radius of Earth in km

def geo2local( ground_lat, ground_lon, ground_alt, sat_x, sat_y, sat_z ):
	# Convert degrees to radians
	ground_lat = radians(ground_lat)
	ground_lon = radians(ground_lon)
	# Find radial distance of ground station from center of Earth
	ground_r = earth_rad + ground_alt

	# Rotate satellite coordinate by -ground station longitute about Z axis
	x = sat_x*cos(-ground_lon) - sat_y*sin(-ground_lon)
	y = sat_x*sin(-ground_lon) + sat_y*cos(-ground_lon)
	sat_x = x
	sat_y = y

	# Rotate satellite coordinates by -ground station lattitude about Y axis
	x = sat_x*cos(-ground_lat) - sat_z*sin(-ground_lat)
	z = sat_x*sin(-ground_lat) + sat_z*cos(-ground_lat)
	sat_x = x
	sat_z = z

	# Shift satellite down by ground station radius
	sat_x = sat_x - ground_r

	# Calculate Range
	sat_r = sqrt( sat_x**2 + sat_y**2 + sat_z**2 )

	# Swap Axes
	# X becomes Z
	# Z becomes Y
	# Z is now perpendicular with Earth's surface
	# Y is North
	x = sat_x
	y = sat_y
	z = sat_z
	sat_z = x
	sat_y = z
	sat_x = y

	# Convert to spherical coordinates
	# Azimuth is angle from Y axis
	azimuth = atan2( sat_x, sat_y )
	elevation = asin( sat_z / sat_r )

	# Convert radians to degrees
	azimuth = degrees(azimuth)
	if azimuth < 0:
		azimuth = 360 + azimuth
	elevation = degrees(elevation)

	return azimuth, elevation, sat_r

# Get options from command line
cli_parser = argparse.ArgumentParser()
cli_parser.add_argument( 'in_filename',
			 metavar='FILE',
			 help='Satellite Situation Center file with GEOgraphic cartesian coordinates' )
output_group = cli_parser.add_mutually_exclusive_group()
output_group.add_argument( '-c',
			dest='csv', action='store_true', default=False,
			help='Export CSV file' )
output_group.add_argument( '-m',
			dest='markdown', action='store_true', default=False,
			help='Export Markdown file' )
output_group.add_argument( '-t',
			dest='txt', action='store_true', default=False,
			help='Export text file' )
cli_parser.add_argument( '--lat',
			 metavar='LATTITUDE',
			 type=float, required=True,
			 help='Degrees of north lattitude in decimal form for the ground station.' )
cli_parser.add_argument( '--lon',
			 metavar='LONGITUDE',
			 type=float, required=True,
			 help='Degrees of east longitude in decimal form for the ground station.' )
cli_parser.add_argument( '--alt',
			 metavar='ALTITUDE',
			 type=float, required=True,
			 help='Altitude of ground station above sea level in kilometers.' )
options = cli_parser.parse_args()

# Setup
now = datetime.datetime.utcnow()
in_file = open(options.in_filename)
last_distance = 0

# Print header
if options.csv:
        print("Date, Time (UTC), Azimuth (°), Elevation (°), Distance (km), Range Rate (km/s)")
else:
        print("ISEE-3 / ICE Ephemeris")
        print("======================\n")
	print("Local Azimuth and Elevation for...")
	print("Lat: "+str(options.lat)+"°")
	print("Lon: "+str(options.lon)+"°")
	print("Alt: "+str(options.alt)+"km\n")
        print("Starting Date:   February 19, 2014       00:00")
        print("Ending Date:     August 11, 2014         00:00")
        print("12 minute increments")
        print("All times are UTC\n")
	print("Range rate is average for the past 12 minutes\n")
        if options.markdown:
                print("Date            | Time  | Azimuth (°)   | Elevation (°)         | Distance (km) | Range Rate (km/s)")
                print("----------------|-------|---------------|-----------------------|---------------|------------------")
        else:
                print("Date     Time (UTC)     Azimuth (°)     Elevation (°)   Distance (km)   Range Rate (km/s)")
                print("-----------------------------------------------------------------------------------------")

# Main Loop
for line in in_file:
	date,time,sat_x,sat_y,sat_z,_ = line.split(None,5)	# Read first 5 columns
	# Convert strings to floats
	sat_x = float(sat_x)
	sat_y = float(sat_y)
	sat_z = float(sat_z)
	# Interpret date
	year,month,day = date.split("/")
	year = 2000+int(year)
	month = int(month)
	day = int(day)
	# Convert coordinates
	azimuth,elevation,distance = geo2local( options.lat, options.lon, options.alt, sat_x, sat_y, sat_z )
	# Calculate range rate for last 12 minuts
	# Would be better to take previous and next interval
	# and take average
	if last_distance == 0:	# Handle first line
		last_distance = distance
	rate = (distance-last_distance) / 720	# Fixed for 12 minute intervals
	last_distance = distance
	# Print results
	if options.markdown:
		print(date+"\t| "+time+"\t| "+str(azimuth)+"\t| "+str(elevation)+"  \t| "+str(distance)+"\t| "+str(rate))
        elif options.csv:
                print(date+","+time+","+str(azimuth)+","+str(elevation)+","+str(distance)+","+str(rate))
        else:
                print(date+"\t"+time+"\t"+str(azimuth)+"\t"+str(elevation)+"\t"+str(distance)+"\t"+str(rate))

