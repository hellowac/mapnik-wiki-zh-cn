<!-- Name: MemoryDatasource -->
<!-- Version: 2 -->
<!-- Last-Modified: 2011/09/01 13:38:53 -->
<!-- Author: Ollie -->
# MemoryDatasource

*New in 0.8 (aka mapnik2)*

A in-memory datasource. Sample usage:

```python    
    import mapnik
    ds = mapnik.MemoryDatasource()
    f = mapnik.Feature(mapnik.Context(), 1)
    f.add_geometries_from_wkt("POINT(2 5)")
    ds.add_feature(f)
```