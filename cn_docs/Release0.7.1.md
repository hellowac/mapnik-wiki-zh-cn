<!-- Name: Release0.7.1 -->
<!-- Version: 1 -->
<!-- Last-Modified: 2010/03/22 13:48:22 -->
<!-- Author: artem -->
## Mapnik 0.7.1 Release

(Packaged from r1745)

- Rasters: Various fixes and improvements to 8bit png output ([#522](https://github.com/mapnik/mapnik/issues/522),[#475](https://github.com/mapnik/mapnik/issues/475))

- XML: Save map buffer_size when serializing map.

- SCons: Added new build options 'PRIORITIZE_LINKING' and 'LINK_PRIORITY'. The first is a boolean (default True)
  of whether to use the new sorting implementation that gives explcit preference to custom or local paths
  during compile and linking that will affect builds when duplicate libraries and include directories are on the
  system. LINK_PRIORITY defaults to prioritizing internal sources of the mapnik source folder, then local/user 
  installed libraries over system libraries, but the option can be customized. Sorting not only ensures that 
  compiling and linking will more likely match the desired libraries but also gives more likelyhood to avoid 
  the scenario where libraries are linked that don't match the includes libmapnik compiled against.

- XML: Fixed behavior of PolygonPatternSymbolizer and LinePatternSymbolizer whereby width, height,
  and type of images is actually allowed to be optionally ommitted ([#508](https://github.com/mapnik/mapnik/issues/508)). This was added in r1543 but
  only worked correctly for PointSymbolizer and ShieldSymbolizer. 

- Fixed reading of PostGIS data on Big Endian systems ([#515](https://github.com/mapnik/mapnik/issues/515))

- PostGIS: Added better support for alterative schemas ([#500](https://github.com/mapnik/mapnik/issues/500))

- AGG Renderer - Enforced default gamma function on all symbolizers to ensure proper antialiasing
  even when gamma is modified on the PolygonSymbolizer. ([#512](https://github.com/mapnik/mapnik/issues/512))

- PNG: fixed png256 for large images and some improvements to reduce color corruptions ([#522](https://github.com/mapnik/mapnik/issues/522))

- PNG: Added new quantization method for indexed png format using hextree with full support for alpha
  channel. Also new method has some optimizations for color gradients common when using elevation based
  rasters. By default old method using octree is used. (r1680, r1683, [#477](https://github.com/mapnik/mapnik/issues/477))

- PNG: Added initial support for passing options to png writter like number of colors, transparency
  support, quantization method and possibly other in future using type parameter. For example
  "png8:c=128:t=1:m=h" limits palette to 128 colors, uses only binary transparency (0 - none,
  1 - binary, 2 - full), and new method of quantization using hextree (h - hextree, o - octree).
  Existing type "png256" can be also written using "png8:c=256:m=o:t=2"  (r1680, r1683, [#477](https://github.com/mapnik/mapnik/issues/477))