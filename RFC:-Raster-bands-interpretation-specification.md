Reading raster data into a mapnik::raster requires interpreting it as either RGB(A) or data.
When the style uses a [[RasterColorizer]], a "data" interpretation is expected.
Otherwise an "RGB(A)" interpretation is expected.

The only raster plugin supporting "data" interpretation is currently the [[GDAL]] one.
The [[PgRaster]] plugin under development at time of writing is currently using the same strategy used by the GDAL plugin to decide how to interpret the input rasters. But such strategy has limitations. For example it cannot re-order RGB(A) bands, nor find a grayscale in a band which is not the first one.

This page is an attempt to standardize bands extraction and interpretation in a way that is backward compatible and improves flexibility. Plugins that are willing to adhere to this specification would accept a "band" parameter as the one supported by GDAL but with extended semantic.

The band parameter could have the following values:

 - rgb[:<r>,<g>,<b>]
   Where <r>, <g> and <b> are integer representing 1-based band indexes.
   Specifying 'rgb' would be interpreted as 'rgb:1,2,3'

 - rgba[:<r>,<g>,<b>,<a>]
   Where <r>, <g>, <b> and <a> are integer representing 1-based band indexes.
   Specifying 'rgba' should be interpreted as 'rgba:1,2,3,4'

 - grayscale[:<n>]
   Where <n> is an integer representing 1-based band indexes.
   Specifying 'grayscale' should be interpreted as 'grayscale:1'

 - data[:<n>]
   Where <n> is an integer representing 1-based band indexes.
   Specifying 'data' should be interpreted as 'data:1'

 - <n>
   Interpreted as data:<n>
   This is for backward compatibility with the GDAL plugin

 - auto
   The default value, if band parameter is omitted, enables guess based on input raster:
   - If the input has 3 bands, 'rgb' assumed
   - If the input has 4 bands, 'rgba' assumed
   - If the input has 1 band, 'grayscale' assumed

 - -1
   Same as auto
   This is for backard compatibility with the GDAL plugin