# Mapnik Datasource

<class 'mapnik.Datasource'>

### all_features

None

### bind

bind( (Datasource)arg1) -> None :

    C++ signature :
        void bind(mapnik::datasource {lvalue})

### describe

None

### descriptor

descriptor( (Datasource)arg1) -> object :

    C++ signature :
        mapnik::layer_descriptor descriptor(mapnik::datasource {lvalue})

### encoding

encoding( (Datasource)arg1) -> str :

    C++ signature :
        std::string encoding(boost::shared_ptr<mapnik::datasource>)

### envelope

envelope( (Datasource)arg1) -> Box2d :

    C++ signature :
        mapnik::box2d<double> envelope(mapnik::datasource {lvalue})

### features

features( (Datasource)arg1, (Query)arg2) -> Featureset :

    C++ signature :
        boost::shared_ptr<mapnik::Featureset> features(mapnik::datasource {lvalue},mapnik::query)

### features_at_point

features_at_point( (Datasource)arg1, (Coord)arg2) -> Featureset :

    C++ signature :
        boost::shared_ptr<mapnik::Featureset> features_at_point(mapnik::datasource {lvalue},mapnik::coord<double, 2>)

### featureset

None

### field_types

field_types( (Datasource)arg1) -> list :

    C++ signature :
        boost::python::list field_types(boost::shared_ptr<mapnik::datasource>)

### fields

fields( (Datasource)arg1) -> list :

    C++ signature :
        boost::python::list fields(boost::shared_ptr<mapnik::datasource>)

### name

name( (Datasource)arg1) -> str :

    C++ signature :
        std::string name(boost::shared_ptr<mapnik::datasource>)

### params

params( (Datasource)arg1) -> Parameters :
    The configuration parameters of the data source. These vary depending on the type of data source.

    C++ signature :
        mapnik::parameters params(mapnik::datasource {lvalue})
