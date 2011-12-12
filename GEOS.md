<!-- Name: GEOS -->
<!-- Version: 6 -->
<!-- Last-Modified: 2011/08/10 13:41:42 -->
<!-- Author: springmeyer -->

```html
    <h2 style="text-align: left; color: red">WARNING: experimental !</h1>
```

Mapnik's PluginArchitecture supports the use of different input formats.

One such plugin supports writing inline [WKT](http://en.wikipedia.org/wiki/Well-known_text) geometries directly in XML files or python, thus allowing to design geometries directly into mapnik withouth the need to access separate files or database. This is extremely useful to build legends, or layer styles images to put in layers controls widgets, or eventually visualize fixed geometries in your maps.


## Installation (On Linux)

Check if you have the GEOS library installed:

```sh
    $ geos-config --version
    3.2.0
```

If not, install it from [here](http://trac.osgeo.org/geos/) or use your package system on your distro.

If scons is unable to find the needed headers and library, make sure you define where they are in _config.py_:


    GEOS_INCLUDES='/usr/local/include'
    GEOS_LIBS='/usr/local/lib'

Make sure that running _python scons/scons.py DEBUG=y_ shows the following line

    Checking for C library geos_c... yes

To check if the geos plugin built and was installed correctly, try the usual Python _from mapnik import *_ on a DEBUG=y build, and look for the following debug line

    registered datasource : geos

## Parameters

| *parameter*       | *value*  | *description* | *default* |
|:------------------|----------|---------------|----------:|
| wkt               | string       | valid Well-Known-Text string describing the geometry to display | |
| extent            | string       | extent of the passed geometry | determined by the WKT geometry |
| gid               | integer      | specify the geometry id, useful if you need to give it an id and display it with a TextSymbolizer | 0 |
| field_data        | string       | additional text of the geometry, if you need to give it an id and display it with a TextSymbolizer | |
| field_name        | string       | name of the field to use in a TextSymbolizer to display the "field_data" value | name |
| multiple_geometries  | boolean   | wheter to use multiple different objects or a single one when dealing with multi-objects (this is mainly related to how the label are used in the map, one label for a multi-polygon or one label for each polygon of a multi-polygon)| false |
| encoding              | string       | internal file encoding | utf-8 |

## Usage

### Python

Instantiate a datasource like:

```python
    lyr = Layer('WKT Rectangle')
    lyr.datasource = Geos(wkt='POLYGON((0 0, 10 0, 10 10, 0 10, 0 0))')
```

### XML

If you are using XML mapfiles to style your data, then using a datasource looks like:

```xml
      <Layer name="WKT Rectangle" status="on">
        <StyleName>RectangleStyle</StyleName>
        <Datasource>
          <Parameter name="wkt">POLYGON((0 0, 10 0, 10 10, 0 10, 0 0))</Parameter>
        </Datasource>
      </Layer>
```

### C++

Plugin datasource initialization example code can be found on PluginArchitecture.

A  datasource may be created as follows:

```c
    {
        parameters p;
        p["type"]="geos";
        p["wkt"]="POLYGON((0 0, 10 0, 10 10, 0 10, 0 0))";
        p["extent"]="0,0,10,10"; // optional
    
        set_datasource(datasource_cache::instance()->create(p));
    
        Layer lyr("WKT Rectangle");
        lyr.add_style("RectangleStyle");
        m.addLayer(lyr);
    }
```