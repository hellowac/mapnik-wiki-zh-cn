Random notes on compiler results in terms of runtime speed and library size

## Mapnik [2.1.x branch](https://github.com/mapnik/mapnik/commit/c6fd387469633ee7055aee606abb6f5d3d936a29) with clang++ `3.3 (trunk 177655)` on OS X 10.7
- -Os: libmapnik.dylib is `16.2` MB and tests run in `3.9s`
- -O2: libmapnik.dylib is `12.8` MB and tests run in `3.7s`
