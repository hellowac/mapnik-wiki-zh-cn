<!-- Name: MapnikViewer -->
<!-- Version: 21 -->
<!-- Last-Modified: 2011/02/07 21:46:12 -->
<!-- Author: springmeyer -->
The Mapnik Viewer is a GUI tool for rendering and viewing maps based on Mapnik XML mapfiles.

It's available under source:trunk/demo/viewer and needs to be compiled after manually modifying the build settings.

----
 

[[Image(mapnik_viewer.png)]]
----

== A Desktop XML Viewer == 

 1. View tile images on-the-fly.
 2. Debug information on bad config files, points to the erroneous line.
 3. Shows scale and envelope for current view.
 4. Fast zooming and point-based attribute queries.
 5. Export to a variety of formats including tif.

## Requirements
 * A working Mapnik installation
 * A Mapnik XML file to view
 * Qt4 including dev files (for example, see [Qt/Mac Open Source Edition](http://trolltech.com/developer/downloads/qt/mac))
 * Qmake

## Compiling

 1. Modify [source:trunk/demo/viewer/viewer.pro viewer.pro] to match your system include and lib directories for boost, your mapnik build, unicode, and freetype.
  * Most default installs put the mapnik libs and includes in `usr/local`, thus requiring an include like:
   
    #!sh
    INCLUDEPATH += /usr/local/include/mapnik
  * And a lib like:
   
    #!sh
    unix:LIBS += -L/usr/local/lib -lmapnik
  * And to link boost, freetype, and unicode from macports on Mac 10.5, for example, would require:
   
    #!sh
    INCLUDEPATH += /opt/local/include/boost-1_35
    INCLUDEPATH += /opt/local/include/unicode
    INCLUDEPATH += /opt/local/include/freetype2
    INCLUDEPATH += /opt/local/include
    unix:LIBS +=   -L/opt/local/lib -lfreetype

  * Since Ubuntu 10.04 those settings are enough:

    QMAKE_CXXFLAGS +=' -ansi'
    INCLUDEPATH += /usr/include/freetype2
    LIBS += -lmapnik

  * A patch for Mac OS 10.5 is [attachment:wiki:MapnikViewer:viewer.patch viewable here], and [downloadable here](http://trac.mapnik.org/raw-attachment/wiki/MapnikViewer/viewer.patch)

 2. Modify main.cpp by setting the correct paths to Mapnik's plug-ins and fonts directories
  * [source:trunk/demo/viewer/main.cpp?order=date&desc=1#L33 Lines 33 - 37]
  * On most systems these lines should point to`/usr/local/lib/mapnik/`
   
    #!sh
    datasource_cache::instance()->register_datasources("/usr/local/lib/mapnik/input"); 
    freetype_engine::register_font("/usr/local/lib/mapnik/fonts/DejaVuSans.ttf");
    freetype_engine::register_font("/usr/local/lib/mapnik/fonts/DejaVuSans-Bold.ttf");
    freetype_engine::register_font("/usr/local/lib/mapnik/fonts/DejaVuSansMono.ttf");

 3. Then run Qmake to generate a makefile

    #!sh
    cd mapnik-svn-tree/demo/viewer
    qmake -makefile

On Mac OSX the above will generate  an Xcodeproject. To generate a normal Makefile do:

    #!sh
    qmake -spec macx-g++

 4. Finally, run Make to build the *viewer.app* or *viewer.exe*

    #!sh
    make

(On OS X, you may need to instead run "open viewer.xcodeproj" to open the project in Apple's XCode environment.)

 * Your make output should be something like:

    #!sh
    $ make
    make -f Makefile.Release
    /opt/local/bin/uic forms/about.ui -o ui_about.h
    /opt/local/bin/uic forms/info.ui -o ui_info.h
    /opt/local/bin/uic forms/layer_info.ui -o ui_layer_info.h
    c++ -c -pipe  -DDARWIN -Os -Wall -W -DQT_NO_DEBUG -DQT_GUI_LIB -DQT_CORE_LIB -DQT_SHARED -I/opt/local/share/qt4/mkspecs/macx-g++ -I. -I/opt/local/include/qt4/QtCore -I/opt/local/include/qt4/QtCore -I/opt/local/include/qt4/QtGui -I/opt/local/include/qt4/QtGui -I/opt/local/include/qt4 -I/usr/local/include/mapnik -I/opt/local/include/boost-1_35 -I/opt/local/include/unicode -I/opt/local/include -I/opt/local/include/freetype2 -I. -Irelease -I. -o release/main.o main.cpp
    [...]
 * If it fails you need to go back to the viewer.pro and set more lib and include paths
 * A successful build will output the ready to run graphical program in that directory.

## Usage

Double click on the resulting application (viewer.app on Mac OS)
 * You can then load map files from the file menu (make sure you have absolute paths set to datasources).
 * Hit the *Home* button to zoom to the data extent.
 * The rest should be obvious.

You can also load your XML files when launching the viewer from a terminal:


    #!sh
    # On linux this would look like:
    # ./viewer /path/to/your.xml
    # On mac this would look like:
    $ ./viewer.app/Contents/MacOS/viewer /path/to/your.xml
    # or
    $ open -a viewer

or




    #!sh
    # ./viewer your.xml -1,50,1,52

or


    #!sh
    # ./viewer # (open your.xml from file menu)

## Further Reading

Related mailing list discussions:

 * https://lists.berlios.de/pipermail/mapnik-devel/2008-February/000501.html