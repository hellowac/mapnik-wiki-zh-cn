# Steps for Mapnik Releases
    
### Prepare
    
* Ensure the [CHANGELOG](https://github.com/mapnik/mapnik/blob/master/CHANGELOG.md) is up to date.
    
* Set release date (https://github.com/mapnik/mapnik/issues/milestones), after checkins with development team
    
* Announce release plans to [group list](http://groups.google.com/group/mapnik)
    
* Ensure milestone is closed out: https://github.com/mapnik/mapnik/issues/milestones
    
### Bundled fonts and scons
    
* Consider updating Scons-local to latest release.  
  The last SCons update was 2.1.0.alpha
    
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

### Pre-tag updates

  * Update version number in [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp)
  * Set `MAPNIK_VERSION_IS_RELEASE` to 1 in [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp)
  * Update `abi_fallback` in https://github.com/mapnik/mapnik/blob/master/SConstruct
  * Update libmapnik.dylib `current_version` and `compatibility_version` in http://trac.mapnik.org/browser/trunk/src/SConscript

### Post tag updates

* Update CHANGELOG in master with the git hash the tagged release was made from.

* Generate Python API docs:
        
    sudo easy_install epydoc
    cd utils/epydoc_config
    ./test_build_epydoc.sh # will output sample docs in 'test_api' folder, view the 'index.html' file
    ./build_epydoc.sh # will build and add to to ../api_docs/python
    
* Then upload these docs - TODO (where should they go?)
    
### Packaging
    
* Source package - use auto-created downloads via github: https://github.com/mapnik/mapnik/tags and upload to downloads
    
### Builds

* Package binaries for Windoww, Mac, and Ubuntu Linux (PPA)
    
* Submit patch for updated Mapnik Portfile (http://trac.macports.org/browser/trunk/dports/python/py26-mapnik/Portfile) and homebrew Formula: https://github.com/mxcl/homebrew
    
### Web
      
* New icon for release at media.mapnik.org/images/release-VERSION.png
* Add a new 'release' item in the admin to update all links on mapnik.org
    
### Wiki Post-Release

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