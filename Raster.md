<!-- Name: Raster -->
<!-- Version: 8 -->
<!-- Last-Modified: 2010/11/14 07:09:01 -->
<!-- Author: kunitoki -->
[[TOC]]

This plugin supports reading tiff and geotiff files.

Tiled or Stripped tiff files are required and when rasters are small < 200-300 MB this driver is faster that the [wiki:GDAL] plugin.

If files are larger it is recommended to build GDAL overviews (with gdaladdo command) and instead read with the [wiki:GDAL] plugin.
 * Note: overviews support is available only in Mapnik >= 0.7.0.

A drawback(or advantage!) of this plugin is that it requires manually setting the file bounds.
 * hint: create a GDAL datasource from your tiff in python, call the envelope() method to get the bounds, and use those.

For other plugins see: PluginArchitecture

# Installation

To check if the raster plugin built and was installed correctly you can do:

    >>> from mapnik import DatasourceCache as c
    >>> 'raster' in c.plugin_names()
    True


# Parameters

|| *parameter* || *value*  || *description* || *default* ||
|| file            || string       || geotiff file path  || ||
|| base            || string       || optional base path where to search for the tiff raster file  || ||
|| lox             || double       || lower x corner of the image in map coordinates || ||
|| loy             || double       || lower y corner of the image in map coordinates || ||
|| hix             || double       || upper x corner of the image in map coordinates || ||
|| hiy             || double       || upper y corner of the image in map coordinates || ||
|| extent          || string       || extent of the image in map coordinates, comma or space separated (at least <lox> <loy> <hix> <hiy> or <extent> should be passed) || ||
|| format          || string       || image format to use, currently only tiff is supported || tiff ||


# Styling

To style a layer use the RasterSymbolizer


# Usage

## Python

See the docstring at: http://svn.mapnik.org/trunk/docs/api_docs/python/mapnik-module.html#Raster

== XML == 


    #!xml
    <!-- NOTE: must be in the same SRS as your map-->
    <Layer name="Raster">
        <StyleName>raster</StyleName>
        <Datasource>
            <Parameter name="type">raster</Parameter>
            <Parameter name="file">/path/to/my/raster/file.tiff</Parameter>
            <Parameter name="lox">min_x</Parameter>
            <Parameter name="loy">min_y</Parameter>
            <Parameter name="hix">max_x</Parameter>
            <Parameter name="hiy">max_y</Parameter>
        </Datasource>
    </Layer>

## C++

Plugin datasource initialization example code can be found on PluginArchitecture.

A Raster datasource may be created as follows:


    #!C
    {
        parameters p;
        p["type"]="raster";
        p["file"]="/path/to/my/raster/file.tiff";
        p["lox"]=min_x;
        p["loy"]=min_y;
        p["hix"]=max_x;
        p["hiy"]=max_y;
    
        set_datasource(datasource_cache::instance()->create(p));
    
        Layer lyr("Raster");
        lyr.add_style("raster");
        m.addLayer(lyr);
    }


## Further References
