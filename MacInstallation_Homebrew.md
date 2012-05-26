# Installing Mapnik on OS X with Homebrew

## Install Homebrew

First, make sure you have homebrew [installed](http://github.com/mxcl/homebrew/wiki/installation)

## Install Options

Now you can either 1) install Mapnik itself with homebrew (which will automatically install all dependencies at the same time) or 2) install all Mapnik dependencies via homebrew and then Mapnik from source.

### To install the latest Mapnik release do:

```sh
brew install mapnik
```

On 10.6.8, you may need to:

```sh
brew link pkg-config
brew install xz libffi
brew link libtiff
brew link jpeg
brew link proj
brew link boost
brew install mapnik
```

### To install Mapnik from source using homebrew for dependencies do:

```sh
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
brew install cairo
git clone https://github.com/mapnik/mapnik.git
cd mapnik
./configure CXX="clang++" JOBS=`sysctl -n hw.ncpu`
make
make install  # sudo make install # Mac OS X Lion. With system default python 2.7 
```

Note that on Lion, we need to be more explicit about SQLite.  Change version as needed.

```
 ./configure CXX="clang++" JOBS=`sysctl -n hw.ncpu` SQLITE_LIBS=/usr/local/Cellar/sqlite/3.7.12/lib/ SQLITE_INCLUDES=/usr/local/Cellar/sqlite/3.7.12/include/
```