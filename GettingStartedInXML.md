# Tutorial 2  -- 'Hello world' using an XML stylesheet

## Overview

Make sure you have mapnik (and the python bindings) installed and you've successfully run through [Getting Started Python Tutorial](GettingStartedInPython).

 * This page will guide you through using the Mapnik python bindings along with a separate XML file for your map styles.

 * This tutorial expects that you are running Mapnik 2.x or greater. The command `mapnik-config -v` will show you which version you are running.

Two examples are covered in this tutorial:

1) An XML stylesheet is rendering that exactly matches the map output from the pure python example in [Getting Started Python Tutorial](GettingStartedInPython).

2) An XML stylesheet is showcased that uses a world borders dataset with population attributes to create a chloropleth map (aka thematic) by population size.

## Step 1

### Hello World XML

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

Now, we need some data to render, let's use a shapefile of world border polygons from http://www.naturalearthdata.com. You can download the data from this wiki's local copy [here](data/) or directly from the [Natural Earth Data site](http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/110m-admin-0-countries.zip). Unzip the archive and it should produce four files like `ne_110m_admin_0_countries.shp, ne_110m_admin_0_countries.shx, ne_110m_admin_0_countries.dbf, and ne_110m_admin_0_countries.prj`

To download and unzip on the command line with the do:

    wget https://github.com/mapnik/mapnik/wiki/data/110m-admin-0-countries.zip
    unzip 110m-admin-0-countries.zip # creates ne_110m_admin_0_countries.shp

Next, create the `world_style.xml` file referenced in the `world_map.py` script. Copy this XML and save to a file called `world_style.xml` in the same directory as `world_map.py` script.

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

Now run the python script:

    python world_map.py

 * It should output a png graphic in the same folder that matches the Getting Started Tutorial.

----

## Step 2

### World Population XML

Attached below and included as code samples, here is a sample python script that accesses a _'population.xml_ map configuration.

Note: you will need to download the [modified world borders shapefile](http://trac.mapnik.org/attachment/wiki/XMLGettingStarted/world_borders.zip).

 * Note: this file is originally from [Thematic Mapping Blog](http://thematicmapping.org/downloads/world_borders.php). The version attached here is the simpler shapefile provided there with some modification made to avoid problems that occur when displaying the map in projections such as 900913/3785 (this tutorial does not use this projection so you can use the original shapefiles as well). See [ticket 308](https://github.com/mapnik/mapnik/issues/308) for details.

This script should result in a graphic like this:

[[/images/world_population_minimized.png]]

```python
    #!/usr/bin/env python
    
    import mapnik
    mapfile = "population.xml"
    m = mapnik.Map(1400, 600)
    mapnik.load_map(m, mapfile)
    bbox = mapnik.Envelope(mapnik.Coord(-180.0, -75.0), mapnik.Coord(180.0, 90.0))
    m.zoom_to_box(bbox) 
    mapnik.render_to_file(m, 'world_population.png', 'png')
```

And here is the xml file:

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE Map>
    <!-- Sample Mapnik XML template by Dane Springmeyer -->
    <Map bgcolor="white" srs="+proj=latlong +datum=WGS84">
      
      <Style name="population">
    
         <Rule>
          <!-- Built from Seven Class sequential YIGnBu from www.colorbrewer.org -->
          <!-- Quantile breaks originally from QGIS layer classification -->
          <Filter>[POP2005] = 0 </Filter>
          <PolygonSymbolizer>
            <CssParameter name="fill">#ffffcc</CssParameter>
          </PolygonSymbolizer>
          <!-- Outlines for Antarctica look good -->
          <LineSymbolizer>
            <CssParameter name="stroke">black</CssParameter>
            <CssParameter name="stroke-width">.1</CssParameter>
          </LineSymbolizer>
         </Rule>
         
         <Rule>
          <Filter>[POP2005] &gt; 0 and [POP2005] &lt; 15000</Filter>
          <PolygonSymbolizer>
            <CssParameter name="fill">#c7e9b4</CssParameter>
          </PolygonSymbolizer>
          <!-- Outlines for Antarctica look good -->
          <LineSymbolizer>
            <CssParameter name="stroke">black</CssParameter>
            <CssParameter name="stroke-width">.1</CssParameter>
          </LineSymbolizer>
         </Rule>
         
         <Rule>
          <Filter>[POP2005] &gt;= 15000 and [POP2005] &lt; 255000</Filter>
          <PolygonSymbolizer>
            <CssParameter name="fill">#7fcdbb</CssParameter>
          </PolygonSymbolizer>
         </Rule>
         
         <Rule>
          <Filter>[POP2005] &gt;= 255000 and [POP2005] &lt; 1300000</Filter>
          <PolygonSymbolizer>
            <CssParameter name="fill">#1d91c0</CssParameter>
          </PolygonSymbolizer>
         </Rule>
         
         <Rule>
          <Filter>[POP2005] &gt;= 1300000 and [POP2005] &lt; 4320000</Filter>
          <PolygonSymbolizer>
            <CssParameter name="fill">#41b6c3</CssParameter>
          </PolygonSymbolizer>
         </Rule>
              
         <Rule>
          <Filter>[POP2005] &gt;= 4320000 and [POP2005] &lt; 9450000</Filter>
          <PolygonSymbolizer>
            <CssParameter name="fill">#225ea8</CssParameter>
          </PolygonSymbolizer>
         </Rule>
              
         <Rule>
          <Filter>[POP2005] &gt;= 9450000 and [POP2005] &lt; 25650000</Filter>
          <PolygonSymbolizer>
            <CssParameter name="fill">#225ea8</CssParameter>
          </PolygonSymbolizer>
         </Rule>
              
         <Rule>
          <Filter>[POP2005] &gt;= 25650000 and [POP2005] &lt; 1134000000</Filter>
          <PolygonSymbolizer>
            <CssParameter name="fill">#122F7F</CssParameter>
          </PolygonSymbolizer>
         </Rule>
              
         <Rule>
          <ElseFilter/> <!-- This will catch all other values - in this case just India and China -->
          <!-- A dark red polygon fill and black outline is used here to highlight these two countries -->
          <PolygonSymbolizer>
            <CssParameter name="fill">darkred</CssParameter>
          </PolygonSymbolizer>
          <LineSymbolizer>
            <CssParameter name="stroke">black</CssParameter>
            <CssParameter name="stroke-width">.7</CssParameter>
          </LineSymbolizer>
         </Rule>
        
       </Style>
        
       <Style name="countries_label">
         <Rule>
          <!--  Only label those countries with over 9 Million People -->
          <!--  Note: Halo and Fill are reversed to try to make them subtle -->
          <Filter>[POP2005] &gt;= 4320000 and [POP2005] &lt; 9450000</Filter>
          <TextSymbolizer name="NAME" face_name="DejaVu Sans Bold" size="7" fill="black" halo_fill= "#DFDBE3" halo_radius="1" wrap_width="20" spacing="5" allow_overlap="false" avoid_edges="false" min_distance="10"/>
         </Rule>
              
         <Rule>
          <!--  Only label those countries with over 9 Million People -->
          <!--  Note: Halo and Fill are reversed to try to make them subtle -->
          <Filter>[POP2005] &gt;= 9450000 and [POP2005] &lt; 25650000</Filter>
          <TextSymbolizer name="NAME" face_name="DejaVu Sans Book" size="9" fill="black" halo_fill= "#DFDBE3" halo_radius="1" wrap_width="20" spacing="5" allow_overlap="false" avoid_edges="false" min_distance="10"/>
         </Rule>
         
         <Rule>
          <!--  Those with over 25 Million get larger labels -->
          <Filter>[POP2005] &gt;= 25650000 and [POP2005] &lt; 1134000000</Filter>
          <TextSymbolizer name="NAME" face_name="DejaVu Sans Book" size="12" fill="white" halo_fill= "#2E2F39" halo_radius="1" wrap_width="20" spacing="5" allow_overlap="false" avoid_edges="true" min_distance="10"/>
         </Rule>
              
         <Rule>
          <!--  Those with over 25 Million get larger labels -->
          <!--  Note: allow_overlap is true here to allow India to sneak through -->
          <Filter>[POP2005] &gt;= 1134000000</Filter>
          <TextSymbolizer name="NAME" face_name="DejaVu Sans Book" size="15" fill="white" halo_fill= "black" halo_radius="1" wrap_width="20" spacing="5" allow_overlap="true" avoid_edges="true" min_distance="10"/>
         </Rule>
      </Style>
      
      <Layer name="countries" srs="+proj=latlong +datum=WGS84" status="on">
        <!-- Style order determines layering hierarchy -->
        <!-- Labels go on top so they are listed second -->
        <StyleName>population</StyleName>
        <StyleName>countries_label</StyleName>
        <Datasource>
          <Parameter name="type">shape</Parameter>
         <!-- FIXME -->
         <!-- Note:  'TM_WORLD_BORDERS_SIMPL-0.3' is the name of the shapefile (without the .shp file extension) -->
          <Parameter name="file">/PATH/TO/THE/TM_WORLD_BORDERS_SIMPL-0.3</Parameter>
        </Datasource>
      </Layer>
    
    </Map>
```