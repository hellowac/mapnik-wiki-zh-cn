<!-- Name: MemoryDatasource -->
<!-- Version: 2 -->
<!-- Last-Modified: 2011/09/01 13:38:53 -->
<!-- Author: Ollie -->
# MemoryDatasource

*New in 0.8 (aka mapnik2)*

A in-memory datasource. Sample usage:


    #!python
    
    from mapnik2 import Feature, MemoryDatasource, Geometry2d
    ds = MemoryDatasource()
    ds.add_feature(Feature(1, Geometry2d.from_wkt("POINT(2 5)"), name="Alberto"))