Log of benchmarking runs using the `benchmark/run.cpp` tool available in Mapnik >= 2.2.x

## OS X 10.8, libstdc++, April 18, 2013, Lots of Chrome tabs open :)

```sh
$ mapnik-config --git-describe
v2.1.0-1076-g60c6592
$ clang++ -v
Apple LLVM version 4.2 (clang-425.0.27) (based on LLVM 3.2svn)
Target: x86_64-apple-darwin12.3.0
Thread model: posix
```

```sh
1) encoding blank image as png: 170 milliseconds
2) encoding multicolor image as png8:m=h: 13660 milliseconds
3) threaded -> encoding blank image as png: 50 milliseconds
4) threaded -> encoding multicolor image as png8:m=h: 4960 milliseconds
5) double to string conversion with std::ostringstream: 1060 milliseconds
6) double to string conversion with mapnik::util_to_string: 270 milliseconds
7) double to string conversion with snprintf: 260 milliseconds
8) threaded -> double to string conversion with std::ostringstream: 124930 milliseconds
9) threaded -> double to string conversion with mapnik::util_to_string: 800 milliseconds
10) threaded -> double to string conversion with snprintf: 820 milliseconds
11) threaded -> lonlat -> merc coord transformation (epsg): 2110 milliseconds
12) threaded -> merc -> lonlat coord transformation (epsg): 2120 milliseconds
13) threaded -> lonlat -> merc coord transformation (literal): 3900 milliseconds
14) threaded -> merc -> lonlat coord transformation (literal): 3900 milliseconds
15) threaded -> expression parsing with grammer per parse: 8680 milliseconds
16) threaded -> expression parsing by re-using grammar: 1760 milliseconds
17) threaded -> rule caching using boost::move: 570 milliseconds
18) threaded -> rule caching using heap allocation: 460 milliseconds
19) threaded -> clipping polygon with agg_conv_clipper: 3320 milliseconds
20) threaded -> clipping polygon with mapnik::polygon_clipper: 5090 milliseconds
21) threaded -> font_engihe: created 220000 faces in : 3280 milliseconds
```