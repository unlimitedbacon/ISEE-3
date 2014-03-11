ISEE-3 / ICE
============

A long-lost, pioneering spaceship—still functional thanks only to chance and human error—is coming home for the first time in three decades. It wants to explore new worlds. But we've forgotten how to talk to it. [The obligatory XKCD.](https://xkcd.com/1337/)

* NSSDC/COSPAR ID:	1978-079A
* Sattelite Index #:	S011004

[![ISEE-3 Returns](http://img.youtube.com/vi/t2YRxdpjce0/0.jpg)](http://www.youtube.com/watch?v=t2YRxdpjce0)

![Trajectory Animation](https://raw.github.com/unlimitedbacon/ISEE-3/master/trajectory.gif)
Trajectory animation from 2008-09-18 to 2014-08-11. Earth is at the origin and the sun is in the +X direction.

Where do I point my satellite dish?
-----------------------------------
Ephemeris is now available from [JPL HORIZONS](http://ssd.jpl.nasa.gov/horizons.cgi), target -111.

[Orbiter](http://orbit.medphys.ucl.ac.uk/) Scenarios
----------------------------------------------------
These are based on the JPL HORIZONS trajectory data and also accurately represent the rate of spin and remaining fuel. Take a shot at parking it at L1 or L2! There are scenarios for...
* Last known position from DSN observations in 2008
* Current position as of March 2014
* Just before descending node on June 21, 2014. A plane change maneuver will be required at this point.
* Earth encounter

Scripts
-------
Use `geo2local.py` to convert the table of geographic coordinates from the [Satellite Situation Center](http://sscweb.gsfc.nasa.gov/tipsod/) to your local azimuth and elevation for pointing a telescope. The tool also gives range rate for calculating doppler shift. You will need to feed it your lattitude, longitude, and altitude. For example...
```
$ ./geo2local.py --lat 33.47 --lon -81.975 --alt 0.04145 GEO.20140219-20140811.txt > Local.Augusta.20140219-20140811.txt
```
try `geo2local.py -h` for more options.

News
----
* 2014.03.09: [AMSAT-DL and Bochum Observatory receive signal from retired NASA spacecraft](http://www.amsat-dl.org/index.php/news-mainmenu-97/199-ice-satellite-received-in-bochum)
* 2014.02.14: [Call for Hams and Hackers: Welcome ICE/ISEE-3 Home (Hack A Day)](http://hackaday.com/2014/02/14/call-for-hams-and-hackers-welcome-iceisee-3-home/)
* 2014.02.12: [America Forgot How to Talk to Its Zombie Spaceship (NationalJournal)](http://www.nationaljournal.com/tech/america-forgot-how-to-talk-to-its-zombie-spaceship-20140212)
* 2014.02.07: [ICE/ISEE-3 to return to an Earth no longer capable of speaking to it (Planetary Society)](http://www.planetary.org/blogs/emily-lakdawalla/2014/02070836-isee-3.html)

Discussions
-----------
* Facebook Page: https://www.facebook.com/ISEE3returns
* Reddit Discussions:
	+ http://www.reddit.com/r/space/comments/1xpfug/america_forgot_how_to_talk_to_its_zombie/
	+ http://www.reddit.com/r/amateurradio/comments/1yb8dt/amateur_radio_exploratory_committee_to_research/
	+ http://www.reddit.com/r/amateurradio/comments/1xbioo/iceisee3_to_return_to_an_earth_no_longer_capable/
	+ http://www.reddit.com/r/amateurradio/comments/1xx3tm/call_for_hams_and_hackers_welcome_iceisee3_home/
	+ http://www.reddit.com/r/RTLSDR/comments/1xq3tj/america_forgot_how_to_talk_to_its_zombie/
	+ http://www.reddit.com/r/RTLSDR/comments/1xtfed/some_more_telemetry_resources_for_people/
* Unmanned Spaceflight Forums: http://www.unmannedspaceflight.com/index.php?showtopic=3800&start=0&p=207327&#entry207327
* AMSAT Mailing List: http://ww2.amsat.org/amsat/archive/amsat-bb/48hour/msg100674.html

Technical Information
---------------------
* NASA General Information: http://nssdc.gsfc.nasa.gov/nmc/spacecraftDisplay.do?id=1978-079A
* ISSE-3/ICE Telecommunications Summary: http://mdkenny.customer.netspace.net.au/ISEE-3.pdf
* Space Weather Journal Article: http://nssdcftp.gsfc.nasa.gov/spacecraft_data/isee/isee3/
* Historical Orbital Elements Database: http://www.planet4589.org/space/elements/
	+ Index: http://www.planet4589.org/space/logs/satcat.txt
	+ ISEE-3/ICE TLE: http://www.planet4589.org/space/elements/11000/S11004
* Wikipedia: http://en.wikipedia.org/wiki/International_Cometary_Explorer
* Raw Tracking and Scientific Data
	+ ftp://spdf.gsfc.nasa.gov/pub/data/isee/isee3/
	+ http://mdkenny.customer.netspace.net.au/2012-ISEE-3-SWE-543.pdf
* Microwave Filter Requirements: http://ipnpr.jpl.nasa.gov/progress_report/42-76/76K.PDF
* DSN 70 m Subnet Telecommunications Interfaces: http://deepspace.jpl.nasa.gov/dsndocs/810-005/101/101E.pdf
* Satellite Situation Center 4D Orbit Viewer: http://sscweb.gsfc.nasa.gov/tipsod/
	+ RE = Earth Radius
* Heliocentric Trajectory Data: http://omniweb.sci.gsfc.nasa.gov/coho/helios/heli.html
* Libration Point Missions: http://www.ieec.fcr.es/libpoint/papers/dunham.pdf
* The Telecommunications and Data Acquisition Progress Report 42-84: http://ipnpr.jpl.nasa.gov/progress_report/42-84/84title.htm
* ICE Navigation Support: http://ipnpr.jpl.nasa.gov/progress_report/42-86/86CC.PDF
* Low Energy Particle Telescope System: http://www.sp.ph.ic.ac.uk/~balogh/isee3.htm


