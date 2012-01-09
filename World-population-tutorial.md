# Tutorial 3 -- Thematic map of world population

## Overview

This tutorial is designed to introduce a few more advanced Mapnik styling features, mainly `Rules` and `Filters`.

## Step 1: data

For this tutorial we'll use the same world borders shapefile from natural earth used for the first two tutorials. Refer to either [Tutorial 1](GettingStartedInPython) or [Tutorial 2](XMLGettingStarted) for details.

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