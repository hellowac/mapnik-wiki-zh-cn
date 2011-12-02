<!-- Name: RasterSymbolizer -->
<!-- Version: 19 -->
<!-- Last-Modified: 2010/03/12 07:06:11 -->
<!-- Author: albertov -->
# RasterSymbolizer

The RasterSymbolizer is used to render an image from any [GDAL supported format](http://www.gdal.org/formats_list.html) using the [wiki:GDAL] plugin or from GeoTiff's using the [wiki:Raster] plugin.

 * Mapnik does not yet support on-the-fly reprojection of raster layers (like it does for vector layers)
  * Therefore it is necessary to first (externally) warp an image to the Spatial Reference System (srs) used in the map (e.g. using the `gdalwarp` command from the gdal-utilities).

 * As of Mapnik 0.6.0 the RasterSymbolizer supports transparency and composition modes.
  * See the original ticket for details: #259
  * See also [wiki:Compositing] for some of the effects.

 * This Symbolizer is often used with DEM (digital elevation model) data containing missing values (for example NASA SRTM DEM data); to achieve nice rendering, the [gdal_fillnodata.py](http://www.gdal.org/gdal_fillnodata.html) tool might be useful.

 * As of Mapnik 0.8 the RasterSymbolizer can be assigned a RasterColorizer to color a raw data raster according to a palette. This is useful for visualizing scientific data, dynamically changing the color gradient of a DEM, etc...

[[BR]]
||[[Image(http://pavlenko.f2s.com/tiles/srtm3/9/277/197.png)]]||[[Image(http://media.mapnik.org/tiles/relief/7/63/42.png)]]||[[Image(http://1.tiles.ump.waw.pl/ump_tiles/12/2265/1395.png)]]||[[Image(http://toolserver.org/~cmarqu/hill/12/2265/1395.png)]] ||
|| || || ||Processed as described in http://wiki.openstreetmap.org/wiki/Hillshading_using_the_Alpha_Channel_of_an_Image||

# Usage

| *parameter* | *value* | *description* |
--------------|---------|-----------|
| opacity         |  0.0 - 1.0   | 1 is fully opaque while zero is fully transparent and .5 would be 50% transparent |
| mode            | grain_merge, grain_merge2, multiply, multiply2, divide, divide2, screen, hard_light | Compositing/Merging effects with image below raster level (?). The formulas for combinding foreground (raster) and background are: grain_merge: bg + fg - 0.5, grain_merge2: bg + 2*fg - 1.0, multiply: fg * bg, multiply2: 2 * fg * bg, divide: bg / fg, divide2: 2*bg / fg, screen: (1-fg)*(1-bg), hardlight: see [[http://docs.gimp.org/en/gimp-concepts-layer-modes.html#id2834930]] |
| scaling         | fast, bilinear, bilinear8 || fast: nearest neighbour, bilinear: bilinear interpolation for all 4 channels (RGBA), bilinear8 like bilinear, but only one channel assumed |


There are two types of raster datasources: *gdal* or *raster*:
 * The [wiki:GDAL] plugin is more convenient as it can read the file extents automatically and supports any GDAL-supported type of file
 * The [wiki:Raster] driver only works with Tiled or Stripped GeoTIFF files and requires manually setting the file bounds, but can be faster.

## XML Layers

See the [wiki:GDAL] plugin and [wiki:Raster] plugin pages for more info


## XML Styles

Default (simply renders a copy of the raster)


    #!xml
    <Style name="My Style">
        <Rule>
            <RasterSymbolizer/>
        </Rule>
    </Style>

Using the new 0.6.0 release opacity / merging / scaling options:

    #!xml
    <Style name="raster">
        <Rule>
            <RasterSymbolizer>
                <CssParameter name="opacity">0.5</CssParameter>
                <!--<CssParameter name="scaling">fast</CssParameter>-->
                <CssParameter name="scaling">bilinear</CssParameter>
                <!--<CssParameter name="scaling">bilinear8</CssParameter>-->
    
                <!--<CssParameter name="mode">grain_merge</CssParameter>-->
                <!--<CssParameter name="mode">grain_merge2</CssParameter>-->
                <!--<CssParameter name="mode">multiply</CssParameter>-->
                <CssParameter name="mode">multiply2</CssParameter>
                <!--<CssParameter name="mode">divide</CssParameter>-->
                <!--<CssParameter name="mode">divide2</CssParameter>-->
                <!--<CssParameter name="mode">screen</CssParameter>-->
                <!--<CssParameter name="mode">hard_light</CssParameter>-->
            </RasterSymbolizer>
        </Rule>
    </Style>

## Python Styles


    #!python
    s = Style()
    r=Rule()
    r.symbols.append(RasterSymbolizer())
    s.rules.append(r)

## C++

` FIXME `
