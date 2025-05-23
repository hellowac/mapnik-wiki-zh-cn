# Tutorial 3 -- Thematic map of world population

## Overview

This tutorial is designed to introduce a few more advanced Mapnik styling features, mainly `Rules` and `Filters`. This XML file is only compatible with Mapnik 2.x and above.

This script should result in a graphic similar to:

![](images/world_population.png)

* Note: text labeling positions may be different between Mapnik versions.

## Step 1: data

For this tutorial we'll use the same world borders shapefile from natural earth used for the first two tutorials. Refer to either [Tutorial 1](GettingStartedInPython) or [Tutorial 2](GettingStartedInXML) for details.

## Step 2: Script

Save the below code into a file called `world_population.py`:

```python
#!/usr/bin/env python

import mapnik
mapfile = "world_population.xml"
m = mapnik.Map(1400, 600)
mapnik.load_map(m, mapfile)
bbox = mapnik.Envelope(mapnik.Coord(-180.0, -75.0), mapnik.Coord(180.0, 90.0))
m.zoom_to_box(bbox) 
mapnik.render_to_file(m, 'world_population.png', 'png')
```

## Step 3: Stylesheet

Save the below XML into a file called `world_population.xml` in the same directory as the `world_population.py` python script:

```xml
<!DOCTYPE Map>
<!-- Sample Mapnik XML template by Dane Springmeyer -->
<Map srs="+proj=latlong +datum=WGS84" background-color="white" minimum-version="0.7.2">
  
  <Style name="population">

     <!-- Built from Seven Class sequential YIGnBu from www.colorbrewer.org -->
     <!-- Quantile breaks originally from QGIS layer classification -->
     <Rule>
      <Filter>[POP_EST] &gt; -1 and [POP_EST] &lt; 15000</Filter>
      <PolygonSymbolizer fill="#c7e9b4"/>
      <LineSymbolizer stroke="black" stroke-width=".1"/>
     </Rule>
     
     <Rule>
      <Filter>[POP_EST] &gt;= 15000 and [POP_EST] &lt; 255000</Filter>
      <PolygonSymbolizer fill="#7fcdbb"/>
      <LineSymbolizer stroke="black" stroke-width=".1"/>
     </Rule>
     
     <Rule>
      <Filter>[POP_EST] &gt;= 255000 and [POP_EST] &lt; 1300000</Filter>
      <PolygonSymbolizer fill="#1d91c0"/>
     </Rule>
     
     <Rule>
      <Filter>[POP_EST] &gt;= 1300000 and [POP_EST] &lt; 4320000</Filter>
      <PolygonSymbolizer fill="#41b6c3"/>
     </Rule>
          
     <Rule>
      <Filter>[POP_EST] &gt;= 4320000 and [POP_EST] &lt; 9450000</Filter>
      <PolygonSymbolizer fill="#225ea8"/>
     </Rule>
          
     <Rule>
      <Filter>[POP_EST] &gt;= 9450000 and [POP_EST] &lt; 25650000</Filter>
      <PolygonSymbolizer fill="#225ea8"/>
     </Rule>
          
     <Rule>
      <Filter>[POP_EST] &gt;= 25650000 and [POP_EST] &lt; 1134000000</Filter>
      <PolygonSymbolizer fill="#122F7F"/>
     </Rule>
          
     <Rule>
      <ElseFilter/> 
      <!-- This will catch all other values - in this case just India and China -->
      <!-- A dark red polygon fill and black outline is used here to highlight these two countries -->
      <PolygonSymbolizer fill="darkred"/>
      <LineSymbolizer stroke="black" stroke-width=".7"/>
     </Rule>
    
   </Style>
    
   <Style name="countries_label">
     <Rule>
      <!--  Only label those countries with over 9 Million People -->
      <!--  Note: Halo and Fill are reversed to try to make them subtle -->
      <Filter>[POP_EST] &gt;= 4320000 and [POP_EST] &lt; 9450000</Filter>
      <TextSymbolizer size="7" fill="black" face-name="DejaVu Sans Bold" halo-fill="#DFDBE3" halo-radius="1" wrap-width="20">[NAME]</TextSymbolizer>
     </Rule>
          
     <Rule>
      <!--  Only label those countries with over 9 Million People -->
      <!--  Note: Halo and Fill are reversed to try to make them subtle -->
      <Filter>[POP_EST] &gt;= 9450000 and [POP_EST] &lt; 25650000</Filter>
      <TextSymbolizer size="9" fill="black" face-name="DejaVu Sans Book" halo-fill="#DFDBE3" halo-radius="1" wrap-width="20">[NAME]</TextSymbolizer>
     </Rule>
     
     <Rule>
      <!--  Those with over 25 Million get larger labels -->
      <Filter>[POP_EST] &gt;= 25650000 and [POP_EST] &lt; 1134000000</Filter>
      <TextSymbolizer size="12" fill="white" face-name="DejaVu Sans Book" halo-fill="#2E2F39" halo-radius="1" wrap-width="20">[NAME]</TextSymbolizer>
     </Rule>
          
     <Rule>
      <!--  Those with over 25 Million get larger labels -->
      <!--  Note: allow_overlap is true here to allow India/China to sneak through -->
      <Filter>[POP_EST] &gt;= 1134000000</Filter>
      <TextSymbolizer size="15" fill="white" face-name="DejaVu Sans Book" halo-fill="black" halo-radius="1" wrap-width="20" allow-overlap="true" avoid-edges="true">[NAME]</TextSymbolizer>
     </Rule>
  </Style>
  
  <Layer name="countries" srs="+proj=latlong +datum=WGS84" status="on">
    <!-- Style order determines layering hierarchy -->
    <!-- Labels go on top so they are listed second -->
    <StyleName>population</StyleName>
    <StyleName>countries_label</StyleName>
    <Datasource>
      <Parameter name="type">shape</Parameter>
      <Parameter name="file">ne_110m_admin_0_countries.shp</Parameter>
    </Datasource>
  </Layer>

</Map>
```
