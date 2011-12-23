<!-- Name: BuildingwithAutotools -->
<!-- Version: 7 -->
<!-- Last-Modified: 2009/04/04 15:13:42 -->
<!-- Author: audifahrer -->
# Building with Autotools

If you get Mapnik from SVN or don't have a bootstrapped package (no _configure_ script in the package root) than you need to generate the Autotools Makefiles before you could configure your build. Just do a


    $ ./bootstrap

You need various developer tool installed to finish this process successful. If tools are missing then the _bootstrap_ script will tell you about.

Latest at this point you have a _configure_ script available in the package root directory. Just execute it with


    $ ./configure --help

to see a short help description about each possible switch. The important part is here:


    --enable-debug=no/yes        enables debug build (default=no)
    --enable-profiling=no/yes    enables profiling build (default=no)
    --enable-tracing=no/yes      enables tracing build (default=no)
    --enable-included-agg=no/yes enables included libagg build (default=yes)
    --enable-libxml2=no/yes      enables libxml2 support (default=no)
    --enable-cairo=no/yes        enables cairo support (default=yes)

More specific information about this switches will follow below. At first you could call the configure script without any additional parameters.


    $ ./configure

**Hint:**  Alternative you could use the _autogen.sh_ script to do the same as with the _configure_ script, but automatically bootstrap the environment:

    % ./autogen.sh

If any required dependencies are failing, then the _configure_ script will stop and tell you about it. If it runs through with success than you'll see a print out like this:


    Build configuration:
    --------------------
    
    Library support:
    cairo ......................... yes
    build included agg library..... yes
    libxml2 loader ................ no
    
    Plugin support:
    build plugin (input/postgis)... yes
    build plugin (input/gdal)...... yes
    build plugin (input/ogr)....... yes
    build plugin (input/osm)....... no
    build plugin (input/sqlite).... yes
    
    Utility support:
    build shapeindex............... yes
    build pgsql2sqlite............. yes
    
    Debugging support:
    debugger (gdb)................. no
    profiling (gprof).............. no
    tracing (log output)........... no

Some features are activated simply by installing some packages and autodetect. Others need to be activated with the switches above.

**TODO: Describe the switches! **