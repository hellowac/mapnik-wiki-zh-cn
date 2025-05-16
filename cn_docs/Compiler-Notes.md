# Compiler Notes

Random notes on compiler results in terms of runtime speed and library size

## Mapnik [2.1.x branch](https://github.com/mapnik/mapnik/commit/c6fd387469633ee7055aee606abb6f5d3d936a29) with clang++ `3.3 (trunk 177655)` on OS X 10.7

- -Os: libmapnik.dylib is `16.2` MB and tests run in `3.9s`
- -O2: libmapnik.dylib is `12.8` MB and tests run in `3.7s`
- -O3: libmapnik.dylib is `12.5` MB and tests run in `3.7s`

## Mapnik 3.x

OS X duel core: `2.8 GHz Intel Core i7`

At <https://github.com/mapnik/mapnik/commit/66ad95cbbe755c9e905406b6f1227b06b24f60e1>

```bash
$ clang++ -v
Apple LLVM version 6.1.0 (clang-602.0.49) (based on LLVM 3.6.0svn)
Target: x86_64-apple-darwin14.3.0
Thread model: posix
```

```bash
$ source bootstrap.sh && time make
real 16m31.347s
user 29m1.430s
sys 1m7.557s
```

rebuilding with ccache `v3.2.1` (first run):

```bash
$ ./configure CXX="/Users/dane/.homebrew/bin/ccache clang++"
$ time make
real 11m3.394s
user 28m36.684s
sys 1m36.502s
```

Second run:

```bash
make clean
time make
real 0m41.734s
user 0m41.007s
sys 0m15.724s
```
