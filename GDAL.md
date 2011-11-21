<!-- Name: GDAL -->
<!-- Version: 18 -->
<!-- Last-Modified: 2010/11/13 10:18:41 -->
<!-- Author: kunitoki -->
[[TOC]]

Mapnik's PluginArchitecture supports the use of different input formats.

This plugin supports the [GDAL](http://www.gdal.org/) library in order to read a lot of spatial geo raster data from multiple formats.


# Installation

Make sure that running _python scons/scons.py _ shows the following line

    Checking for gdal-config --libs... yes
    Checking for gdal-config --cflags... yes

To check if the gdal plugin built and was installed correctly you can do:

    >>> from mapnik import DatasourceCache as c
    >>> 'gdal' in c.plugin_names()
    True


# Parameters

|| *parameter* || *value*  || *description* || *default* ||
|| file            || string       || file of the raster to be read || ||
|| base            || string       || base path where to search for file parameter || ||
|| shared          || boolean      || wheter to open the dataset in shared mode (allowing save of resources when using multiple access to the same files) or not || false ||
|| band            || integer      || request for a specific raster band index, -1 means all bands || -1 ||
|| filter_factor   || double       || filter to use when querying for raster data || 0.0 ||


# Styling

To style a layer from GDAL use the RasterSymbolizer


# Usage

This plugin in Mapnik >= 0.7.0 supports reading overviews created with http://www.gdal.org/gdaladdo.html

## Python


    #!python
    style=Style()
    rule=Rule()
    rule.symbols.append(RasterSymbolizer())
    style.rules.append(rule)
    map.append_style('Raster Style',style)
    lyr = Layer('GDAL Layer from TIFF file')
    lyr.datasource = Gdal(base='/path/to/your/data',file='raster.tif')
    lyr.styles.append('Raster Style')

See the docstring at: http://svn.mapnik.org/trunk/docs/api_docs/python/mapnik-module.html#Gdal

## XML


    #!xml
    <!-- NOTE: must be in the same SRS as your map-->
    <Layer name="GDAL Layer from TIFF file">
    	<StyleName>raster</StyleName>
    	<Datasource>
    		<Parameter name="type">gdal</Parameter>
    		<Parameter name="file">/path/to/your/data/raster.tiff</Parameter>
    	</Datasource>
    </Layer>

## C++

Plugin datasource initialization example code can be found on PluginArchitecture.

A GDAL datasource may be created as follows:


    #!C
    {
        parameters p;
        p["type"]="gdal";
        p["file"]="/path/to/your/data/raster.tiff";
    
        set_datasource(datasource_cache::instance()->create(p));
    
        Layer lyr("GDAL Layer from TIFF file");
        lyr.add_style("raster");
        m.addLayer(lyr);
    }

## Further References
