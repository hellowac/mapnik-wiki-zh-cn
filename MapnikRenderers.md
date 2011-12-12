# Mapnik Renderers

Mapnik supports a variety of rendering backends. See OutputFormats for comparisons of different output formats.

## agg_renderer | Anti-Grain Geometry

The AGG renderer ([Antigrain Geometry](http://antigrain.com)) is the primary renderer in Mapnik.

* AGG 's fast scanline rendering with subpixel *anti-aliasing* is the standout reason for the beauty of Mapnik output.
 * [Anti-Aliasing](http://en.wikipedia.org/wiki/Antialiasing) and [Subpixel Rendering](http://en.wikipedia.org/wiki/Subpixel_rendering) on Wikipedia 
* The AGG renderer's buffer can easily be encoded in a variety of formats. Currently Mapnik supports writing to png and jpeg.
* Version 2.3 of the AGG C++ library is included/embedded within the source tree of Mapnik and compiled automatically during the Scons process.
* Because the primary developer of AGG has moved on to other endeavors, we happily maintain our own version of AGG with bugfixes.
* Mapnik can also build against a system version of AGG, but this is NOT RECOMMENDED since packaged versions have likely not been updated with critical bug fixes
    
While Mapnik was the first to use AGG rendering for mapping, the AGG renderer is also now an optional rendering engine in the [MapServer](http://mapserver.gis.umn.edu/docs/howto/agg-rendering-specifics) and [MapGuide](http://trac.osgeo.org/mapguide/wiki/MapGuideRfc40) projects.
    
    
## cairo_renderer | Cairographics
  
The [Cairo](http://cairographics.org/) renderer is an auxiliary renderer in Mapnik.

* Cairo was added in r656 due to its similar reputation for high quality graphics output to various formats
 * http://trac.mapnik.org/log/trunk/src/cairo_renderer.cpp
* Cairo has the '''added advantage''' of supporting both Vector and Raster output.
* Mapnik can render to any [surface](http://www.cairographics.org/manual/cairo-surfaces.html) supported by cairo, either directly or by rendering to a cairo [context](http://www.cairographics.org/manual/cairo-context.html).
 * You can demo the PNG, JPEG, SVG, PDF, and PS formats using the [OSM export tool](http://openstreetmap.org/export/)
* Cairo is optional during Mapnik Scons build process but is enabled automatically if found (using pkg-config).
 * Pkg-config must find libcairo as well as Cairomm(C++ bindings) and Pycairo (python bindings)
 * If Pkg-config is successful you will see the added compiler flags: `-DHAVE_CAIRO -DHAVE_PYCAIRO`


### Python Example Code

Writing to SVG with Mapnik's Cairo renderer:

```python
    import mapnik
    import cairo
    
    mapfile = 'mapfile.xml'
    projection = '+proj=latlong +datum=WGS84'
    
    mapnik_map = mapnik.Map(1000, 500)
    mapnik.load_map(mapnik_map, mapfile)
    bbox = mapnik.Envelope(-180.0,-90.0,180.0,90.0)
    mapnik_map.zoom_to_box(bbox)
    
    # Write to SVG
    surface = cairo.SVGSurface('mapfile.svg', mapnik_map.width, mapnik_map.height)
    mapnik.render(mapnik_map, surface)
    surface.finish()
    
    # Or write to PDF
    surface = cairo.PDFSurface('mapfile.pdf', mapnik_map.width, mapnik_map.height)
    mapnik.render(mapnik_map, surface)
    surface.finish()
```

 * Note: Cairo can also write to PostScript and other image formats
 * Note: 'mapnik.render()' can also render to Cairo Contexts


## svg_renderer

The SVG renderer is written by Carlos López Garcés, started as part of GSOC 2010 and the "better printing project". The idea is that while the Cairo backend offers both PDF and SVG support, we can do better by having a custom implementation to handle things such as layer grouping, re-used of svg/bitmap symbols, and texts on paths. Only the basics are implemented at this point and those needed custom features are still a ways off, but the renderer has much promise. Currently is is not built by default but can be enabled with the build flag `SVG_RENDERER=True`.

The svg_renderer uses some very cool features of boost karma to generate SVG really fast and should be a good example of ways to leverage boost karma more in the future, potentially for other types of innovative vector output.

## grid_renderer

The Grid renderer is designed to output highly optimized feature "hit grids". It does this by leveraging and extending modular parts of the antigrain geometry library to rasterize feature id's into a buffer, then outputs metadata about the relevant feature attributes for the given ids, all enclosed within a compact, highly compressible json file. The grid_renderer will first be available in the Mapnik 2.0 release and landed in trunk in r2840.

There is a sample application showing how to use the output at https://github.com/springmeyer/gridsforkids#readme.

The grid renderer output targets >= 1.1 of the mbtiles interaction spec found at https://github.com/mapbox/mbtiles-spec/. Specifically it targets "grid.json" a  [UTF8 Grid format](https://github.com/mapbox/mbtiles-spec/blob/master/1.1/utfgrid.md) which is then handled by client javascript code as detailed in the [Interaction spec](https://github.com/mapbox/mbtiles-spec/blob/master/1.1/interaction.md).

The client javascript library that works with all major javascript mapping APIs and has the logic to interface with the json grids is called WAX and is located at https://github.com/mapbox/wax. Specifically the control for parsing the grid.json is in https://github.com/mapbox/wax/blob/master/control/lib/gridutil.js and depends on a metadata file called layer.json to instruct about how the feature data should be formatted in the browser.

It should be noted that while the mbtiles spec also talks about leveraging sqlite as a tile cache the interaction and grid.json should work absolutely fine with any caching format on the filesystem. However, at this time the WAX client javascript code (for legacy reasons) assumes that the tile scheme is [TMS](http://wiki.osgeo.org/wiki/Tile_Map_Service_Specification), which is basically the same as the OSM/Google scheme except that the [Y axis is flipped](http://lists.osgeo.org/pipermail/tiling/2010-September/000015.html) (or the origin is [lower left](http://wiki.osgeo.org/wiki/File:Tms.png) not top left). Luckily it is pretty easy to "flip" the y with code like:

```python
y = (2**z-1) - y
```


## Further References

 * [OSGEO Discussion of Rendering](http://wiki.osgeo.org/wiki/OSGeo_Cartographic_Library)
 * [GRASS GIS use of Cairo](http://trac.osgeo.org/grass/browser/grass/trunk/lib/cairodriver)
 * [Cairo Vs. AGG Comparison](http://goodythoughts.blogspot.com/2008/03/why-cairo-vs-agg.html)
 * [Blog post on Skia (Chrome Renderer) in context of AGG and Cairo](http://www.gnashdev.org/?q=node/57)
 * [Agg inclusion in Boost thread - see 'A preliminary proposal: AGG project'](http://lists.boost.org/Archives/boost/2002/05/index.php)
 * [Good intro into anti-aliased font issues](http://www.joelonsoftware.com/items/2007/06/12.html)
