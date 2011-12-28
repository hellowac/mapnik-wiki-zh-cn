<!-- Name: MapnikReleaseSteps -->
<!-- Version: 42 -->
<!-- Last-Modified: 2011/08/30 14:31:08 -->
<!-- Author: springmeyer -->
# Steps for Mapnik Releases
    
### Prepare
    
* Catch up on CHANGELOG by going through all commits
    
* Set release date (http://trac.mapnik.org/roadmap), after checkins with development team
    
* Announce release plans to mapnik-devel/mapnik-users
    
* Recruit volunteers to help with release laundry-list.
    
* Develop and add to laundry-list on this page.
    
* Sort Trac tickets, prioritize, assign, close or push.
    
### Bundled fonts and scons
    
* Consider updating Scons-local to latest release.  
  The last scons update was 2.1.0.alpha
    
        wget http://prdownloads.sourceforge.net/scons/scons-local-2.1.0.alpha.20101125.zip
        rm -rf scons
        unzip -o scons-local-2.1.0.alpha.20101125.zip -d scons/
        rm scons-local-2.1.0.alpha.20101125.zip
    
* Consider updating DeJaVu Fonts:  
  The last version updated was 2.33
    
        cd fonts
        svn rm dejavu-fonts-ttf-
        wget http://sourceforge.net/projects/dejavu/files/dejavu/2.33/dejavu-fonts-ttf-2.33.tar.bz2
        tar xvf dejavu-fonts-ttf-2.33.tar.bz2
        svn add dejavu-fonts-ttf-2.33
    
* And unifont from: http://unifoundry.com/unifont.html
    
### Testing

* Buildbot: http://miranda.nwcr.net:8010/waterfall
    
### Trac Pre-Release

* Update Roadmap details for Milestone
    
* Change default Ticket Milestone
    
* Change default Ticket Version adding new release
    
### SVN updates

* Generate Python API docs::
        
        $ sudo easy_install epydoc
        $ cd docs/epydoc_config
        $ ./test_build_epydoc.sh # will output sample docs in 'test_api' folder, view the 'index.html' file
        $ ./build_epydoc.sh # will build and add to to ../api_docs/python
    
* Then upload these docs to media.mapnik.org/api_docs replacing what is already there.
    
* Commit in trunk:
     * Update version number in http://trac.mapnik.org/browser/trunk/include/mapnik/version.hpp
     * Update `abi_fallback` in http://trac.mapnik.org/browser/trunk/SConstruct
     * Update libmapnik.dylib `current_version` and `compatibility_version` in http://trac.mapnik.org/browser/trunk/src/SConscript
    
* Update CHANGELOG with the svn r the tagged release is made from.
    
    Tag release
    
### Packaging
    
* Strip autotools/makefiles from tag::
    
        rm -rf config/
        rm bootstrap
        rm configure.ac
        rm autogen.sh
        rm mapnik.anjuta
        rm mapnik-uninstalled.pc.in
        rm mapnik.pc.in
        for i in $(find . -name Makefile*); do rm $i; done;
      
* Strip svn data from tag::
    
        $ find . -name '.svn' -exec rm -rf {} \;
    
* Package tarball/gzip::
    
        $ NAME=mapnik_VERSION
        $ cd ../
        $ svn co http://svn.mapnik.org/tags/release-0.7.1 $NAME
        $ cd $NAME
        $ find . -name '.svn' -exec rm -rf {} \;
        $ cd ../
        $ tar --exclude=".*" -cvf $NAME.tar $NAME/*
        $ gzip $NAME.tar
    
* Make sure to include:
    * Updated Python bindings (__init__.py)
    * Customize __init__.py to remove unix specific DL open stuff
    * demo/python/rundemo.py, etc
    
* Post tarball (gzip and bz2) of source at [berlios](http://developer.berlios.de/projects/mapnik)

    * mapnik-VERSION.tar.gz
    * mapnik-VERSION.tar.bz2
    
* Post win32 build (by python version) at [berlios](http://developer.berlios.de/projects/mapnik)

    * mapnik-VERSION-win32-pyVERSION.zip
    * make sure to zip with command line to avoid '__MACOSX/' files

            $ zip -9vr mapnik-0.7.1-win32-py25_26.zip  mapnik-0.7.1/*
    
### Builds

* Windows (debug builds and py25/py26 builds)

* Mac (debug builds and py25/py26 builds)
    
* Submit patch for updated Mapnik Portfile (http://trac.macports.org/browser/trunk/dports/python/py26-mapnik/Portfile)
    
### Web
      
* New icon for release at media.mapnik.org/images/release-VERSION.png
* Add a new 'release' item in the admin to update all links on mapnik.org
    
### Trac Post-Release

* Update [[Mapnik-Installation]], [MacInstallation](MacInstallation), [LinuxInstallation](https://github.com/mapnik/mapnik/wiki/LinuxInstallation) and [WindowsInstallation](WindowsInstallation) links
* Create a release page from the relevant section of CHANGELOG like this page [Release0.7.1](Release0.7.1)
* Update [MapnikReleases](MapnikReleases), a starting page for users to learn about Mapnik development
    
### Announce
    
* Notify Packagers for Linux distros ([PackageBuilding](PackageBuilding))
* Notify Packagers for OSGEO4w: http://norbit.de/
* Mapnik lists
* Mapnik.org news
* OSGEO News item: http://www.osgeo.org/content/news/submit_news.html
* Freshmeat : http://freshmeat.net/projects/mapnik
* FreeGIS : http://www.freegis.org
* SlashGeo : http://slashgeo.org/
* OpenStreetMap : [OSM-Dev] [OSM-Talk] ??
