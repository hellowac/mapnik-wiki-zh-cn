<!-- Name: MapnikCodeSprint/MCS01/Results -->
<!-- Version: 4 -->
<!-- Last-Modified: 2010/09/30 12:04:24 -->
<!-- Author: springmeyer -->
## Blogs

Bonnie Bogle
[http://developmentseed.org/blog/2010/sep/24/mapnik-code-sprint-london-weekend]

Tom MacWright
[http://developmentseed.org/blog/2010/sep/27/report-mapnik-code-sprint]

OpenGeoData
[http://opengeodata.org/mapnik-code-sprint-committers-and-cartographe]

Mike Migurski
[http://mike.teczno.com/notes/map-sprint.html]

Dane Springmeyer
 * Kickoff - [http://mapnik.org/news/2010/sep/24/mcs01_day1/]
 * Faster Mapnik - [http://mapnik.org/news/2010/sep/29/mcs01_roundup1/]
 * Community - [http://mapnik.org/news/2010/sep/29/mcs01_roundup2/]


## Photos

Hard at work on Mapnik
[http://www.flickr.com/photos/developmentseed/5029925686/in/photostream/]

Dane and Artem meet in person
[http://yfrog.com/50o6xj]

Intensely following TileMill demonstration
[http://yfrog.com/n4go6sj]

Toasting a successful sprint
[http://yfrog.com/jvegpqj]


## Fixes and Improvements

This is a quick list of things we started work on or achieved during the sprint:

(please add anything I missed - dane)

 * Discussed next stable release (.7x series and Mapnik2 work, what to backport)
  * Forward compatibility of .7.x series a priority  (springmeyer)
 * Lots of work on new prototype for documentation (dodobas) #288
 * Moved Cascadenik to github and refactored lots of code, merging in XML-bad branch (migurski, rcoup, ninow) (http://github.com/mapnik/Cascadenik)
 * Came up with lots of new ideas and pushed they into tickets against [Sprint Milestone](http://trac.mapnik.org/milestone/MCS1%20Tickets) 
 * Many sprinters installed Mapnik2 - we updated docs with lessons learned (springmeyer)
 * Extensive review and prioritization of tickets relating to cartographic features (ldp)
 * Work towards native boost::spirit WKT parser (artem)
 * Number of improvements to python api documentation (tmcw)
 * Add functions to set the alpha of overall rendering map image (springmeyer)
 * Started work on better warning output during XML parsing for misspelled property names (springmeyer) #110
 * Added function to convert grayscale channel to alpha channel for "World Glass" effect (springmeyer)
 * Added support for faster multi-threaded reprojection through use of proj ctx (#605) (tomhughes)
 * Addition of RTL test XML (r2244, ajashton)
 * Worked on scoping Cairo context.scale() bugs - no solution quite yet (mishok13)
 * Added support for "late-binding" of datasources for better control over object creation from calling apps like Cascadenik (#622) (rcoup)
 * Various Improvements to shield and text positioning (artem)
 * Improvements to SVG parsing and rendering (artem)
 * Fixed feature caching when using multiple styles for faster rendering (woodpeck) (#624)
 * Brainstormed and scoped on wiki ideas around [Compositing](/wiki:Ideas/Compositing/) and [Legends](/wiki:Legending/) (gravitystorm, ivansanchez)
 * Added Python3 support (haoyu,springmeyer) [wiki:Python3k]
 * Wrote a render_debug() function to output statistics on rendering times (woodpeck)
 * Added the ability to control the timeout of expensive PostGIS queries (jburgess) #632
 * Started writing Spreadnik v2 in python (ivansanchez)
 * Doubled speed of the [Paleoserver](http://trac.mapnik.org/wiki/Paleoserver) for returning transparent tiles (springmeyer)
 * Fixed bugs in nik2img around double-opening of images on linux and recursively registering fonts (springmeyer)

## Trac timeline

[http://trac.mapnik.org/timeline?from=09%2F29%2F10&daysback=10&ticket=on&ticket_details=on&changeset=on&update=Update]

## Tickets
[http://trac.mapnik.org/milestone/MCS1%20Tickets]