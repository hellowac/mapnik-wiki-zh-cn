<!-- Name: PostGIS -->
<!-- Version: 18 -->
<!-- Last-Modified: 2011/08/23 13:51:30 -->
<!-- Author: springmeyer -->

Mapnik's PluginArchitecture supports the use of different input formats.

One such plugin supports the [PostGIS](http://en.wikipedia.org/wiki/PostGIS) extension to the popular PostgreSQL database.

See also a performance tuning page: [[OptimizeRenderingWithPostGIS]]

## New 0.7.0 Features

Docs TODO ->

 * Dynamic map variables
  * !bbox!
  * !scale_denominator!
 * subquery best practices -  when to set the 'subquery_extent' to true
 * controlling connection persistence   

## Installation

For Ubuntu, see [[UbuntuInstallation]] (specifically the package install line that includes _postgresql-8.3_)

On Macs, try the instructions listed on [[MacInstallation_Optional]].

Either way, make sure that running _python scons/scons.py DEBUG=y_ shows the following line

    Checking for C library pq... yes

pq, or rather libpq, is the "C application programmer's interface to PostgreSQL". Without this library, Mapnik will not know how to talk to PostGIS / PostgreSQL, and the PostGIS plugin will neither build nor be installed.

To check if the PostGIS plugin built and was installed correctly, try the usual Python _from mapnik import *_ on a DEBUG=y build, and look for the following debug line

    registered datasource : postgis

## Parameters

| *parameter*       | *value*  | *description* | *default* |
|:------------------|----------|---------------|----------:|
| host                  | string       | name of the postgres host | |
| port                  | integer      | name of the postgres port | |
| dbname                | string       | name of the database | |
| user                  | string       | username to use for connecting | |
| password              | string       | user password to use for connecting | |
| table                 | string       | name of the table to fetch, this can be a sub-query;  subquery has to use syntax of:  '( ) as table'. | |
| geometry_field        | string       | name of the geometry field, in case you have more than one in a single table. This field and the SRID will be deduced from the query in most cases, but may need to be manually specified in some cases.| |
| geometry_table        | string       | name of the geometry table ??? | |
| srid                  | integer      | srid of the table, if this is > 0 then fetching data will avoid an extra database query for knowing the srid of the table | 0 |
| extent                | string       | maxextent of the geometries | determined by querying the oracle metadata for the table |
| extent_from_subquery  | boolean      | evaluate the extent of the subquery, this might be a performance issue | false |
| connect_timeout       | integer      | timeout is seconds for the connection to take place | 4 |
| persist_connection    | boolean      | choose wheter to share the same connection for subsequent queries | true |
| row_limit             | integer      | max number of rows to return when querying data, 0 means no limit | 0 |
| cursor_size           | integer      | if this is > 0 then server cursor will be used, and will prefetch this number of features | 0 |
| initial_size          | integer      | initial size of the stateless connection pool | 1 |
| max_size              | integer      | max size of the stateless connection pool | 10 |
| multiple_geometries   | boolean      | wheter to use multiple different objects or a single one when dealing with multi-objects (this is mainly related to how the label are used in the map, one label for a multi-polygon or one label for each polygon of a multi-polygon)| false |
| encoding              | string       | internal file encoding | utf-8 |

## Usage

*Note*: 

 * Spatial tables read from PostGIS by Mapnik _must_ have a cooresponding entry in `geometry_columns`.
 * Use the `geometry_field` parameter to specify which field to use if you have >1 geometry in the table/query (added in r769).

### Python

Instantiate a datasource like:

```python
    lyr = Layer('Geometry from PostGIS')
    lyr.datasource = PostGIS(host='localhost',user='postgres',password='',dbname='your_postgis_database',table='your_table')
```

If you want to do complex queries you can nest subselects in the `table` argument:

```python
    lyr = Layer('Buffered Geometry from PostGIS')
    BUFFERED_TABLE = '(select ST_Buffer(geometry, 5) as geometry from %s) polygon' % ('your_postgis_table')
    lyr.datasource = PostGIS(host='localhost',user='postgres',password='',dbname='your_postgis_database',table=BUFFERED_TABLE)

If you want to add something after the query (for example ORDER BY) you must use !bbox! dynamic map variable:

    lyr = Layer('Order by st_lenght from PostGIS')
    BUFFERED_TABLE = 'table_line where way && !bbox! ORDER BY st_LENGTH(way) DESC'
    lyr.datasource = PostGIS(host='localhost',user='postgres',password='',dbname='your_postgis_database',table=BUFFERED_TABLE, srid='your_srid', geometry_field='way', extent='your_extent')
```

 * *Note*: because mapnik depends on the `geometry_columns` entry be careful not to use sub-selects that change the geometry type.
 * Further references: See Artem's email on [using the PostGIS from Python](https://lists.berlios.de/pipermail/mapnik-users/2007-June/000300.html)
 * Example code at the Mapnik-utils project: http://mapnik-utils.googlecode.com/svn/example_code/postgis/postgis_geometry.py

### XML

If you are using XML mapfiles to style your data, then using a PostGIS datasource (with a sub-select in this case) looks like:

 * *Note*: if you use a sub-select that changes the extents of your features, make sure to use `estimate_extent=false` otherwise Mapnik will return no features. Otherwise you don't need to use the `estimate_extent` or `extent` parameters at all.

```xml
    <Layer name="countries" status="on" srs="+proj=latlong +datum=WGS84">
        <StyleName>countries_style_label</StyleName>
        <Datasource>
          <Parameter name="type">postgis</Parameter>
          <Parameter name="host">localhost</Parameter>
          <Parameter name="dbname">geodjango_geographic_admin</Parameter>
          <Parameter name="user">postgres</Parameter>      
          <Parameter name="password"></Parameter>
          <Parameter name="table">(select ST_Buffer(ST_Centroid(geometry),2) as geometry, name  from world_worldborders) as world</Parameter>
          <Parameter name="estimate_extent">false</Parameter>
          <Parameter name="extent">-180,-90,180,89.99</Parameter>
        </Datasource>
    </Layer>
```

*Note*: If you use a custom projection, you might need to change the extent parameters to the area for which the projection is defined. For example, the Dutch grid (EPSG:28992) is only defined around the Netherlands. It does not make sense to try to project South America onto it. You need to change the extent parameter to something like this:

```xml
    <Parameter name="extent">3.09582088671,50.6680811311,7.41350097346,53.6310799196</Parameter>
```

If you don't do this, you might not see data from this data source at all, even if it does not contain data outside of the valid region. Also note that you always specify the extents in the coordinates of the source system.

### C++

Plugin datasource initialization example code can be found on [[PluginArchitecture]].

A PostGIS datasource may be created as follows:

```cpp
    {
        parameters p;
        p["type"]="postgis";
        p["host"]=database_hostname;
        p["port"]=5432;
        p["dbname"]="gis";
        p["user"]=your_username;
        p["password"]="";
    
        Layer lyr("Roads");
        set_datasource(datasource_cache::instance()->create(p));
        lyr.add_style("roads");
        m.addLayer(lyr);
    }
```

For other PostGIS parameters, see [the postgis_datasource constructor in postgis_datasource.cpp#L48](https://github.com/mapnik/mapnik/blob/master/plugins/input/postgis/postgis_datasource.cpp#L48)

TODO -- more PostGIS query usage

## Further References
 [Using Mapnik and PostGIS with OSM](http://wiki.openstreetmap.org/index.php/Mapnik/PostGIS)