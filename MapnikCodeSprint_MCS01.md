<!-- Name: MapnikCodeSprint/MCS01 -->
<!-- Version: 31 -->
<!-- Last-Modified: 2010/09/29 03:24:53 -->
<!-- Author: springmeyer -->
[[Image(MCS01-devseed.png)]]

*Committers and Cartographers* was the name and theme selected for the first Mapnik Code Sprint.  Grown from the seed of an idea at the OpenStreetMap State of the Map conference in Girona, Spain, July 2010.  It germinated on the Mapnik-Devel list to grow into an event on two continents.  

[[TOC]]

## Date
Friday, 24 September 2010 - Sunday, 26 September 2010

## [Location](/wiki:MapnikCodeSprint/MCS01/Location/)
MCS01 will be / was held in [London, England](/wiki:MapnikCodeSprint/MCS01/Location/).

## [Schedule](/wiki:MapnikCodeSprint/MCS01/Schedule/)
This will be a full weekend of Mapnik fun.  For details see the [schedule](/wiki:MapnikCodeSprint/MCS01/Schedule/).

## Code
Plan here for code to write and bugs to squish.  Please add your thoughts.  Discuss.  Plan.  

### Cartography Wish List
Cartography wish list.  

From Steve Chilton's SotM presentation:
 * respect the layer tag implicitly
 * names for lower roads should not appear where other roads pass over them
 * iterate alternative label placement
 * apply point within polygon labels
 * allow rotation for icons
 * accept SVG icons (Done? See [Changeset 1793](http://trac.mapnik.org/changeset/1793) )
 * apply variable widths to canals and rivers
 * apply vignettes inside polygons
 * produce spread text labels
 * different casing either side of roads (Done as patch for 0.7.1?  see offset lines #180 )
 * text labels either side of a line
 * more Natural Earth data at low-zooms (May apply more to OSM style than Mapnik-core)


 * add your advanced cartography requests

 * as it's already able to replace certain strings in the filename of a Symbolizer, other parameters should be changeable too. Say: I want to define a Template for a Symbolizer in the Stylesheet, but define its parameters (color, width, etc.) from database columns.
 
### Bug list
List of bugs for squishing or topics to discuss:
 * http://trac.mapnik.org/milestone/MCS1%20Tickets

### Cascadenik

Rob's going to be working on [Cascadenik](http://code.google.com/p/mapnik-utils/wiki/Cascadenik):
  - adding all the currently supported symbolizer attributes
  - supporting Mapnik2 alongside 0.x
  - supporting the new parameterized symbolizer attributes
  - merging the `-xmlbad` branch to trunk
  - cleaning, testing, and fixing bugs
  - fixing mapnik bugs uncovered by the above :)
    - one being #612 (dane will try to close during sprint)

### Profiling

Fred's interested in performance:
  - how long did it take to render this?
  - how much time was spent acquiring the data,
  - how much was spent processing each layer/style,
  - etc

## Results

[http://trac.mapnik.org/wiki/MapnikCodeSprint/MCS01/Results]

## Participants

London:
 * Artem Pavlenko - Mapnik Founder
 * Dane Springmeyer - Mapnik Project Release Manager
 * Steve Chilton - Chair, Society of Cartographers
 * Andy Allan - Founder OpenCycleMap
 * Iván Sánchez Ortega - OSM España (arriving Fri late evening)
 * AJ Ashton - Cartographer, Development Seed
 * Tom MacWright - GIS Developer, Development Seed
 * Tom Hughes - OSM SysAdmin and author of Mapnik Cairo backend
 * Andrii Mishkovskyi - GIS Developer, CloudMade
 * Frederik Ramm - geofabrik.de (from Fri noon)
 * and a cast of thousands (some shy folks not listed here)

San Francisco:
 * Michal Migurski - Walking-Papers Founder
 * Nino Walker
 * Katie Filbert (Friday ?)

Remote:
 * Rob Coup - Koordinates
 * Craig de Stigter - Koordinates

## Oh look, Development Seed made a logo for us!
How cool are they?  Pretty cool!

The logo is © 2010 Development Seed, [OpenStreetMap](http://www.openstreetmap.org/) and Contributors
and is licensed [CC-By-SA](http://creativecommons.org/licenses/by-sa/2.0/)