# Steps for Mapnik Releases
    
### Prepare
    
* Ensure the [CHANGELOG](https://github.com/mapnik/mapnik/blob/master/CHANGELOG.md) is up to date.
    
* Set release date after checkins with development team
    
* Announce release plans to [group list](http://groups.google.com/group/mapnik)
    
* Ensure [milestone](https://github.com/mapnik/mapnik/issues/milestones) is closed out

* Ensure all tests pass (`make test`)
    
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
    
* Check for new [unifont release](http://unifoundry.com/unifont.html)

### Pre-tag updates

  * Update version number in [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp)
  * Set `MAPNIK_VERSION_IS_RELEASE` to 1 in [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp)
  * Update `abi_fallback` in [SConstruct](https://github.com/mapnik/mapnik/blob/master/SConstruct)
  * `make install`, then:

```
MAPNIK_VERSION=`mapnik-config --version`
git commit -a -m "setting up for mapnik v${MAPNIK_VERSION} release" 
git push
```

  * Update CHANGELOG with the git hash of latest commit using the output of:

```
git rev-parse --verify HEAD
```

  * Then, push change:

```
git ci -a -m "update CHANGELOG"
git push
```

### Tagging

```sh
MAPNIK_VERSION=`mapnik-config --version`
git tag "v${MAPNIK_VERSION}" -m "tagging v${MAPNIK_VERSION}"
git push --tags
```

* Create a clean tarball:

```sh
cd /tmp
TARBALL_DIR="mapnik-v`mapnik-config --version`"
git clone --depth=1 \
  git@github.com:mapnik/mapnik.git $TARBALL_DIR
cd $TARBALL_DIR
git checkout "v`mapnik-config --version`"
cd ../
rm -rf $TARBALL_DIR/.git
rm -rf $TARBALL_DIR/.gitignore
tar cjf $TARBALL_DIR.tar.bz2 $TARBALL_DIR/
```

Then upload that tarball to the [downloads page](https://github.com/mapnik/mapnik/downloads).


### Post tag updates

* Update master branches entries in [CHANGELOG](https://github.com/mapnik/mapnik/blob/master/CHANGELOG.md) from the new release (if relevant).

Now, edit [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp) again, incrementing version # and changing `MAPNIK_VERSION_IS_RELEASE` back to `0` to set up for the next release:

```
./configure
make install
MAPNIK_VERSION=`mapnik-config --version`
git ci include/mapnik/version.hpp -m "now working on mapnik v${MAPNIK_VERSION}"
git push
```

* Generate Python API docs:

```sh
sudo pip install epydoc
cd utils/epydoc_config
./build_epydoc.sh
```

* Then upload these docs - TODO (where should they go?)
    
### Packaging
    
* Package binaries for Windows, Mac, and Ubuntu Linux (PPA)
* Upload Mac/Win binary packages to the [github downloads page](https://github.com/mapnik/mapnik/downloads)
* Submit patch for updated [Mapnik Portfile](http://trac.macports.org/browser/trunk/dports/python/py26-mapnik/Portfile) and [homebrew Formula](https://github.com/mxcl/homebrew)

### Web
      
* New blog post at [mapnik.org](http://mapnik.org) updated release links
    
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