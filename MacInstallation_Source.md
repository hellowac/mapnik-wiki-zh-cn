<!-- Name: MacInstallation/Source -->
<!-- Version: 4 -->
<!-- Last-Modified: 2010/11/02 06:37:18 -->
<!-- Author: willwhite -->


# Installing Mapnik on OS X from Source

Detailed notes for installing from source are below.

There are *three main routes* for getting Mapnik installed on Mac OS X.

*Please* take a moment to decide which one fits you best.

|| *Route A - Option 1* || _Easiest_ -> Recommended for users *new to Python* or users already using Python26 from Macports. ||
|| *Route A - Option 2* || _Hardest_ -> Recommended for advanced users already using Python26 from Macports. ||
|| *Route B* || _Moderate_ -> Recommended for users who actively using the Python that came pre-installed with Leopard.||
|| *Route C* || _Moderate_ -> Recommended for users who are running Python installed from python.org.||

*Hint*: open Terminal.app and type:

    #!sh
    $ which python
 * This will give the path to the python executable
  * '/opt/local...' means you are using Macports Python
  * /System/... means you are using the python pre-installed by Apple
  * /Library/... means you are likely using MacPython from http://python.org

 

[[Image(http://trac.mapnik.org/raw-attachment/wiki/MacInstallation/mapnik_on_mac_os.png)]]

# Step 1: Install Xcode

First make sure you have XCode installed.
 * XCode comes as an optional Installer on Leopard Install Discs
 * If your CD contains at least version 3.1, you can use the CD installer, otherwise download from ADN

*Recommended*: The latest version of XCode can be downloaded from the Apple Developer Network (ADN) site
 * [ADN](http://developer.apple.com/technology/Xcode.html) (~900 MB, requires registering with Apple)
 * Either the iPhone SDK or XCode can be used.

# Step 2: Install Macports

No matter what route you take you'll likely want [Macports](http://www.macports.org/install.php) installed.
  * Look for the latest dmg: [Current version is 1.8.1](http://www.macports.org/install.php)
  * Nice [overview article by Apple](http://developer.apple.com/mac/articles/opensource/workingwithmacports.html)


Check your Macports Installation:

    #!sh
    $ port # should take you into 'interactive mode'
    > quit # to leave...
 * If the port command is not available then you'll need to add this to your ~/.profile hidden file

    'export PATH=/opt/local/bin:/opt/local/sbin:$PATH'

# Step 3: Choose your Route, then begin...

## Route A

Update Macports

    #!sh
    sudo port selfupdate
 * This will fetch the latest port updates in addition to *syncing* with the remote repository.
 * If this command fails try:

    #!sh
    sudo port sync

Install Python 26

    #!sh
    $ sudo port install python26 python_select # will take ~ 1 hour
 * Note: If you are on a dual-core or quad-core machine use the extra argument ['build.jobs=N'](http://trac.macports.org/wiki/howto/ParallelBuilding) to speed up Macports.
 * The above command on a quad-core machine would be:

    $ sudo port install python26 python_select build.jobs=4

Switch to using the Macports Python26 (if you are not already using it)

    #!sh
    $ sudo python_select python26 # switch to using Macports python just installed

Install core Mapnik dependencies

    #!sh
    $ sudo port install boost +python26 icu libpng jpeg libgeotiff libxml2 freetype # go for a long walk!
 * *Note*: The '+' invokes a certain boost variant that includes boost-python (which is needed for mapnik's python bindings). The trick is that this requires Macports downloading its own version of python26. This behavior *REQUIRES* you to switch to using the macports version of PYTHON for building mapnik otherwise you will get a 'VERSION MISMATCH' error when you are trying to `>>> import mapnik' because the boost python bindings are built against a different version of python than the interpreter you are running.

*Optional*: Install extra libraries needed *only* if you want to read custom formats (other than shapefiles) or make maps in PDF/SVG formats

    #!sh
    $ sudo port install sqlite3 gdal postgresql83-server postgresql83 postgis cairo cairomm py26-cairo 
 * *Note*: if postgis fails with

    Error: Checksum (sha1) mismatch for postgis-1.3.3.tar.gz
    Error: Target org.macports.checksum returned: Unable to verify file checksums
    Error: Status 1 encountered during processing.

Then we can update the portfile locally to patch the problem 

    #!sh
    $cd `port dir postgis`
    $sudo cp Portfile Portfile.orig
    $port edit postgis
Change line 23 of the port file to: 

    checksums		sha1 665abd2869e5c59140ed30c20ba1970ea3880fd4"


## Route A | Option 1 - Install Mapnik Port


    #!sh
    $ port info py26-mapnik # get options for install, for example +gdal +postgis are needed to get gdal and postgis support
    $ sudo port -d install py26-mapnik +postgis +gdal +cairo # -d turns on debug mode (send any errors to mapnik-users list)
 * Note: if you want to see how the *py26-mapnik* portfile works [check out the source](http://www.macports.org/ports.php?by=name&substr=mapnik). 

Then do:

    #!sh
    $ python
    >>> import mapnik # if no errors, you're good, your're done, wahoo!

If you get a 'VERSION MISMATCH' this likely means that the 'boost_python.dylib' library (installed by the boost +python26 port) was linked wrong and unfortunately, is a common and re-occurring macports bug (http://trac.macports.org/ticket/21444).

In english, that means that Apple provides a copy of python and so does macports, which confuses the heck out of boost python.

On snow leopard, usually this exact command fixes the problem:

    sudo install_name_tool -change /System/Library/Frameworks/Python.framework/Versions/2.6/Python /opt/local/Library/Frameworks/Python.framework/Versions/2.6/Python /opt/local/lib/libboost_python-mt.dylib

If that does not fix the problem, please email the mapnik-users list for further assistance and provide the output of:

    otool -L /opt/local/lib/libboost_python*
    otool -L /opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/mapnik/_mapnik.so

## Route A | Option 2  - Install Mapnik Latest release from source


    #!sh
    $ svn co http://svn.mapnik.org/tags/release-0.7.1/ mapnik
    $ cd mapnik
    $ touch config.py # create a blank python file...
    $ open config.py # to edit in your favorite text editor...

Copy and paste all this text into that 'config.py' file:

    #!python
    # config.py file that sits in mapnik source directory
    BOOST_INCLUDES = '/opt/local/include'
    BOOST_LIBS = '/opt/local/lib'
    FREETYPE_CONFIG = '/opt/local/bin/freetype-config'
    XML2_CONFIG = '/opt/local/bin/xml2-config'
    ICU_INCLUDES = '/opt/local/include'
    ICU_LIBS = '/opt/local/lib'
    PNG_INCLUDES = '/opt/local/include'
    PNG_LIBS = '/opt/local/lib'
    JPEG_INCLUDES = '/opt/local/include'
    JPEG_LIBS = '/opt/local/lib'
    TIFF_INCLUDES = '/opt/local/include'
    TIFF_LIBS = '/opt/local/lib'
    PROJ_INCLUDES = '/opt/local/include'
    PROJ_LIBS = '/opt/local/lib'
    GDAL_CONFIG = '/opt/local/bin/gdal-config'
    PG_CONFIG = '/opt/local/lib/postgresql83/bin/pg_config'
    SQLITE_INCLUDES = '/opt/local/include'
    SQLITE_LIBS = '/opt/local/lib'
    FRAMEWORK_PYTHON = False
    INPUT_PLUGINS = 'gdal,ogr,postgis,raster,shape,sqlite'
    # or use...
    # INPUT_PLUGINS = 'all'

Configure and Install Mapnik

    #!sh
    $ cd mapnik # make sure you are inside the source dir
    $ python scons/scons.py configure
    $ python scons/scons.py
    $ sudo python scons/scons.py install

* Note: if *pycairo* is not found during the configure step you need to add a non standard path to PKG_CONFIG_PATH

    #!sh
    $ port contents py26-cairo | grep .pc  
    /opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/pkgconfig/pycairo.pc
    $ export PKG_CONFIG_PATH=/opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/pkgconfig/
Then rerun the configure step.

If the configure step fails or is interrupted, stale dependency tests can be left over in a directory called .sconf_temp. This can cause future configure attempts to fail. If you're experiencing problems, look for this folder and remove it.

## Route B and C

These two routes are essentially the same, just make sure:
 * You know which Python Version you are using
  * The 'python_select' tool from macports is handy for switching between the macports python and the system python (python 25)
 * If you have used different versions of Python in the past you should confirm that you have edited your PYTHONPATH correctly to point to the correct site-packages or other needed locations
  * Edit PYTHONPATH in your ~/.bash_profile (for user) or /etc/profile (for all users)
 * Use the FRAMEWORK_SEARCH_PATH = '/Library/Frameworks/Python.framework/Versions/2.6/' option to link against Python26 installed from python.org


## Step 1: Route B/C

Install Latest Boost from source


    #!sh
    curl -O http://voxel.dl.sourceforge.net/project/boost/boost/1.42.0/boost_1_42_0.tar.bz2
    tar xjvf boost_1_42_0.tar.bz2
    cd boost_1_42_0
    export BOOST=`pwd`
    cd tools/jam/src
    ./build.sh darwin
    cd bin.macosxx*
    export PATH=`pwd`:$PATH
    cd $BOOST

Finally, then compile boost with `bjam`

Note: newer macs with 64 bit fireware will default to 64 bit libraries, or x86_64 arch. It is recommended to build boost multi-arch (both 32 and 64 bit to avoid potential problems later on)

If you don't want to build both 32 and 64 bit and would rather stick with the single default arch of your compiler remove the below 'address-model' and  'architecture' flags.


    bjam  --with-python \
      --with-thread --with-filesystem \
      --with-iostreams --with-regex \
      --with-program_options --with-system \
      toolset=darwin \
      address-model=32_64 \
      architecture=x86 \
      stage
    
    sudo bjam  --with-python \
      --with-thread --with-filesystem \
      --with-iostreams --with-regex \
      --with-program_options --with-system \
      toolset=darwin \
      address-model=32_64 \
      architecture=x86 \
      install

Note: to build boost_regex with icu support you need to pass `-sHAVE_ICU=1`
To rebuild just boost regex do:
{{{ 
sudo bjam  --with-regex \
  toolset=darwin \
  -sHAVE_ICU=1 -sICU_PATH=/opt/local \
  -a install
}}}

Install remaining dependencies from either Macports, [Kyngchaos Frameworks](http://www.kyngchaos.com/wiki/software:frameworks), or from source.

  * For dependencies via Macports (other than python and boost) see Route A above.
  * For Kyngchaos installs:
    * Proj4/SQLite/Freetype/UnixImageIO/GDAL from: http://www.kyngchaos.com/wiki/software:frameworks
    * And PostGIS/Postgres from http://www.kyngchaos.com/software:postgres
  * For Source installs see MacInstallationSource

Then download, configure, and install Mapnik:

Grab from latest release:

    #!sh
    $ curl -O http://download.berlios.de/mapnik/mapnik-0.7.1.tar.bz2
    $ tar xjvf mapnik-0.7.1.tar.bz2
    $ cd mapnik-0.7.1

Or grab latest release from subversion:

    #!sh
    $ svn co http://svn.mapnik.org/tags/release-0.7.1/ mapnik
    $ cd mapnik

Edit your 'config.py':

    #!sh
    $ touch config.py
    $ open config.py

 * Mapnik uses `SCons` to find dependencies, a next-generation `make` (see UsingScons for more info).
  * MacPorts installs libraries into `/opt/` while SCons by default expects dependencies in `/usr/`
  * Anything installed by Macports or Kygnchaos will need custom paths in 'config.py'

Here is an example 'config.py':

    #!python
    # example config.py file
    
    # Uncomment if you want to use Python26 from Python.org (option available in Mapnik >=0.6.1)
    # FRAMEWORK_SEARCH_PATH = '/Library/Frameworks/'
    # otherwise we'll link to the Apple provided Python
    FRAMEWORK_SEARCH_PATH = '/System/Frameworks/'
    
    # use lots of cores
    JOBS = 4
    
    # full compiler optimization
    OPTIMIZATION = '3'
    
    # build with debug output
    DEBUG = True
    
    # boost from source
    BOOST_INCLUDES = '/usr/local/include/boost-1_39/'
    BOOST_LIBS = '/usr/local/lib/'
    BOOST_TOOLKIT = 'xgcc40'
    
    # icu from macports
    ICU_INCLUDES = '/opt/local/include'
    ICU_LIBS = '/opt/local/lib'
    
    # Imaging libs from Kyngchaos
    PNG_INCLUDES = '/Library/Frameworks/UnixImageIO.framework/unix/include'
    PNG_LIBS = '/Library/Frameworks/UnixImageIO.framework/unix/lib'
    JPEG_INCLUDES = '/Library/Frameworks/UnixImageIO.framework/unix/include'
    JPEG_LIBS = '/Library/Frameworks/UnixImageIO.framework/unix/lib'
    TIFF_INCLUDES = '/Library/Frameworks/UnixImageIO.framework/unix/include'
    TIFF_LIBS = '/Library/Frameworks/UnixImageIO.framework/unix/lib'
    
    # SQLite from Kyngchaos
    SQLITE_INCLUDES = '/Library/Frameworks/SQLite3.framework/unix/include'
    SQLITE_LIBS = '/Library/Frameworks/SQLite3.framework/unix/lib'
    
    # Proj4 from Kyngchaos
    PROJ_LIBS = '/Library/Frameworks/PROJ.framework/unix/lib'
    PROJ_INCLUDES = '/Library/Frameworks/PROJ.framework/unix/include'
    
    # Freetype from Kyngchaos
    FREETYPE_CONFIG='/Library/Frameworks/FreeType.framework/unix/bin/freetype-config'
    
    # gdal/postgres/postgis from Kyngchaos
    GDAL_CONFIG = '/Library/Frameworks/GDAL.framework/unix/bin/gdal-config'
    PG_CONFIG = '/usr/local/pgsql/bin/pg_config'
    INPUT_PLUGINS = 'gdal,ogr,postgis,raster,shape,sqlite'
    # or use...
    # INPUT_PLUGINS = 'all'



    #!sh
    $ python scons/scons.py configure DEBUG=True INPUT_PLUGINS='all' # any options provided on command line will OVERRIDE config.py options
    $ python scons/scons.py
    $ sudo python scons/scons.py install


## Testing

If this works without error - Congrats and welcome to Mapnik on Mac OS!

    #!sh
    $ python
    >>> import mapnik
    registered datasource : gdal # this will only show up if you build with DEBUG=True
    registered datasource : postgis # this will only show up if you build with DEBUG=True
    registered datasource : raster # this will only show up if you build with DEBUG=True
    registered datasource : shape # this will only show up if you build with DEBUG=True
    >>> dir(mapnik) # This gets you a list of symbols
    ['BoostPythonMetaclass', 'Color', 'Coord', 'CreateDatasource', ...]
    >>> help(mapnik)

Check out which libraries libmapnik.dylib has linked against:
 * Freetype for example could have been linked to either `/opt/` or `/usr/`

    #!sh
    otool -L /usr/local/lib/libmapnik.dylib

## References

 * Extended MacInstallationSource guide
 * WORK IN PROGRESS: For _Optional_ dependencies (such as Cairo, GDAL, and PostGIS), also see the *out-of-date* MacInstallation/Optional