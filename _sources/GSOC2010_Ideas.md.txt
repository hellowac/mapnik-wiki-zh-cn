# Google Summer of Code Ideas - 2010

Mapnik will participate in Google Summer of Code 2010.

Both potential students and mentors can start adding their ideas for potential projects here.

See the main page for more details: [GSOC2010](GSOC2010)

See also steve8's ideas page: [Ideas](Ideas)

## Project Ideas

----

## Results

* *Mapnik Python3k Support*: Done: see [Python3k](Python3k)

* *Layer Composites*: Too hard for a GSOC student, but hopefully will be tackled by core devs soon

* *Better Print Support*: GSOC Student Carlos finished adding scale_factor to agg_renderer and wrote a custom svg_renderer (also see: <https://github.com/thjc/mapnik-svg>)

* *Support for outputting hit-areas*:  GSOC Student Herm created [MetaWriter](MetaWriter)

* *Processnik*: DevSeed wrote something like this, see <http://tilemill.com>

----

## Mapnik Python3k Support

### Description

Mapnik uses Boost.Python for its python bindings. Boost.Python is written in C++ and recently added support for Python 3.x based on the excellent [2009 Google Summer of Code project by Haoyu Bai](http://socghop.appspot.com/gsoc/student_project/show/google/gsoc2009/boost/t124021999037) (mentored by Stefan Seefeld). An amazing addition to the Mapnik library would be following up on this work and applying it to Mapnik for full python 3.x support.

In addition, if interest and time this project could look at exposing more pythonic access to Mapnik C++ objects, perhaps using a more declarative style ([#459](https://github.com/mapnik/mapnik/issues/459)) and extending wrapping of key object like r1740.

### How it would benefit Mapnik Project

Mapnik would be compatible with both Python 2.x and Python 3.x, paving the way for better integration with other leading python applications. Better python style would encourage faster and funner development.

### What student would learn

The student would learn about the latest advances in Boost Python, the intricacies of Mapnik's Python bindings, and overall very valuable skills that could be applied to a range of other projects that have yet to upgrade to Python 3.x.

### Submitter

[Dane Springmeyer](http://dbsgeo.com)

### Possible Mentors

[Dane Springmeyer](http://dbsgeo.com)

### Technical Issues

* See [ticket #334](https://github.com/mapnik/mapnik/issues/334) for more details
* -- springmeyer - March 12th,2010

----
----

## Layer Composites

### Description

Mapnik layers should be able to interact with one another just like layers in Photoshop. They could have transfer modes (e.g. screen, hard light, darken), masks, and groups. The XML description for this would be backward-compatible with the current Mapnik stylesheet language, but when new markup is added, such as a *mode* or *opacity* attribute on a layer, a *Group* element around a group of layers, or a *Mask* layer inside another layer, new behaviors could be seen.

### How it would benefit Mapnik Project

Mapnik would natively create complex, layered maps like the amazing [TopOSM](http://wiki.openstreetmap.org/wiki/TopOSM).

### What student would learn

The student would learn the internals of Mapnik and the math and complexity behind Photoshop-style image compositing.

### Submitter

[Mike Migurski](http://mike.teczno.com) (<mike@stamen.com>)

### Possible Mentors

Unsure who would be a willing mentor - [I](http://mike.teczno.com) know what would be a great-looking end result and could help with the math and cartography and XML format bits, but I can't offer C++ help of any kind. Maybe this is a bidirectional mentorship? =)

### Technical Issues

* Maybe is possible to use other free software (like imagemagick) instead Photoshop to study layer composing, i'm interesting to develop this idea, i have a little knowledge of C++ but i can study it in these months before GSOC will start
* -- luca delucchi - March 11, 2009

* GRASS GIS made something similar with [r.his](http://grass.osgeo.org/grass64/manuals/html64_user/r.his.html)
* -- luca delucchi - March 12, 2009

* Seems perhaps related to [#314](https://github.com/mapnik/mapnik/issues/314)
* -- springmeyer - March 12, 2009

* TopOSM does indeed use ImageMagick for compositing, so that may be a good thing to look at. See <http://wiki.openstreetmap.org/wiki/TopOSM/Details> for more info about how it is done.
    * -- Lars Ahlzen - March 13, 2010

* See also: <http://wiki.openstreetmap.org/wiki/User:Kobezda/GSoC>
    * -- Dane Springmeyer - April 6, 2010

* Potential spec could look like: [Ideas/Compositing](Ideas_Compositing)
    * -- Dane Springmeyer - April 6, 2010

* Good brainstorming thread on issues around compositing on #mapnik April 7th: <http://mapnik.dbsgeo.com/mapnik_logs/2010/04/07/>
* -- Dane Springmeyer - April 7, 2010

* Ideas/Compositing - shawnbot's idea around a potential syntax

----
----

## Better Print Support

### Description

Through the growth of projects using Mapnik rendering, like <http://OpenStreetMap.org>, <http://Walking-Papers.org>, and <http://MapOSMatic.org>, more and more users are looking to print out Mapnik cartography. Target formats are large paper plots or other variable-resolution digital formats (vectors like PDF/SVG). It is an exciting and powerful thing to be able to use the same renderer for web cartography as multi-resolution cartography, and due to Mapnik's solid Cairo Rendering backend the foundation is in place for multi-resolution output. But currently Mapnik has a few limits which hold back optimal print and vector output.

Potential subtopics include:

* Mapnik's understanding of units could be expanded beyond just pixels ([#389](https://github.com/mapnik/mapnik/issues/389))
* Users could gain hooks into the Mapnik rendering process to control scaling directives ([#343](https://github.com/mapnik/mapnik/issues/343)), and tune currently hardcoded map scale assumptions ([#196](https://github.com/mapnik/mapnik/issues/196))
* More internal objects could be logically scalable
* e.g. we need to be able to scale raster graphics which should be feasible (not going to look very good, but still needed: see [#155](https://github.com/mapnik/mapnik/issues/155))
* and ideally need scalable vector symbols as per [#320](https://github.com/mapnik/mapnik/issues/320) (this is likely out of the scope of a GSOC project but should be considered).
* Other cool stuff can (and should for proper paper output) be drawn on the map: [#358](https://github.com/mapnik/mapnik/issues/358) (see also [Legending](Legending))
* Lastly, certain limitations exist in the Cairo API Mapnik uses that might be able to be addressed by student research/coding:
* notably Cairo does not currently embedded fonts in SVG output but rather falls back to vectors to represent fonts.([#535](https://github.com/mapnik/mapnik/issues/535))

So, to recap Mapnik output could be easily adjustable to various scales and point sizes, use vector or multi-scale symbolizers (shields, points, texture fills, etc), svg icons, etc. SVG supports text on a path, perhaps this could be used in the output. Something like scale-9 might be useful for highway shields: <http://www.sephiroth.it/tutorials/flashPHP/scale9/> ... all this should be documented, too! In combination with cascadenik, maybe this uses the CSS media attributes, and could be extended to other changes in resolution like mobile cartography too.

### How it would benefit Mapnik Project

Mapnik would continue to be an attractive way to structure and process cartographic information and a single stylesheet could be generalized and applicable in multiple contexts.

### What student would learn

The student would learn the internals of Mapnik (AGG, Boost etc) and the subtleties of multi-scale and multi-resolution rendering. There's a tension between the accuracy of pixels and the reusable nature of measurements specified in points, inches, millimeters etc. that will be very familiar to users and authors of graphical software. The student would learn all that.

### Submitter

[Tom Carden](http://www.tom-carden.co.uk) (<tom@tom-carden.co.uk>)

### Possible Mentors

As above, [I](http://www.tom-carden.co.uk) would be willing to mentor this from a sanity, usefulness and syntax point of view but not really from a C++ internals point of view.

I would be interested in co-mentoring this project from an Mapnik/C++ internals point of view

* -- dane springmeyer - March 21, 2010

### Technical Issues

* This could be done in tandem with two students/mentors with OpenStreetMap
* **Important**: see discussion also at: <http://wiki.openstreetmap.org/wiki/GSoC_Project_Ideas_2010#Paper_Output_Projects>
* -- dane springmeyer - March 21, 2010

* Existing tickets that could be advanced/started as part of this project include: [#343](https://github.com/mapnik/mapnik/issues/343) and [#389](https://github.com/mapnik/mapnik/issues/389)
* --dane springmeyer - March 21, 2010

* This has many linkages with the idea of [OSGEO Cartographic Library](http://wiki.osgeo.org/wiki/OSGeo_Cartographic_Engine#Ideas_for_Summer_of_Code_2010_Project)
* --dane springmeyer - March 9, 2010

* One student application on this topic is being prepared at: <http://betterprintsupport.blogspot.com/>

* Two more examples of people using Mapnik for printed output:
    * <http://oliverobrien.co.uk/2010/03/map-adornments-with-cairo/>
    * <http://razor.occams.info/blog/2010/02/26/printable-congressional-district-maps-behind-the-scenes/>

----
----

## Support for outputting hit-areas

### Description

It should be possible to specify a layer as "clickable" and as well as outputting an image output a corresponding data file (e.g. JSON or HTML map/area tags or raw geometry) that could be used to perform hit tests. This could be used to make clickable points, lines or polygons. Demo implementation could be done using OpenLayers, perhaps. This idea could be extended to embedding metadata directly in image files, for example all visible street names could be added as EXIF data so that a map image (might) appear in an image search for a street.

### How it would benefit Mapnik Project

Mapnik would continue to be the first open-source choice for rendering web-based maps. Mapnik's geometry internals would be robustly exposed to outputting (projected, image-space) geometry with arbitrary selections of metadata.

### What student would learn

The student would learn the internals of mapnik and the very edges of the trade-offs between raster and vector imagery for interactivity on the web.

### Submitter

[Tom Carden](http://www.tom-carden.co.uk)

### Possible Mentors

As above, [I](http://www.tom-carden.co.uk) would be willing to mentor this from a sanity, usefulness and syntax point of view but not really from a C++ internals point of view.

### Technical Issues

----
----

## Processnik

### Description

Processing <http://processing.org> for Mapnik/Cascadenik. Or Nodebox, for Python folks. Basically a tabbed text editor with a play button that would preview a map. But clearly Mapnik requires a few more features than that: it would be lovely to be able to interrogate/browse data sets and find out which attributes should be used. It would be ideal, Firebug style, to click on a street and find out which styles were applied to it. It would be great to have a slippy map as a preview. Perhaps this is an extension of Quantumnik. Perhaps it's a Firefox extension that uses Mapnik's SVG output and then piggybacks onto Firebug. Who knows?

### How it would benefit Mapnik Project

GUI tools bring users, users bring fame and glory.

### What student would learn

GUI development, Mapnik internals, Cascadenik, Python, etc. Plus a healthy dose of reaching out to cartographers who don't want to edit code. Setting up layers with database queries in this environment would be tricky, but simple shapefile rendering should be totally doable.

### Submitter

[Tom Carden](http://www.tom-carden.co.uk)

### Possible Mentors

As above, [I](http://www.tom-carden.co.uk) would be willing to mentor this from a sanity, usefulness and syntax point of view but not really from a C++ internals point of view.

### Technical Issues

----
----

Format should be:

## NAME HERE

### Description

### How it would benefit Mapnik Project

### What student would learn

### Submitter

### Possible Mentors

### Technical Issues

* Comment/Idea
* -- name of person commenting - date

----
