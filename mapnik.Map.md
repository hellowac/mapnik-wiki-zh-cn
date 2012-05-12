

Below are a list of methods and properties available in mapnik.Map.

* __Map.append_style__ - adds a style to the map
* __Map.aspect_fix_mode__ 
* __Map.background__
* __Map.base__
* __Map.buffer_size__
* __Map.buffered_envelope__
* __Map.envelope__ - gets a bounding box of the map
* __Map.extra_attributes__
* __Map.find_inmem_metawriter__
* __Map.find_style__ - using a style name string (which can be found through
  LaMap.yer.syles), returns a mapnik.Style object
* __Map.get_metawriter_property__
* __Map.has_metawriter__
* __Map.height__
* __Map.layers__ - contains a list of Layer objects
* __Map.maximum_extent__
* __Map.pan__
* __Map.pan_and_zoom__
* __Map.query_map_point__
* __Map.query_point__
* __Map.remove_all__
* __Map.remove_style__
* __Map.resize__
* __Map.scale__
* __Map.scale_denominator__
* __Map.set_metawriter_property__
* __Map.srs__
* __Map.view_transform__
* __Map.width__
* __Map.zoom__
* __Map.zoom_all__
* __Map.zoom_to_box__ - takes an Envelope as an argument and zooms to that
       location

###append_style


append_style( (Map)arg1, (str)style_name, (Style)style_object) -> bool :
    Insert a Mapnik Style onto the map by appending it.
    
    Usage:
    >>> sty
    <mapnik._mapnik.Style object at 0x6a330>
    >>> m.append_style('Style Name', sty)
    True # style object added to map by name
    >>> m.append_style('Style Name', sty)
    False # you can only append styles with unique names
    

    C++ signature :
        bool append_style(mapnik::Map {lvalue},std::string,mapnik::feature_type_style)

###aspect_fix_mode

None

###background

None

###base

str(object) -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.

###buffer_size

int(x[, base]) -> integer

Convert a string or number to an integer, if possible.  A floating point
argument will be truncated towards zero (this does not include a string
representation of a floating point number!)  When converting a string, use
the optional base.  It is an error to supply a base when converting a
non-string.  If base is zero, the proper base is guessed based on the
string content.  If the argument is outside the integer range a
long object will be returned instead.

###buffered_envelope


buffered_envelope( (Map)arg1) -> Box2d :
    Get the Box2d() of the Map given
    the Map.buffer_size.
    
    Usage:
    >>> m = Map(600,400)
    >>> m.envelope()
    Box2d(-1.0,-1.0,0.0,0.0)
    >>> m.buffered_envelope()
    Box2d(-1.0,-1.0,0.0,0.0)
    >>> m.buffer_size = 1
    >>> m.buffered_envelope()
    Box2d(-1.02222222222,-1.02222222222,0.0222222222222,0.0222222222222)
    

    C++ signature :
        mapnik::box2d<double> buffered_envelope(mapnik::Map {lvalue})

###envelope


envelope( (Map)arg1) -> Box2d :
    Return the Map Box2d object
    and print the string representation
    of the current extent of the map.
    
    Usage:
    >>> m.envelope()
    Box2d(-0.185833333333,-0.96,0.189166666667,-0.71)
    >>> dir(m.envelope())
    ...'center', 'contains', 'expand_to_include', 'forward',
    ...'height', 'intersect', 'intersects', 'inverse', 'maxx',
    ...'maxy', 'minx', 'miny', 'width'
    

    C++ signature :
        mapnik::box2d<double> envelope(mapnik::Map {lvalue})

###extra_attributes


extra_attributes( (Map)arg1) -> Parameters :
    TODO

    C++ signature :
        mapnik::parameters extra_attributes(mapnik::Map {lvalue})

###find_inmem_metawriter


find_inmem_metawriter( (Map)arg1, (str)name) -> MetaWriterInMem :
    Gets an inmem metawriter, or None if no such metawriter exists.
    Use this after the map has been rendered to retrieve information about the hit areas rendered on the map.
    

    C++ signature :
        boost::shared_ptr<mapnik::metawriter_inmem> find_inmem_metawriter(mapnik::Map,std::string)

###find_style


find_style( (Map)arg1, (str)style_name) -> Style :
    Query the Map for a style by name and return
    a style object if found or raise KeyError
    style if not found.
    
    Usage:
    >>> m.find_style('Style Name')
    <mapnik._mapnik.Style object at 0x654f0>
    

    C++ signature :
        mapnik::feature_type_style find_style(mapnik::Map,std::string)

###get_metawriter_property


get_metawriter_property( (Map)arg1, (str)name) -> str :
    Reads a metawriter property.
    These properties are completely user-defined and can be used tocreate filenames, etc.
    
    Usage:
    >>> map.set_metawriter_property("x", "10")
    >>> map.get_metawriter_property("x")
    10
    

    C++ signature :
        std::string get_metawriter_property(mapnik::Map {lvalue},std::string)

###has_metawriter


has_metawriter( (Map)arg1) -> bool :
    Check if the Map has any active metawriters
    
    Usage:
    >>> m.has_metawriter()
    False
    

    C++ signature :
        bool has_metawriter(mapnik::Map)

###height

int(x[, base]) -> integer

Convert a string or number to an integer, if possible.  A floating point
argument will be truncated towards zero (this does not include a string
representation of a floating point number!)  When converting a string, use
the optional base.  It is an error to supply a base when converting a
non-string.  If base is zero, the proper base is guessed based on the
string content.  If the argument is outside the integer range a
long object will be returned instead.

###layers

None

###maximum_extent


###pan


pan( (Map)arg1, (int)x, (int)y) -> None :
    Set the Map center at a given x,y location
    as integers in the coordinates of the pixmap or map surface.
    
    Usage:
    >>> m = Map(600,400)
    >>> m.envelope().center()
    Coord(-0.5,-0.5) # default Map center
    >>> m.pan(-1,-1)
    >>> m.envelope().center()
    Coord(0.00166666666667,-0.835)
    

    C++ signature :
        void pan(mapnik::Map {lvalue},int,int)

###pan_and_zoom


pan_and_zoom( (Map)arg1, (int)x, (int)y, (float)factor) -> None :
    Set the Map center at a given x,y location
    and zoom factor as a float.
    
    Usage:
    >>> m = Map(600,400)
    >>> m.envelope().center()
    Coord(-0.5,-0.5) # default Map center
    >>> m.scale()
    -0.0016666666666666668
    >>> m.pan_and_zoom(-1,-1,0.25)
    >>> m.scale()
    0.00062500000000000001
    

    C++ signature :
        void pan_and_zoom(mapnik::Map {lvalue},int,int,double)

###query_map_point


query_map_point( (Map)arg1, (int)layer_idx, (float)pixel_x, (float)pixel_y) -> Featureset :
    Query a Map Layer (by layer index) for features 
    intersecting the given x,y location in the pixel
    coordinates of the rendered map image.
    Layer index starts at 0 (first layer in map).
    Will return a Mapnik Featureset if successful
    otherwise will return None.
    
    Usage:
    >>> featureset = m.query_map_point(0,200,200)
    >>> featureset
    <mapnik._mapnik.Featureset object at 0x23b0b0>
    >>> featureset.features
    >>> [<mapnik.Feature object at 0x3995630>]
    

    C++ signature :
        boost::shared_ptr<mapnik::Featureset> query_map_point(mapnik::Map,int,double,double)

###query_point


query_point( (Map)arg1, (int)layer idx, (float)x, (float)y) -> Featureset :
    Query a Map Layer (by layer index) for features 
    intersecting the given x,y location in the coordinates
    of map projection.
    Layer index starts at 0 (first layer in map).
    Will return a Mapnik Featureset if successful
    otherwise will return None.
    
    Usage:
    >>> featureset = m.query_point(0,-122,48)
    >>> featureset
    <mapnik._mapnik.Featureset object at 0x23b0b0>
    >>> featureset.features
    >>> [<mapnik.Feature object at 0x3995630>]
    

    C++ signature :
        boost::shared_ptr<mapnik::Featureset> query_point(mapnik::Map,int,double,double)

###remove_all


remove_all( (Map)arg1) -> None :
    Remove all Mapnik Styles and layers from the Map.
    
    Usage:
    >>> m.remove_all()
    

    C++ signature :
        void remove_all(mapnik::Map {lvalue})

###remove_style


remove_style( (Map)arg1, (str)style_name) -> None :
    Remove a Mapnik Style from the map.
    
    Usage:
    >>> m.remove_style('Style Name')
    

    C++ signature :
        void remove_style(mapnik::Map {lvalue},std::string)

###resize


resize( (Map)arg1, (int)width, (int)height) -> None :
    Resize a Mapnik Map.
    
    Usage:
    >>> m.resize(64,64)
    

    C++ signature :
        void resize(mapnik::Map {lvalue},unsigned int,unsigned int)

###scale


scale( (Map)arg1) -> float :
    Return the Map Scale.
    Usage:
    
    >>> m.scale()
    

    C++ signature :
        double scale(mapnik::Map {lvalue})

###scale_denominator


scale_denominator( (Map)arg1) -> float :
    Return the Map Scale Denominator.
    Usage:
    
    >>> m.scale_denominator()
    

    C++ signature :
        double scale_denominator(mapnik::Map {lvalue})

###set_metawriter_property


set_metawriter_property( (Map)arg1, (str)name, (str)value) -> None :
    Sets a metawriter property.
    These properties are completely user-defined and can be used tocreate filenames, etc.
    
    Usage:
    >>> map.set_metawriter_property("x", str(x))
    >>> map.set_metawriter_property("y", str(y))
    >>> map.set_metawriter_property("z", str(z))
    
    Use a path like "[z]/[x]/[y].json" to create filenames.
    

    C++ signature :
        void set_metawriter_property(mapnik::Map {lvalue},std::string,std::string)

###srs

str(object) -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.

###view_transform


view_transform( (Map)arg1) -> ViewTransform :
    Return the map ViewTransform object
    which is used internally to convert between
    geographic coordinates and screen coordinates.
    
    Usage:
    >>> m.view_transform()
    

    C++ signature :
        mapnik::CoordTransform view_transform(mapnik::Map {lvalue})

###width

###zoom


zoom( (Map)arg1, (float)factor) -> None :
    Zoom in or out by a given factor.
    Positive number zooms in, negative number
    zooms out.
    
    Usage:
    
    >>> m.zoom(0.25)
    

    C++ signature :
        void zoom(mapnik::Map {lvalue},double)

###zoom_all


zoom_all( (Map)arg1) -> None :
    Set the geographical extent of the map
    to the combined extents of all active layers.
    
    Usage:
    >>> m.zoom_all()
    

    C++ signature :
        void zoom_all(mapnik::Map {lvalue})

###zoom_to_box


zoom_to_box( (Map)arg1, (Box2d)Boxd2) -> None :
    Set the geographical extent of the map
    by specifying a Mapnik Box2d.
    
    Usage:
    >>> extext = Box2d(-180.0, -90.0, 180.0, 90.0)
    >>> m.zoom_to_box(extent)
    

    C++ signature :
        void zoom_to_box(mapnik::Map {lvalue},mapnik::box2d<double>)
