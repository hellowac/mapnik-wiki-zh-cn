# Installing Mapnik on OS X with Homebrew

## Install Homebrew

First, make sure you have homebrew [installed](http://github.com/mxcl/homebrew/wiki/installation)

Then make sure homebrew is updated:

```sh
brew update
```

## Install Options

Now you can either 1) install Mapnik itself with homebrew (which will automatically install all dependencies at the same time) or 2) install all Mapnik dependencies via homebrew and then Mapnik from source.

### To install the latest Mapnik release do:

```sh
brew install mapnik
```

### To install Mapnik from source using homebrew for dependencies do:

```sh
brew install cairo --without-x --without-glib
brew install icu4c
brew link icu4c
brew install boost
brew install proj
brew install jpeg
brew link jpeg
brew install libtiff
brew install gdal --with-libtiff=/usr/local/lib
brew link ossp-uuid
brew install postgis
git clone https://github.com/mapnik/mapnik.git
cd mapnik
./configure
make
make install
```

Note that on Lion, you need may to be more explicit about SQLite.  Change version as needed.

```
 ./configure CXX="clang++" JOBS=`sysctl -n hw.ncpu` SQLITE_LIBS=/usr/local/Cellar/sqlite/3.7.12/lib/ SQLITE_INCLUDES=/usr/local/Cellar/sqlite/3.7.12/include/
```

## Boost-Python Link Problems

After you install mapnik, you may try to import it and get `Fatal Python error: Interpreter not initialized (version mismatch?)`. If so, you likely have boost linked with the wrong version of python. To see what version of python boost is linked from, try:

```sh
otool -L `brew list boost | grep python-mt.dylib` | grep -i python
```

It's likely that your copy of boost was linked against the system python, but you're trying to use a homebrew python. To fix, uninstall boost, and reinstall with --build-from-source:

```sh
brew uninstall boost
brew install --build-from-source boost
```

## Building with Cairo

If you need Cairo and its Python bindings, install and link these (cairo and py2cairo) with homebrew as normal. Then, to build Mapnik from source with Cairo:

```
./configure CXX="clang++" JOBS=`sysctl -n hw.ncpu` CAIRO=True PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/local/lib/pkgconfig:/usr/X11/lib/pkgconfig
```