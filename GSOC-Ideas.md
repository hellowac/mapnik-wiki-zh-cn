# Google Summer of Code Ideas

Mapnik has participated in Google Summer of Code in 2010 (2 students) & 2011 (3 students). In 2012 we had a GSoC student via the OpenStreetMap umbrella project, and in 2013 students can apply via either OSGeo or OpenStreetMap (*not both*). 

Below are some projects we've come up with, which hopefully will interest you! See also [@steve8s ideas page](Ideas) for more "what Mapnik would do in an ideal world".

In general, students will need to:
* have a solid coding (C/C++/Python)
* ideally have had some exposure to mapping/geo (or, get started and experimenting now!)
* be good communicators, we expect weekly public blog posts with progress/successes/problems.
* be motivated and self-driven - we're not going to drag you through this, you need to *want* it!

Questions? Email [Rob](/rcoup) at robert@coup.net.nz

# Project Ideas

## New visual test framework

### Description

The amount of styling options demanded by high performance and high quality cartography is bewildering.

```
$ wget https://raw.github.com/mapnik/mapnik-reference/master/latest/reference.json
$ python
>>> import json
>>> doc = json.loads(open('reference.json','r').read())
>>> count=0
>>> for d in doc['symbolizers'].items(): count += len(d[1])
...
>>> print count
162
```

Combine those 162 properties with the many different [types of datasources](https://github.com/mapnik/mapnik-reference/blob/master/latest/datasources.json) and [output formats]([[OutputFormats]]) Mapnik supports, and all their options and you end up with thousands of combinations of things that interact with variable and massive geodata in interesting ways.

Add sources like OSM, which do not restrict geometry validity and to forge forward in this wild world you need amazing test cases and an amazing framework for creating, evaluating, summarizing, and understanding the test results. They have to be visual so that developers to look at the results to learn about the impact of code and because the visual output is the goal. Regressions need to be prevented, but developers also need easy ways to understand how their code changes potentially many hundreds of test results. So, a code change that fixes a bug, for example in the way that text is placed, should break hundreds of tests because tests should exist already to validate current behavior. But it should also be very easy to update all those tests and confirm, visually that the updates look good.

What could the framework look like? Where can you look for inspiration?

* our existing tests at https://github.com/mapnik/mapnik/tree/master/tests. Note there are not just visual tests, but 'traditional' algorithm/code/performance unit tests as well.
* what test frameworks exist for video encoders/decoders and image processing libraries? (think ffmpeg, videolan, imagemagick, OpenCV, PIL, [node-blend](https://github.com/developmentseed/node-blend/tree/master/test), etc) Which do it really well?
* what test frameworks exist for software with 1000s of combinations?
* how can we optimise test creation/running/reporting/updates for developer efficiency? 
* how could we run it on distributed infrastructure via TravisCI/Jenkins/etc?

What we want in an application:

* to see your experience in Python
* research into what is 'out there'
* a solid proposed approach we can work together to refine

### How it would benefit Mapnik Project

Allows the project to move forward faster - fixing bugs, adding features, and refactoring without needing to just hope that regressions don't appear. The faster bugs/regressions are found, the easier they are to fix. The easier tests are to create and update, the more tests there will be.

### What student would learn

How a modern map rendering framework works. How test frameworks catering to 1000s of possible combinations of options/inputs/outputs can work (because you'll build one!). All about image and geodata formats and their structures and internals. How to optimise testing for developer happiness and developer speed.

### Submitter

[Dane Springmeyer](/springmeyer)

### Possible Mentors

* [Dane Springmeyer](/springmeyer) - dane@dbsgeo.com

### Discussion
  * Comment/Idea
   * -- name of person commenting - date

---

## Anti-Meridian Support
### Description

The anti-meridian (aka 'date line'/180th meridian/+180°/-180°/end of the world) causes problems (eg. [1](http://trac.osgeo.org/mapserver/attachment/ticket/15/mswms_gmap.gif), [2](http://www.youtube.com/watch?v=-t0AV27t8tQ&feature=youtu.be&noredirect=1), [3](https://earth-issues.googlecode.com/issues/attachment?aid=13400000000&name=PolygonCross.jpg&token=DznRVkFPn0C7yeqygJ3rkGEZp8g%3A1364419894395&inline=1), [4](http://cdn.cruisersforum.com/forums/attachment.php?attachmentid=37372&d=1329218601), [5](http://wiki.openstreetmap.org/wiki/180th_meridian) ) for most mapping and geospatial software, since they naively treat our round world as flat. Mapnik is no exception.

* Features with components (eg. MultiPolygons) where [parts are on different sides](http://data.linz.govt.nz/#/layer/785-nz-land-districts/) of the anti-meridian. Think a 
* [Geometries that span](http://koordinates.com/#/layer/1541-new-zealand-region-bathymetry/) the antimeridian  
* [Rasters that span](http://koordinates.com/#/layer/1720-new-zealand-250m-bathymetry-rainbow-2008/) the anti-meridian
* lines/polygons whose coordinates go from +175 to +185 (into the 'next world'), or -175 to -185 (into the 'previous world'), or +175 to -175 (theoretically 'right')
* projection issues - data that 'works' in one coordinate system might not work in another based on naive transformations. At least with geographic (lat/long) coordinate systems we _know_ they wrap, for projected ones (eg. Spherical Mercator) that span the world, we don't even know.
* all the various hacks people have done to source data to make it work in particular software
* extents/bounds/boxes that use (& enforce) minx,maxx rather than left,right
* [Geography data types](http://postgis.net/docs/using_postgis_dbmanagement.html#PostGIS_Geography), which solve it at a datasource level. But we're rendering flat maps!
* output maps that cross the anti-meridian
* tiled maps that go right up to the anti-meridian but don't cross it.

Unfortunately since the bulk of the world's mapping software engineers work in Europe/America/Asia, the problem has never really been dealt to. Ask a New Zealander geographer and you'll get an earful ;)

There are all sorts of approaches to 'solving' it, each with their own performance/complexity/data limitations:

* copying/shifting geometries into previous/next worlds
* splitting geometries on the anti-meridian into separate lines/polygons
* querying multiple extents, checking for duplicates
* rendering multiple extents and gluing together the results

Since Mapnik lives between datasources and rendered maps, we can solve this. That's the project.

What we need to see in a proposal:
* to see your experience and background in C/C++
* Geospatial background - understand geographic and projected coordinate systems, and what happens when you re-project geometries at the anti-meridian.
* Good understanding of the problem, how mapnik (& related geo software like Tilemill, Leaflet, OpenLayers, PostGIS, GeoServer) work right now with the anti-meridian. Create some data, have a play.
* Research into how different software works around it, and what ideas there are.
* A proposed approach we can refine together.
* Thoughts on performance.

### How it would benefit Mapnik Project

Mapnik will be the first FOSS rendering engine that deals with the anti-meridian properly. Users won't need to mangle both datasources *and* map outputs to get working results. 

### What student would learn

More than they ever wanted to know about meridians, projections, coordinate systems, polygon windings, and geospatial data. Be able to out-geo-geek even the geekiest geographers you'll find. Shake your head for years afterwards at all the software that doesn't solve it properly - thanks to you Mapnik will! New Zealand geographers will love you forever.

### Submitter

[Robert Coup](/rcoup)

### Possible Mentors

* [Robert Coup](/rcoup) - robert@coup.net.nz
* [Craig de Stigter](/craigds) - craig.destigter@koordinates.com

### Discussion
  * Comment/Idea
   * -- name of person commenting - date

---

## Prospective (2.5 Dimension) Rendering 
### Description
Mapnik right now print only 2D image. This project could improve a prospective (2.5 Dimension) Rendering. The idea come from Maperitive function that provide map similar these [image 1](http://images2.gazzettaobjects.it/static_images/ciclismo/giroditalia/2012/tappa_19_S03.jpg), [image 2](http://www.gazzetta.it/Speciali/Giroditalia/2011/immagini/zoom/tappa_15_s.jpg)
### How it would benefit Mapnik Project
Mapnik could rendering prospective (2.5 Dimension) image, another beautiful type of maps. This kind of rendering it is very important for outdoor sports: ski resort, cycling or hiking stage are often rendering with  prospective (2.5 Dimension) image.
### What student would learn
The Mapnik core and prospective (2.5 Dimension) rendering.
### Submitter
Luca Delucchi
### Possible Mentors
### Discussion

## Skia/OpenGL backend

### Description

Mapnik has a pluggable rendering backend system, currently supporting numerous renderers: AGG (antigrain geometry, main rendering for image output), Cairo (alternative renderer for image output + vector formats like PDF and SVG), Grid (json format - utf8 hit grids).

[Skia](http://code.google.com/p/skia/) is the rendering library used in Chrome and has some support for OpenGL on certain hardware. An experimental backend using Skia would be interesting to see if the software rendering pipeline was any faster than AGG (and of similar quality) and if the hardware pipeline was useful for rendering on mobile devices. Alternatively a direct OpenGL backend could also be investigated.

What we want to see in your proposal:
* to see your experience and background in C/C++
* to see your experience with OpenGL/Skia/similar rendering software
* a proposed approach we can refine together.

### How it would benefit Mapnik Project

Mapnik is about beautiful maps, but also fast maps. In many common performance critical rendering scenarios using Mapnik, the rendering backend is not the bottleneck - e.g. its not AGG that is taking the most time, but rather io and pulling/processing data. But, focused optimizations in Mapnik core are starting to change this and the renderer may become more of the bottleneck in the future - so seeking the fastest possible rendering is desirable.

### What student would learn
They would learn a lot about the latest advances in GPU's, the tradeoffs of hardware acceleration, and the details of modern graphics libraries for desktop and mobile, like Skia.

### Submitter

[Dane Springmeyer](/springmeyer)

### Possible Mentors

* [Dane Springmeyer](/springmeyer) - dane@dbsgeo.com

### Discussion
  * Comment/Idea
   * -- name of person commenting - date

----

Got more? Format should be:

```
## Project Name
### Description
### How it would benefit Mapnik Project
### What student would learn
### Submitter
### Possible Mentors
### Discussion
  * Comment/Idea
   * -- name of person commenting - date
```