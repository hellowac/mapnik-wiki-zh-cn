<!-- Name: Mapnik2 -->
<!-- Version: 64 -->
<!-- Last-Modified: 2011/04/14 18:26:35 -->
<!-- Author: springmeyer -->
# Mapnik2


Mapnik2 is current trunk and a new era of the mapnik codebase that uses boost features only available in boost >=1.41, icu >=4.2, and is a testbed for next-generation Mapnik features.

Pre-release installers for Mapnik2 are available for Mac OS X: http://dbsgeo.com/downloads/#mapnik-2.0.0

For Linux source compiles are required, see instructions below.

Mapnik2 implements a naming change for ease of development and testing .

So in python for now you do:

```python
    >>> import mapnik2 # . This enables running the Mapnik 0.7.x series alongside Mapnik2.
```

And C++ programs must link against mapnik2:

```sh
    -L/usr/local/lib -lmapnik2
```

See also the brainstorming page for Future Mapnik at [[Ideas_FutureMapnik]]

## Compatibility

The Mapnik2 API has advanced (requiring breakages) and the XML syntax has changed in specific cases.

Therefore Mapnik2 is the [first release](MapnikReleases) with significant backward incompatibility. See [[Mapnik2_Changes]]

# Upgrade Guide

1. rebuild all shapefile indexes

2. upgrade stylesheets with a python script:

We have written a python converter to seamlessly upgrade your pre-Mapnik2 stylesheets to be fully compatible with Mapnik2.

After installing Mapnik2 you will have a new command available called 'upgrade_map_xml.py':

```
    $ upgrade_map_xml.py
        Usage: upgrade_map_xml.py <input_file> <output_file>
```

Also, for osm.xml users, you will note that this script does not preserve entities (sorry). You may be interested in an experimental version of this script (but not installed by default) which does. See:

***WARNING*** this script has not been kept in sync with the main script mentioned above.

https://github.com/mapnik/mapnik/blob/master/utils/upgrade_map_xml/upgrade_map_xml_keep_ent.py

Also, we have ported support for the new Mapnik2 syntax to the upcoming 0.7.2 release, so you can stay on the 0.7 series but keep your stylesheets in the cleaner Mapnik2 format.

## External Applications

Special care will be needed to run various external applications against Mapnik2:

### Python Applications with Mapnik2

Note: you cannot do:

```python
    >>> import mapnik
    >>> import mapnik2
```

This is because the namespaces will clash. We ultimately plan to release Mapnik2 using the standard `>>> import mapnik` namespace, so its not worth the trouble to make the above work. The rule of thumb is that you can have both installed just only run one at a time.

### Cascadenik

There is a branch of Cascadenik that is adding Mapnik2 compatibility at https://github.com/mapnik/Cascadenik/tree/mapnik2

### nik2img

Nik2img as of 0.5.0 supports both mapnik and mapnik2 transparently. Pass --mapnik-version 1 or mapnik-version 2 to force the usage of a single one (it will default to using Mapnik2) 

### mod_tile/renderd

Supports Mapnik2 as of [r22900](http://trac.openstreetmap.org/changeset/22900)
But requires a patch to the Makefile and moving to the side any non-mapnik2 headers.

Here is the patch needed to the Makefile:

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

Because Mapnik2 headers are not renamed 'include/mapnik' it is not possible to simultaneously compile C++ applications against headers of both Mapnik2 and Mapnik 0.7.x.

However, Python applications should be able to work against either Mapnik or Mapnik2 if both are installed.

So, for C++ compiles if you currently have old mapnik headers installed you must remove them and install mapnik2 headers in their place:

```sh
    rm -rf /usr/local/include/mapnik
    # re-install mapnik2 headers
    cd <mapnik2 sources>
    sudo scons install
    # build mod_tile/renderd with above patch
    svn co http://svn.openstreetmap.org/applications/utils/mod_tile
    cd mod_tile
    make # will take a long time
    sudo make install
    # now if you want to later rebuild mod_tile agains Mapnik 0.7.x
    # just remove the mapnik2 headers and re-install mapnik 0.7.x
    # this is easy as mapnik2 now supports uninstalling
    cd <old mapnik sources>
    sudo scons uninstall # yah!
    # then recompile mod_tile/ rendered
    cd mod_tile
    make clean
    make
    sudo make install
```

## Getting Mapnik2 source

Previously Mapnik2 was in a branch, but as of Dec 16th, 2009 is it mainline trunk

Checkout trunk with:

```
    svn co http://svn.mapnik.org/trunk mapnik2
```

Or switch from the old branch to trunk by doing:

```
    svn switch http://svn.mapnik.org/trunk .
```

Similarly, if you wish to stay on the previous trunk code, that is now the 0.7.1 release:

```
    svn switch http://svn.mapnik.org/tags/release-0.7.1 .
```

## Changes

Mapnik2 is also about harmonizing C++ coding conventions and thus a few class names have changed:

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
    wget http://voxel.dl.sourceforge.net/project/boost/boost/1.46.1/boost_1_46_1.tar.bz2
    tar xjvf boost_1_46_1.tar.bz2
    cd boost_1_46_1
    ./bootstrap.sh
    ./bjam \
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
    sudo ./bjam \
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
    sudo ./bjam  --with-regex toolset=gcc -sHAVE_ICU=1 -sICU_PATH=/usr/local -a install
```

Note: If later when compiling mapnik you get and error like...

```
     Checking for C++ library boost_regex... no
     ...
```

it might be because you have two versions of libicu on your system. You have to recompile boost such that `ldd /usr/local/lib/libboost_regex.so` is the latest version. Since bjam tends to give some problem when passing parameters, one way to overcome this could be to move the libicu*.so.40 libraries for example and replace them with the ones compiled on /usr/local/lib/libicu* and then rebuild boost with regex support. You could later return them to the same place so that both `import mapnik` and `import mapnik2` work.

Note: you may want to (re)build boost_python against a specific version of python on your system. To do this in the most robust way (because passing command line args to bjam is hard!), create a custom jam file:

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