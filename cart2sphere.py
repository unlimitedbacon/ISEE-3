# Converts table of cartesian coordinates to celestial spherical coordinates
# Input format:
# DATE TIME X Y Z
# Output format:
# DATE TIME RIGHT_ASCENSION DECLINATION RADIUS

import argparse
import math

# Get options from command line
cli_parser = argparse.ArgumentParser()
cli_parser.add_argument( 'in_filename',
			help='TIPSOD Position file' )
options = cli_parser.parse_args()

in_file = open(options.in_filename)
for line in in_file:
	date,time,x,y,z,_ = line.split(None,5)
	# Convert strings to floats
	x = float(x)
	y = float(y)
	z = float(z)

	# Calculate radius, right ascension, and declination
	r = math.sqrt(x**2+y**2+z**2)
	ra = math.atan2(y,x)
	dec = math.asin(z/r)

	# Convert radians to degrees
	ra = math.degrees(ra)
	dec = math.degrees(dec)
	print(date,time,ra,dec,r)
