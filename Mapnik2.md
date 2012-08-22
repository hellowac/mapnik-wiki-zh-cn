# Mapnik2

Mapnik2 is the name for the Mapnik (2.0.0) and 2.x series. In this major release we jumped from 0.7.x to 2.x.

To get Mapnik 2.x either:

1) Download the latest master from github `git clone https://github.com/mapnik/mapnik.git`

2) Download the latest 2.x series release from https://github.com/mapnik/mapnik/downloads.

3) Or, read about installing for specific platforms: https://github.com/mapnik/mapnik/wiki/Mapnik-Installation

Mapnik2 was over a year in development before formal release for two reasons:

   * Mapnik2 requires at least Boost 1.42, and we waited for major linux distributions to start packaging at least that boost version
   * Mapnik2 simplifies a few elements of the XML syntax in backward incompatible ways.

## Naming conventions

While Mapnik2 was in development (and for the 2.0.0 release) we implemented a naming change for ease of development and testing.

But this is now rolled back, following the first release of 2.0.0. So the basics are:

| *version* | *library* | *python module* |
------------|-----------|-----------------|
| 0.7.x     | libmapnik | mapnik |
| 2.0.0     | libmapnik2 | mapnik2 |
| >= 2.1 (current master) | libmapnik | mapnik (mapnik2 works but issues warning) |

To get the library name for your install of Mapnik2 do:

    $ mapnik-config --libs
    -L/usr/local/lib -lmapnik

Specifically in python with Mapnik 2.0.0 and 2.1 you can do:

```python
    >>> import mapnik2 # . This made it easier for developers to run the Mapnik 0.7.x series alongside Mapnik2.
```

But, the current development code (and the upcoming Mapnik 2.1.0 release) has now moved back to using:

```python
    >>> import mapnik #import mapnik2 will still work but will issue a deprecation warning
```

## Compatibility

The Mapnik2 API has advanced (requiring breakages) and the XML syntax has changed in specific cases.

Therefore Mapnik2 is the [first release](MapnikReleases) with significant backward incompatibility. See [[Mapnik2_Changes]]

# Upgrade Guide
1. Recommended: rebuild shapefile indexes

Say you have a directory of shapefiles in a folder named 'shapes'. Then you can regenerate all the indexes at once like:

```
shapeindex shapes/*.shp
```

2. Required: upgrade stylesheets

We have written a python converter to automatically upgrade your pre-Mapnik2 stylesheets to be fully compatible with Mapnik2.

After installing Mapnik2 you will have a new command available called 'upgrade_map_xml.py':

```
    $ upgrade_map_xml.py
        Usage: upgrade_map_xml.py <input_file> <output_file>
```

For osm.xml users, you will note that this script does not preserve entities. The best approach (until osm.xml is upgraded to require at least mapnik 2.x) is to continue editing the osm.xml and just convert it each time you wish to render with Mapnik2.

Also, we have ported support for the new Mapnik2 syntax to the 0.7.2 release, so with 0.7.2 you can stay on the stable 0.7 series but keep your stylesheets in the cleaner Mapnik2 format.

### Cascadenik

There is a branch of Cascadenik that is adding Mapnik2 compatibility at https://github.com/mapnik/Cascadenik/tree/mapnik2

### nik2img

Nik2img as of 0.5.0 supports both mapnik and mapnik2 transparently. Pass --mapnik-version 1 or mapnik-version 2 to force the usage of a single one (it will default to using Mapnik2) 

### mod_tile/renderd

Supports Mapnik2 as of [r22900](http://trac.openstreetmap.org/changeset/22900).

Please note, as per the above naming changes, if using Mapnik 2.0.0 the library name is `libmapnik2`, but all previous and future releases simply use `libmapnik` as the library name. Sorry for the temporarily hassle.

So, if you are using exactly the 2.0.0 release, here is the basic patch needed to the Makefile:

```diff
    Index: Makefile
    ===================================================================
    --- Makefile	(revision 22899)
    +++ Makefile	(working copy)
    @@ -51,7 +51,7 @@
     RENDER_LDFLAGS += -L/usr/local/lib
     endif
     
    -RENDER_LDFLAGS += -lmapnik -Liniparser3.0b -liniparser
    +RENDER_LDFLAGS += -lmapnik2 -Liniparser3.0b -liniparser
     
     ifeq ($(UNAME), Darwin)
     RENDER_LDFLAGS += -licuuc -lboost_regex
```

Because Mapnik2 headers are not renamed (they are still 'include/mapnik'_ it is not possible to simultaneously compile C++ applications against headers of both Mapnik2 and Mapnik 0.7.x.

However, Python applications should be able to work against either Mapnik or Mapnik2 if both are installed.

## Changes

see [[Mapnik2_Changes]]

## Building ICU

Mapnik2 requires at least icu >= 4.2.

1. Get the latest release:

```sh
        wget http://download.icu-project.org/files/icu4c/4.6/icu4c-4_6-src.tgz
        tar xzvf icu4c-4_6-src.tgz
        cd icu/source
        ./runConfigureICU Linux # on os x do: ./runConfigureICU MacOSX
        make
        sudo make install
        sudo ldconfig
```

## Building Boost

You need boost >=1.41 for Mapnik2 (ideally 1.42).

Grab some dependencies (this is for debian systems)

```sh
    sudo apt-get install libbz2-dev
```

If you are compiling on Mac OS X see: http://trac.mapnik.org/wiki/MacInstallation#Step1:RouteBC

Otherwise on linux do:

```sh
    wget http://voxel.dl.sourceforge.net/project/boost/boost/1.51.0/boost_1_51_0.tar.bz2
    tar xjvf boost_1_51_0.tar.bz2
    cd boost_1_51_0
    ./bootstrap.sh
    ./b2 \
      --with-thread \
      --with-filesystem \
      --with-iostreams \
      --with-python \
      --with-regex -sHAVE_ICU=1 -sICU_PATH=/usr/local  \
      --with-program_options \
      --with-system \
      link=shared \
      toolset=gcc \
      stage
    sudo ./b2 \
      --with-thread \
      --with-filesystem \
      --with-iostreams \
      --with-python \
      --with-regex -sHAVE_ICU=1 -sICU_PATH=/usr/local \
      --with-program_options \
      --with-system \
      toolset=gcc \
      link=shared \
      install
    sudo ldconfig
```

Note: see the custom builds of libboost_regex and libboost_python below (if using these then you can remove them from the above lines)

*Note: Starting from r2760  there is no dependency on boost::iostreams library in shape.input and '--with-iostreams' flag can be omitted while building boost.*

To rebuild just boost_regex, for example to compile/link in the right ICU support try:
 * -a forces rebuild/install

```sh
    sudo ./b2  --with-regex toolset=gcc -sHAVE_ICU=1 -sICU_PATH=/usr/local -a install
```

Note: If later when compiling mapnik you get and error like...

```
     Checking for C++ library boost_regex... no
     ...
```

it might be because you have two versions of libicu on your system. You have to recompile boost such that `ldd /usr/local/lib/libboost_regex.so` is the latest version. Since b2 tends to give some problem when passing parameters, one way to overcome this could be to move the libicu*.so.40 libraries for example and replace them with the ones compiled on /usr/local/lib/libicu* and then rebuild boost with regex support. You could later return them to the same place so that both `import mapnik` and `import mapnik2` work.

Note: you may want to (re)build boost_python against a specific version of python on your system. To do this in the most robust way (because passing command line args to b2 is hard), create a custom jam file:

```
    import option ;
    import feature ;
    if ! gcc in [ feature.values <toolset> ]
    {
        using gcc ; 
    }
    project : default-build <toolset>gcc ;
    using python
         : 2.5 # version
         : /usr/bin/python2.5 # cmd-or-prefix
         : /usr/include/python2.5/ # includes
         : /usr/lib/python2.5/config/ # directory holding libpython
         : <toolset>gcc # condition
         ;
    libraries = --with-python ;
```

Then (re) compile the boost python lib using this custom jam file (call it 'user-config.jam'):

```sh
    bjam --with-python -a -j2 --ignore-site-config --user-config=user-config.jam toolset=gcc stage -d2
    sudo cp stage/lib/libboost_python.so* /path/to/install/dir/lib # modify for your system
```