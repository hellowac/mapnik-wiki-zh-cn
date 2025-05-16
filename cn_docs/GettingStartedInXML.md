# Tutorial 2  -- 'Hello world' using an XML stylesheet

## Overview

Make sure you have mapnik (and the python bindings) installed and you've successfully run through [Getting Started Python Tutorial](GettingStartedInPython).

* This page will guide you through using the Mapnik python bindings along with a separate XML file for your map styles.

* This tutorial expects that you are running Mapnik 2.x or greater. The command `mapnik-config -v` will show you which version you are running.

This tutorial covers using an XML stylesheet to rendering output that exactly matches the map output from the pure python example in [Getting Started Python Tutorial](GettingStartedInPython).

## Step 1: rendering script

First you will need a python script that sets the basic map parameters and points to the XML stylesheet. Copy the code below and save to a file called `world_map.py`.

```python
#!/usr/bin/env python
import mapnik
stylesheet = 'world_style.xml'
image = 'world_style.png'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all() 
mapnik.render_to_file(m, image)
print "rendered image to '%s'" % image
```

## Step 2: data

Now, we need some data to render. Let's use a shapefile of world border polygons from <http://naturalearthdata.com>. Download the data from this wiki's local cache [here](data/110m-admin-0-countries.zip) or directly from the [Natural Earth Data site](http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/110m-admin-0-countries.zip). Unzip the archive in the same directory as the `world_map.py`. Once unzipped, you should see four files like:

    ne_110m_admin_0_countries.shp
    ne_110m_admin_0_countries.shx
    ne_110m_admin_0_countries.dbf
    ne_110m_admin_0_countries.prj

To download and unzip on the command line with the do:

    wget https://github.com/mapnik/mapnik/wiki/data/110m-admin-0-countries.zip
    unzip 110m-admin-0-countries.zip # creates ne_110m_admin_0_countries.shp

## Step 3: style

Finally, create the `world_style.xml` file referenced in the `world_map.py` script. Copy this XML and save to a file called `world_style.xml`, also in the same directory as `world_map.py` script.

```xml
<Map background-color="steelblue" srs="+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs">

  <Style name="My Style">
    <Rule>
      <PolygonSymbolizer fill="#f2eff9" />
      <LineSymbolizer stroke="rgb(50%,50%,50%)" stroke-width="0.1" />
    </Rule>
  </Style>

  <Layer name="world" srs="+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs">
    <StyleName>My Style</StyleName>
    <Datasource>
      <Parameter name="type">shape</Parameter>
      <Parameter name="file">ne_110m_admin_0_countries.shp</Parameter>
    </Datasource>
  </Layer>

</Map>
```

## Step 4: test

Now run the python script:

    python world_map.py

* It should output a png graphic in the same folder that matches the Getting Started Tutorial.

Hint: if you would like to run the script without first typing `python` you can do:

    chmod +x world_map.py # to make it executable
    ./world_map.py
