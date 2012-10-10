<!-- Name: SQLite -->
<!-- Version: 11 -->
<!-- Last-Modified: 2010/11/13 10:07:41 -->
<!-- Author: kunitoki -->


Mapnik's PluginArchitecture supports the use of different input formats.

One such plugin supports the sqlite ([SQLite](http://en.wikipedia.org/wiki/SQLite)) / spatialite ([Spatialite](http://www.gaia-gis.it/spatialite)) extension to the popular SQLite database.

# Installation

Make sure that running _python scons/scons.py DEBUG=y_ shows the following line

    Checking for C library sqlite3... yes

To check if the sqlite plugin built and was installed correctly, try the usual Python _from mapnik import *_ on a DEBUG=y build, and look for the following debug line

    registered datasource : sqlite

# Creating an example database

## Getting the tools

First of all we need a bit of external tools for loading and preparing our first spatial database with sqlite.
Go to [Spatialite](http://www.gaia-gis.it/spatialite-2.3/) and download (depending on your arch) the "spatialite executable [statically linked, no deps]" and unpack them in a directory of choice. Also download and unpack [InitSpatialiteSql](http://www.gaia-gis.it/spatialite/init_spatialite-2.2.sql.zip) in the same directory.

If you have problems with your spatial indexes (mbr calculated wrong in tables idx_table_geometry), you will need to rebuild spatialite-2.3 yourself using a recent version of GEOS (>=3.0.3): refer to [Spatialite](http://www.gaia-gis.it/spatialite-2.3) compilation guide.

## Prepare the data

Now execute spatialite on a new empty database:

    user@geo ~/spatialite/ $ spatialite spatial_test.sqlite
    SpatiaLite version ..: 2.3	Supported Extensions:
    	- 'VirtualShape'	[direct Shapefile access]
    	- 'VirtualText		[direct CSV/TXT access]
    	- 'VirtualNetwork	[Dijkstra shortest path]
    	- 'RTree'		[Spatial Index - R*Tree]
    	- 'MbrCache'		[Spatial Index - MBR cache]
    	- 'VirtualFDO'		[FDO-OGR interoperability]
    	- 'SpatiaLite'		[Spatial SQL - OGC]
    PROJ.4 version ......: Rel. 4.6.1, 21 August 2008
    GEOS version ........: 3.0.0-CAPI-1.4.1
    SQLite version ......: 3.6.6.1
    Enter ".help" for instructions
    spatialite> 

From the spatialite shell you must initialize the spatialite tables (_geom_cols_ref_sys_, _geometry_columns_, _spatial_ref_sys_):

    spatialite> .read init_spatialite-2.2.sql ASCII
    1

We import a shapefile directly inside our database (in this example using utf-8 encoding, 3004 as SRID(epsg) and 'geom' as the geometry column). This will take care of creating the table for us, executing *AddGeometryColumn* which will initialize the _geometry_columns_ table and add a BLOB column to our table for the geometry, then it will insert the rows into it:

    spatialite> .loadshp bridges bridges UTF-8 3004 geom
    ========
    Loading shapefile at 'bridges' into SQLite table 'bridges'
    BEGIN;
    CREATE TABLE bridges (
    PK_UID INTEGER PRIMARY KEY AUTOINCREMENT,
    ANNO_COSTR INTEGER,
    RAG_GIUR INTEGER,
    DECORAZ TEXT);
    SELECT AddGeometryColumn('bridges', 'geom', 3004, 'MULTIPOLYGON', 2);
    INSERT INTO ponte (
    PK_UID,ANNO_COSTR,RAG_GIUR,DECORAZ,geom)
    VALUES (1,0,1,'',GeomFromWkb(X'010600000001000000010300000001000000150000001A...',3004));
    ...
    COMMIT;
    
    Inserted 499 rows into 'bridges' from SHAPEFILE
    ========

At this point we can decide also to create the R*Tree index on this table, for speed spatial access to the table:

    spatialite> select CreateSpatialIndex('bridges', 'geom');
    1

You can now exit the spatialite shell:

    spatialite> .quit

# Parameters

| *parameter*       | *value*  | *description* | *default* |
|:------------------|----------|---------------|----------:|
| file                  | string       | sqlite database file path | |
| base                  | string       | optional base path where to search for the sqlite database file | |
| table                 | string       | name of the table to fetch, this can be a sub-query | |
| metadata              | string       | name of the metadata table where the extent and srid of the table are specified | |
| key_field             | string       | name of the id field of the table | OGC_FID | 
| geometry_field        | string       | name of the geometry field, in case you have more than one in a single table | the_geom |
| extent                | string       | maxextent of the geometries | determined by querying the metadata table |
| row_offset            | integer      | number of rows to skip when querying data | 0 |
| row_limit             | integer      | max number of rows to return when querying data, 0 means no limit | 0 |
| wkb_format            | string       | type of WKB in the geometry field blob, this can be "sqlite" or "spatialite" | sqlite |
| use_spatial_index     | boolean      | choose wheter to use the spatial index when fetching data | true |
| multiple_geometries   | boolean      | wheter to use multiple different objects or a single one when dealing with multi-objects (this is mainly related to how the label are used in the map, one label for a multi-polygon or one label for each polygon of a multi-polygon)| false |
| encoding              | string       | internal file encoding | utf-8 |

# Usage

*Note*: 
 * Spatial tables read from sqlite by Mapnik _must_ have a cooresponding entry in `geometry_columns`.
 * Use the `geometry_field` parameter to specify which field to use if you have >1 geometry in the table/query.

## C++

Plugin datasource initialization example code can be found on PluginArchitecture.

A Sqlite datasource may be created as follows:

```cpp
    {
        parameters p;
        p["type"]="sqlite";
        p["file"]=sqlite_spatial_database_file;
        p["table"]="bridges";
        p["geometry_field"]="geom";
        p["extent"]="2309554.99818767,5024797.73763923,2318414.90507308,5040447.94690007";
    
        set_datasource(datasource_cache::instance()->create(p));
    
        // Bridges
        Layer lyr("Bridges");
        lyr.add_style("bridges"); // in style.xml
        m.addLayer(lyr);
    }
```

## Further References
