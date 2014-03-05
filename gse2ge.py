# THIS PROGRAM IS BROKEN
# DON'T USE IT
# 
# Converts table of Geocentric Solar Ecliptic coordinates
# to Geocentric Equatorial coordinates (J2000)
# 
# Input format:
# DD/MM/YY HH:MM RIGHT_ASCENSION DECLINATION RADIUS
# Solar Ephemeris format:
# YYYY-Mon-DD HH:MM	RIGHT_ASCENSION DECLINATION

import argparse
import math

solar_filename = "SolEphemeris.txt"
months = { "Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12 }

# Get options from command line
cli_parser = argparse.ArgumentParser()
cli_parser.add_argument( 'in_filename',
			help='TIPSOD Position file' )
format_group = cli_parser.add_mutually_exclusive_group()
format_group.add_argument( '-c',
                        dest='csv', action='store_true', default=False,
                        help='Export CSV file' )
format_group.add_argument( '-m',
                        dest='markdown', action='store_true', default=False,
                        help='Export Markdown file' )


options = cli_parser.parse_args()

sun = {}
solar_file = open(solar_filename)
data_section = False
for line in solar_file:
	if "$$EOE" in line:
		data_section = False
	if data_section:
		date,time,ra,dec = line.split(None,3)
		dec = dec.replace("\n","") # Remove EOL
		# Interpret date
		year,month,day = date.split("-")
		year = int(year)
		month = months[month]
		day = int(day)
		# Interpret time
		hour,minute = time.split(":")
		hour = int(hour)
		minute = int(minute)
		# Combine date and time for database index
		datetime = year*100000000 + month*1000000 + day*10000 + hour*100 + minute
		# Convert strings to float
		ra = float(ra)
		dec = float(dec)
		sun[datetime] = (ra,dec)
	if "$$SOE" in line:
		data_section = True

# Print header
if options.csv:
	print("Date, Time (UTC), Right Ascension (Hours), Right Ascension (°), Declination (°), Distance (km)")
else:
	print("ISEE-3 / ICE Ephemeris")
	print("======================\n")
	print("For local azimuth and altitude, use Wolfram Alpha.")
	print("Example: http://www.wolframalpha.com/input/?i=3.2016887536118475+right+ascension+-12.4972872261582+declination")
	print("Be sure to use hours for Right Ascension and degrees for Declination.\n")
	print("Geocentric Equatorial Coordinate System with respect to J2000 equinox.\n")
	print("Starting Date:	February 19, 2014	00:00")
	print("Ending Date:	August 11, 2014		00:00")
	print("12 minute increments")
	print("All times are UTC\n")
	if options.markdown:
		print("Date		| Time	| Right Ascension (Hrs)	| Right Ascension (°)	| Declination (°)	| Distance (km)")
		print("----------------|-------|-----------------------|-----------------------|-----------------------|-------------------")
	else:
		print("Date	Time (UTC)	Right Ascension (Hours)	Right Ascension (°)	Declination (°)		Distance (km)")
		print("--------------------------------------------------------------------------------------------------------------")

in_file = open(options.in_filename)
for line in in_file:
	date,time,gse_ra,gse_dec,r = line.split(None,4)
	r = r.replace("\n","") # Remove EOL
	# Convert strings to floats
	gse_ra = float(gse_ra)
	gse_dec = float(gse_dec)
	r = float(r)
	# Interpret date
	year,month,day = date.split("/")
	year = 2000+int(year)
	month = int(month)
	day = int(day)
	# Interpret time
	hour,minute = time.split(":")
	hour = int(hour)
	minute = int(minute)
	# Combine date and time for database index
	datetime = year*100000000 + month*1000000 + day*10000 + hour*100 + minute

	# Get solar location
	sun_ra,sun_dec = sun[datetime]
	# Find angle between equatorial and ecliptic planes
	theta = math.atan2(sun_dec,sun_ra)
	# Rotate GSE coordinates by angle
	ge_ra = gse_ra*math.cos(theta) - gse_dec*math.sin(theta)
	ge_dec = gse_ra*math.sin(theta) + gse_dec*math.cos(theta)
	# Offset GSE coordinates by solar position
	ge_ra = ge_ra + sun_ra
	ge_dec = ge_dec + sun_dec
	# Wrap around
	if ge_ra >= 360:
		ge_ra = ge_ra-360
	# Convert RA to hours
	ge_ra_hrs = ge_ra/360 * 24

	if options.markdown:
		print(date+"\t| "+time+"\t| "+str(ge_ra_hrs)+"\t| "+str(ge_ra)+"\t| "+str(ge_dec)+"\t| "+str(r))
	elif options.csv:
		print(date+","+time+","+str(ge_ra_hrs)+","+str(ge_ra)+","+str(ge_dec)+","+str(r))
	else:
		print(date+"\t"+time+"\t"+str(ge_ra_hrs)+"\t"+str(ge_ra)+"\t"+str(ge_dec)+"\t"+str(r))
