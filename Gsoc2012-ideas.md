# Google Summer of Code Ideas - 2012

Mapnik has applied to participate in Google Summer of Code 2012. ([application](Gsoc2012-application))

Three students were accepted last year: http://mapnik.org/news/2011/04/25/three_students_mapnik_gsoc_2011/

See the main page for more details: [[GSOC2012]]

See also steve8's ideas page: [[Ideas]]


# Project Ideas

Format should be:

## Project Name
### Description
### How it would benefit Mapnik Project
### What student would learn
### Submitter
### Possible Mentors
### Discussion
  * Comment/Idea
   * -- name of person commenting - date

----


## Skia/OpenGL backend

### Description

Mapnik has a pluggable rendering backend system, currently supporting numerous renderers: AGG (antigrain geometry, main rendering for image output), Cairo (alternative renderer for image output + vector formats like PDF and SVG), Grid (json format - utf8 hit grids).

[Skia](http://code.google.com/p/skia/) is the rendering library used in Chrome and has some support for OpenGL on certain hardware. An experimental backend using Skia would be interesting to see if the software rendering pipeline was any faster than AGG (and of similar quality) and if the hardware pipeline was useful for rendering on mobile devices. Alternatively a direct OpenGL backend could also be investigated.

### How it would benefit Mapnik Project

Mapnik is about beautiful maps, but also fast maps. In many common performance critical rendering scenarios using Mapnik, the rendering backend is not the bottleneck - e.g. its not AGG that is taking the most time, but rather io and pulling/processing data. But, focused optimizations in Mapnik core are starting to change this and the renderer may become more of the bottleneck in the future - so seeking the fastest possible rendering is desirable.

### What student would learn
They would learn a lot about the latest advances in GPU's, the tradeoffs of hardware acceleration, and the details of modern graphics libraries for desktop and mobile, like Skia.

### Submitter

Dane Springmeyer

### Possible Mentors

Dane Springmeyer

### Discussion
  * Comment/Idea
   * -- name of person commenting - date

----

## Gorgeous multi-lingual text rendering

### Description

The quality of label placement and text rendering makes the difference between a good map and amazing map. And a beautiful map is useless if the text is not perfectly legible.

Mapnik, through the Freetype library, has pretty nice text display. And through previous GSOC projects by @Herm, has an awesome framework for advanced text placement and formatting. But at this time Mapnik has numerous bugs and problems when it comes to non-latin languages: https://github.com/mapnik/mapnik/wiki/InternationalText.

This is no surprise, text rendering with unicode is extremely hard: http://behdad.org/text.

But, we have to fix this - we need excellent support for text positioning and display in all languages. You could become the master of how text rendering works and make the maps made with Mapnik massively more useful to people around the world, particularly in places like China, India, Cambodia, and the Middle east.

### How it would benefit Mapnik Project

The idea here is to benefit not only the Mapnik project, but primarily projects like OpenStreetMap and all the other users of Mapnik making international, global baselayers.

### What student would learn

Would become an expert in Freetype, ICU, Harfbuzz, and Pango. Would learn the nuances and challenges of label placement algorithms. Would learn about the tradeoffs in text rendering perfection and performance.

### Submitter

Dane Springmeyer

### Possible Mentors

Dane Springmeyer

### Discussion
  * Comment/Idea
   * -- name of person commenting - date

----

## Packaging of Mapnik2
### Description:
This project can bring mapnik2 to use in a very easy way, just like apt-get install mapnik2 and it will be ready to use. This will include all the packaging work to add into linux distribution's main repository specially of Ubuntu's which is being used much more than other distributions and all the scripting work to install the mapnik2 by checking all the required dependencies and then also install them automatically and finally is the troubleshooting i.e if mapnik fails to install in any way then to do troubleshooting by itself to install it on user's machine.
### How it would benefit Mapnik Project
It will make mapnik to use very easily just like other software available to use and definitely will increase the usability of Mapnk  
### What student would learn
Packaging, Shell Scripting and Understanding of Mapnik's code and its complete use. 
### Submitter
Parveen Arora

### Possible Mentors

### Discussion
  * What would this provide that is not already done with https://github.com/mapnik/mapnik-packaging/tree/master/debian-nightlies and https://launchpad.net/~mapnik?
   * -- springmeyer - mar 9th, 2012
----