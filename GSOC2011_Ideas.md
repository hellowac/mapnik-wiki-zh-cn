<!-- Name: GSOC2011/Ideas -->
<!-- Version: 8 -->
<!-- Last-Modified: 2011/04/29 18:02:00 -->
<!-- Author: springmeyer -->


# Google Summer of Code Ideas

Mapnik was accepted to participate in Google Summer of Code 2011.

Three students were accepted this year: http://mapnik.org/news/2011/apr/25/three_students_mapnik_gsoc_2011/

See the main page for more details: [[GSOC2011]]

See also steve8's ideas page: [[Ideas]]


# Project Ideas

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

# Mapnik PHP extension
# Description
The Mapnik library can be used from its native language C++ or from Python by using the Python Mapnik bindings. I propose a GSoC project to fully develop PHP bindings for Mapnik. The large user base of PHP developers means that PHP bindings will make Mapnik available to a whole new audience. I’ve done initial work already on these bindings, and a proof of concept is available. The GSoC project would make it possible to mature this proof of concept to a complete PHP wrapper around Mapnik 0.7 and 2.0. It would also make the extension easily accessible to other developers with build systems for Linux and Windows and have QA with unit tests and automated testing against various versions of PHP. Ideally it should also be able to read XML-based stylesheets and render maps based on them.
# How it would benefit Mapnik Project
The Mapnik project would benefit from having PHP bindings by being opened up to a lot more potential users. There are many PHP developers writing software for the web. Having PHP as a fully supported language to use Mapnik from, next to C++ and Python, will allow many people to add mapping functionality to their web projects while staying within the same technology stack.
# What student would learn
PHP/Zend internals and build system; Mapnik internals; unit testing best practices.
# Submitter
Roel Vanhout
# Possible Mentors
???
# Technical Issues
Technical issues include finding reusable C++ patterns to comfortably work with the Zend extension API, finding ways to optimize the performance hit that comes with scriptings languages and can be substantial for operations that are performed many times and finding a balance in the API design between the idiomatich PHP way and staying close to Mapnik C++.

----
# Cartographic elements
# Description
Mapnik is mostly focused on rendering maps for the Web, in the form of tiles – map cutouts that are combined to look like one big map. Cartography is more than that, though. For non-interactive maps, traditional cartographic elements like map headers, legends, a north arrow etc. need to be added. I propose an extension to the Mapnik library that allows users to specify these elements and in this way render complete production-quality maps, without having to use other software.
The project would start with an inventarisation of required mapping elements in the form of a literature study on cartographic design. After a set of map elements to be implemented is selected, the API needs to be designed that fits with the rest of the Mapnik API. Finally this API needs to be implemented, and tests written to check its correct functioning.
# How it would benefit Mapnik Project
The described functionality will broaden the applicability of Mapnik as a multi-purpose map rendering library. It will allow making complete, cartographically correct maps from within the comfort of a text editor. These added visual features will allow Mapnik to be a general-purpose map renderer, and not just a Web tile generator.
# What student would learn
Fundamentals of (computer-based) cartographic design; Mapnik internals.
# Submitter
Roel Vanhout
# Possible Mentors
???
# Technical Issues
The issues with this project are in finding generic ways to specify map elements, in ways that provide a natural fit with the data and provide as much flexibility to the cartographer as possible for maximum expressiveness. As much of the rendering code in the rest of Mapnik should be re-used, e.g. SVG code for rendering SVG north arrows.

  * See also [[Legending]] and https://github.com/mapnik/mapnik/issues/536 .

  * Scale bars, legends, and grid lines are implemented in this evolving work within a python 'printing' module: https://github.com/thjc/mapnik-svg
     o -- Dane Springmeyer - April 5, 2011 

----
# Gradient support for polygons
# Description
When rendering thematic maps like choropleth maps, gradients are a popular design tool to create visually more exciting maps. This project would add gradient support to the polygon rendering code. There are several ways to apply gradients to a collection of polygons (which constitute most maps); the user should be able to precisely define a gradient (possibly in several color models) and how to apply it to the polygon features.
# How it would benefit Mapnik Project
Gradient support for polygons would allow users to create more visually pleasing maps and as such will make Mapnik more attractive to users. This project can also result in gradient representations that can be re-used throughout other parts of Mapnik that can be rendered as gradients.
# What student would learn
Computer graphics concepts, Mapnik internals
# Submitter
Roel Vanhout
# Possible Mentors
???
# Technical Issues
Finding a memory-efficient way to apply gradients across multiple polygons, potentially color model issues in rendering libraries.

----

# Layer Composites
## Description

_Note: this was taken over from [ideas GSoC2010](GSOC2010_Ideas) in Composites part and amended with the bitmap filter feature_ 

Mapnik layers should be able to interact with one another just like layers in Photoshop. They could have transfer modes (e.g. screen, hard light, darken), masks, and groups. The XML description for this would be backward-compatible with the current Mapnik stylesheet language, but when new markup is added, such as a mode or opacity attribute on a layer, a Group element around a group of layers, or a Mask layer inside another layer, new behaviors could be seen. An additional feature could be to make bitmap filters work on those layers (gaussian blur, offset and others).
## How it would benefit Mapnik Project

Mapnik would natively create complex, layered maps like the amazing TopOSM.
## What student would learn

The student would learn the internals of Mapnik and the math and complexity behind Photoshop-style image compositing.
## Submitter

Mike Migurski (mike@…)
## Possible Mentors

Unsure who would be a willing mentor - I know what would be a great-looking end result and could help with the math and cartography and XML format bits, but I can't offer C++ help of any kind. Maybe this is a bidirectional mentorship? =)
## Technical Issues

* Maybe is possible to use other free software (like imagemagick) instead Photoshop to study layer composing, i'm interesting to develop this idea, i have a little knowledge of C++ but i can study it in these months before GSOC will start  
o -- luca delucchi - March 11, 2009 

* GRASS GIS made something similar with r.his  
o -- luca delucchi - March 12, 2009 

* Seems perhaps related to [#314](https://github.com/mapnik/mapnik/issues/314)  
o -- springmeyer - March 12, 2009 

* TopOSM does indeed use ImageMagick? for compositing, so that may be a good thing to look at. See http://wiki.openstreetmap.org/wiki/TopOSM/Details for more info about how it is done.  
o -- Lars Ahlzen - March 13, 2010 

* See also: http://wiki.openstreetmap.org/wiki/User:Kobezda/GSoC  
o -- Dane Springmeyer - April 6, 2010

* Potential spec could look like: [[Compositing]]  
o -- Dane Springmeyer - April 6, 2010 

* Good brainstorming thread on issues around compositing on #mapnik April 7th: http://mapnik.dbsgeo.com/mapnik_logs/2010/04/07/  
o -- Dane Springmeyer - April 7, 2010 

* Ideas/Compositing - shawnbot's idea around a potential syntax 

----
## Cascadenik: Native C++ implementation of node.js Carto

### Description

Cascadenik has evolved as we've figured out more and more, and integrating less.css syntax with Carto takes another leap. Now it's time to turn it into a native implementation inside mapnik, rather than just living as an external tool.

You'd need to research and maybe develop a parser for the Carto/Cascadenik/less.css syntax, including variables, classes, inheritance, IDs, and the use of attributes from vector features in style declarations - eg. `#mylayer { line-width: expr(1.7 * $POWER); }`

Links:

 * Cascadenik: https://github.com/mapnik/Cascadenik
 * Carto: https://github.com/mapbox/carto

### How it would benefit Mapnik Project

 * Faster parsing performance
 * Match to internal features - rather than being maintained outside and incompatibilities introduced.
 * Less code-smell - the python Cascadenik code has evolved well beyond its initial design
 * Wider adoption of CSS-like syntax for styling maps, lowering barriers

### What student would learn

A hell of a lot about styling maps :) Seriously though, exploring the depths of mapnik's rendering options. Designing and implementing syntax parsing of less.css/css in C++, and having it extensible as we continue to add new symbolizers and options.

### Submitter

Rob Coup

### Possible Mentors

Rob Coup, Dane Springmeyer

### Technical Issues

todo

----
## Cascadenik/Carto: SLD Converter
### Description

Mapnik to Geoserver already started e.g https://github.com/dwins/mapnik2geotools/

SLD is an OGC standard for map styling. It's XML and isn't really human-editable. It makes peoples eyes bleed. Cascadenik & Carto are CSS-like ways to define map styles. They're easy, like styling a web page.

Being able to compile a set of Cascadenik/Carto styles into corresponding SLD would be great! Build styles easily, yet have them standards-compliant for use in/with WxS servers.

First priority would be Cascadenik/Carto > SLD. Second priority would be the reverse.

Links:

 * SLD standard: http://www.opengeospatial.org/standards/sld
 * SLD in GeoServer: http://docs.geoserver.org/latest/en/user/styling/index.html
 * Cascadenik: https://github.com/mapnik/Cascadenik
 * Carto: https://github.com/mapbox/carto


### How it would benefit Mapnik Project

People could use Cascadenik/Carto styles to set up rendering in GeoServer, etc. This drives the popularity of the Cascadenik/Carto syntax and the mapnik project.

### What student would learn

XML, Cascadenik, Carto, CSS-like syntax parsing. You'd need to design and build a flexible framework so that we can easily test compatibility and extend in the future with new rendering features.

### Submitter

Rob Coup

### Possible Mentors

Rob Coup

### Technical Issues

todo