<!-- Name: Filter -->
<!-- Version: 10 -->
<!-- Last-Modified: 2011/08/29 09:04:20 -->
<!-- Author: MaZderMind -->
# Filter
Each Style-Rule can optionally have a Filter attached. Mapnik walks through all Rules of a Style and checks if it has a Filter specified and if this Filter matches the Object currently rendered. Filters compare an Objects Key-Value Information against the specified rules. When the Datasource is a Postgis Database, the Filter operates on the tables columns, for Shapefiles the Attributes are used.

In XML [character entities](http://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references) are used to construct filters. You can use the following characters to specify value-comparisons:

 * Greater Than: `&gt;`
 * Greater Then or Equal: `&gt;=`
 * Less Than: `&lt;`
 * Less Than or Equal: `&lt;=`
 * Equal: `=`

Filters can be combined with the following operators:

 * A `and` B
 * A `or` B
 * `not` A

And be combined to complex rules using brackets: `(` and `)`.

Missing Attributes are treated as empty strings. Attributes can be compared against [Regular expressions](http://en.wikipedia.org/wiki/Regular_expression) using the `.match` operator.


## Examples in XML
Matches all Objects that have an attribute "amenity" with a value of "restaurant":

```xml
    <Filter>[amenity] = 'restaurant'</Filter> 
```

Matches all Objects that have an attribute "CARTO" with a value that compares greater or equal 2 and lower then 5:

```xml
    <Filter>[CARTO] &gt;= 2 and [CARTO] &lt; 5</Filter>
```

Matches all Objects that have an attribute "waterway" with a value of "canal" a) without a "tunnel" attribute or b) with a "tunnel" attribute that has a value different from "yes" and "true".

```xml
    <Filter>[waterway] = 'canal' and not ([tunnel] = 'yes' or [tunnel] = 'true')</Filter> 
```

Example using an Regular expression, matching all Objects with an attribute "place" with a value of "town" and an attribute "population" with a value consisting of exactly 5 characters where the first one is one of 5, 6, 7 or 8 and the remaining 4 characters are digits.

```xml
    <Filter>[place] = 'town' and [population].match('[5-9]\d\d\d\d')</Filter>
```

## Examples in Python
In python filters can be set using the following syntax:

```python
    f = Filter("[name] = 'value'")
```

## See also
 * The [OpenStreetMap Stylesheet](http://trac.openstreetmap.org/browser/applications/rendering/mapnik/osm.xml?rev=9228) which uses Filters in many ways.
 * The special Filters [ElseFilter](https://github.com/mapnik/mapnik/wiki/ElseFilter) and [AlsoFilter](https://github.com/mapnik/mapnik/wiki/AlsoFilter)
