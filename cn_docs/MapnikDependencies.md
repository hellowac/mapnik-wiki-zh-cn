<!-- Name: MapnikDependencies -->
<!-- Version: 3 -->
<!-- Last-Modified: 2009/11/11 11:10:04 -->
<!-- Author: springmeyer -->
## Mapnik Dependencies

Mapnik requires the Boost libraries, International Components for Unicode (ICU), Freetype, Proj4, and a variety of image libraries.

Installing Boost is often new to mapnik users, but the majority of remaining dependencies are more familiar.

If you have previously built or installed other open source graphics or mapping applications it is likely that many of the remaining dependencies are already installed.

Notes on installing Mapnik dependencies are included within each [MapnikInstallation platform specific instructions].

## Learn More

 * *Input Format Plugins*
  * PostGIS/PostgreSQL - to read data using the Mapnik PostGIS plugin.
   * [PostgreSQL](http://www.postgresql.org/): Relational database system
   * [PostGIS](http://www.postgis.org/): Spatial extension to PostgreSQL
  * [GDAL](http://trac.osgeo.org/gdal/wiki/FAQGeneral#WhatdoesGDALstandsfor) - to read raster data using the Mapnik GDAL plugin
   * [GDAL](http://www.gdal.org/): Geospatial Data Abstraction Library
   * [GDAL Formats](http://www.gdal.org/formats_list.html): Raster Formats supported by GDAL

 * *Libraries* for Imaging
  * libcairo - [Multi-platform 2D graphics library](http://www.cairographics.org/)
  * libcairomm - [C++ wrapper for Cairo graphics](http://www.cairographics.org/cairomm/)
  * pycairo  - [Python bindings for the cairo graphics library](http://www.cairographics.org/pycairo/)
  * tinyxml, spirit, or libxml2  - for XML parsing extensions, see: ManagingLargeXmlFiles

 * *Mapnik WMS* (Web Map Service) dependencies - [WMS on wikipedia](http://en.wikipedia.org/wiki/Web_Map_Service)
  * jonpy.fcgi - [Jon's FastCGI Python module](http://jonpy.sourceforge.net/)
  * libxslt - [XSLT(Extensible Stylesheet Language Transformations) C library](http://xmlsoft.org/XSLT/)
  * libxml2 - [XML C parser](http://xmlsoft.org/)
  * lxml - [Python bindings for the libxml2 and libxslt libraries](http://codespeak.net/lxml/index.html)
  * PIL [Python Imaging Library](http://www.pythonware.com/products/pil/)
  * Proj.4 - see above
  * Apache webserver: Comes pre-installed on Mac OS X
    * Apache2 config is in: /etc/apache2/
    * Apache2 web root is: /Library/WebServer
    * Apache2 cgi-bin is: /Library/WebServer/CGI-Executables
    * Apache2 logs are in: /var/log/apache2/
  * Python handler run as either [FastCGI](http://www.fastcgi.com/) or [mod-fcgid](http://fastcgi.coremail.cn/) 
  * WSGI handler also possible, but undocumented