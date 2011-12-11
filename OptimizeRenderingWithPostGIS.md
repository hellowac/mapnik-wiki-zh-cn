<!-- Name: OptimizeRenderingWithPostGIS -->
<!-- Version: 13 -->
<!-- Last-Modified: 2010/11/10 02:52:19 -->
<!-- Author: manelclos -->


# Optimize Rendering with PostGIS

When rendering maps with Mapnik, using a [PostGIS](/wiki:PostGIS/) database as the backend, there is often a large speed gain to be made by employing several optimizations. These optimizations relate to the interaction of PostGIS SQL queries and Mapnik's layers, rules, and filters.

This page will detail some measures you can take to make sure you're not wasting time and memory when rendering a map, or energy maintaining a stylesheet. They are particularly relevant to the rendering of OpenStreetMap data with Mapnik (imported into PostGIS using osm2pgsql), but readers should feel free to edit and extend the instructions with examples from other datasets.

## Keep the SQL resultset as small as possible

### Basics
First, you have to understand how the Datasource table parameter works for each Layer. What happens is that Mapnik takes what you have defined in your `<Parameter name="table>...</Parameter>`, and slaps a `SELECT AsBinary("way"),column,names,needed AS geom ` in front of it, and ending with some SQL to limit results to the BBOX used for the map that's rendering. Mapnik will intelligently limit the columns queried for to what's actually needed in the Styles referenced in the Layer.

Often, when making a new layer and not paying much attention to the Datasource, you may be doing:


    #!xml
    <Parameter name="table">planet_osm_point</Parameter>

This is fine, and will get your data from the database. In fact, it will get *all* data from that table that is within the area that you're rendering. Taking the above explanation, Mapnik expands this to:


    #!sql
    SELECT AsBinary("way") AS geom
    FROM planet_osm_point 
    WHERE "way" && SetSRID('BOX3D(-39135.75848201022 6222585.598639628,665307.8941941741 6927029.251315812)'::box3d,900913)

The SELECT will also add all columns needed to satisfy the styles for this layer. The "WHERE ..." ending will only return rows with an actual geometry (or there'd be nothing to draw for that row anyway) limited to the BBOX given. The coordinates above are just an example.

This type of query is not very efficient. Other than the check for a valid geometry, it will simply fetch each and every row from that table. When the results get to the rules, most of the rows will be filtered out and discarded.


### Limiting the amount of rows to fetch

Let's say you have a style that's only rendering place names for a given layer. You're not rendering anything else in this style, so why would you fetch records from the database for this layer that have nothing to do with place names? Let's limit the query to just what we need:


    #!xml
    <!-- the table parameter for a Layer with just place name styles associated with it -->
    <Parameter name="table">(select * from planet_osm_point where place is not null) as foo</Parameter>

This is an example of a subquery. Mapnik will still put its own SELECT and WHERE "way" etc. around it, and PostGIS will actually see this query:


    #!sql
    SELECT AsBinary("way") AS geom from
    (select * from planet_osm_point where place is not null) as foo
    WHERE "way" && SetSRID('BOX3D(-39135.75848201022 6222585.598639628,665307.8941941741 6927029.251315812)'::box3d,900913)

Let's say you're filtering for some water features, and only want to render rivers, canals, drains, and streams:


    #!sql
    (SELECT * from planet_osm_line where waterway in ('river','canal','drain','stream')) as foo

If you only want to render road tunnels in a style:


    #!sql
    (SELECT * from planet_osm_line where highway is not null and tunnel in ('yes','true','1')) as foo

### Limiting the columns fetched from the database

Doing a `SELECT *` will fetch all columns for the records you want. You can further limit this to only the fields you need in your style.


    #!sql
    (select way,place from planet_osm_point where place is not null) as foo

Notice the `way` column. You always need to include this, or else Mapnik will not get the geometry from the database, and nothing can be drawn.

Assume you're also testing for capital cities. You're not testing for `capital` in the SQL, but you will be testing for that in the Mapnik rules. That means the `capital` field needs to be included in the results, by putting it into the `SELECT`:


    #!sql
    (SELECT way,place,capital from planet_osm_point where place is not null) as foo

You may be building some rules that render elements based on the length of a field, let's say for different sized highway shields:


    #!sql
    (SELECT way,highway,ref,char_length(ref) as length from planet_osm_line where highway is not null and ref is not null) as foo

Notice again that you only need to fetch data from the database that will actually render for this style. Assuming that you're rendering highway shields, it makes no sense to fetch highways without a _ref_.

## Move filtering from Mapnik to PostGIS

Often, a Mapnik style will only render a certain element. You would normally use a filter to only draw something for those elements:


    #!xml
    <Filter>[power] = 'tower'</Filter>

used together with:


    #!sql
    (select * from planet_osm_point) as foo

But this means that you a) select all rows from the database from that table and b) Mapnik then needs to discard most of those rows. Same as in the examples above. If your style only contains a single type of data to render, you can omit the Mapnik filtering altogether and do all filtering in SQL:


    #!sql
    (SELECT way,power from planet_osm_point where power='tower') as foo

You may be rendering only tunnels for roads in a particular style:


    #!sql
    (SELECT way,highway from planet_osm_line where highway is not null and tunnel in ('yes','true','1')) as foo

Then you don't need to include a filter to test for tunnel in the Mapnik rules. Usually this means you can simplify things:


    #!xml
    <Filter>[highway] = 'motorway' and ([tunnel] = 'yes' or [tunnel] = 'true' or [tunnel] = '1')</Filter>
    
    becomes
    
    <Filter>[highway] = 'motorway'</Filter>


## Simplify redundant filter elements

Let's elaborate some more on the last filter example. You may have a style that's testing for `tunnel` but some rules also have to render if an element is *not* a tunnel.

So you'll see a mix of filters in the style:


    #!xml
    <Filter>[highway] = 'motorway' and ([tunnel] = 'yes' or [tunnel] = 'true' or [tunnel] = '1')</Filter>

and another rule with


    #!xml
    <Filter>[highway] = 'motorway' and not ([tunnel] = 'yes' or [tunnel] = 'true' or [tunnel] = '1')</Filter>

Typing all those tunnel tests (actually three tests rolled into one) will get tiresome after a while, and they don't add to the readability of the XML.

SQL to the rescue! Let's have postgresql roll all those choices into 1 simple one to work with in the Mapnik filters:


    #!sql
    (SELECT way,highway,
    case when tunnel in ('yes','true','1') then 'yes'::text
    else tunnel
    end as tunnel
    from planet_osm_line where highway is not null) as foo

The query is split over multiple lines so it's easy to see what's going on. You can also split your own queries into multiple lines in the stylesheet (Mapnik 0.6.0 > | see #173), if it helps you to understand long queries.

Now you can replace the two filters with these:


    #!xml
    <Filter>[highway] = 'motorway' and [tunnel] = 'yes'</Filter>
    
    <Filter>[highway] = 'motorway' and not [tunnel] = 'yes'</Filter>

You could even expand the `case when ... end` to also handle the `no` cases, and increase the readability some more.


    #!sql
    (SELECT way,highway,
    case when tunnel in ('yes','true','1') then 'yes'::text
     else 'no'::text
     end as tunnel
    from planet_osm_line where highway is not null) as foo


    #!xml
    <Filter>[highway] = 'motorway' and [tunnel] = 'yes'</Filter>
    <Filter>[highway] = 'motorway' and [tunnel] = 'no'</Filter>

In these examples, the SQL will get more elaborate, but actual filters will be greatly simplified. Since there is only a single datasource query for a layer, and potentially lots of rules and filters to test these results, it stands to reason to do the hard work in a single location, and leave it to the component that does this the best: PostGIS.

## PostGIS layers

Creating indexes can also help fetching the rows faster. To create a GIST index:


    #!sql
    CREATE INDEX idx_buildings_the_geom ON buildings USING gist(the_geom);

Also, if you are filtering or sorting on a specific field, an index on that field can help too:


    #!sql
    CREATE INDEX idx_buildings_code ON buildings USING btree(code);

## General Postgresql maintenance

Keep your database optimized. You should run this SQL command from time to time:


    #!sql
    vacuum full analyze

If there is any active connection Postgresql will wait until it is closed, so if you are running Ogcserver restart Apache to close the connections.