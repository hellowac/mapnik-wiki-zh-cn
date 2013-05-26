# Steps for Mapnik Releases
    
### Prepare
    
* Ensure the [CHANGELOG](https://github.com/mapnik/mapnik/blob/master/CHANGELOG.md) is up to date.
    
* Set release date after checkins with development team
    
* Announce release plans to [group list](http://groups.google.com/group/mapnik)
    
* Ensure [milestone](https://github.com/mapnik/mapnik/issues/milestones) is closed out


### Testing

* Ensure all tests pass (`make test`)

* Test Mapnik with `INPUT_PLUGINS=''`

### Bundled fonts and scons
    
* Consider updating Scons-local to latest release.  
  The last SCons update was 2.3.0.alpha
    
        wget http://prdownloads.sourceforge.net/scons/scons-local-2.3.0.zip
        rm -rf scons
        unzip -o scons-local-2.3.0.zip -d scons/
        rm scons-local-2.3.0.zip
    
* Consider updating DeJaVu Fonts:  
  The last version updated was 2.33
    
        cd fonts
        svn rm dejavu-fonts-ttf-
        wget http://sourceforge.net/projects/dejavu/files/dejavu/2.33/dejavu-fonts-ttf-2.33.tar.bz2
        tar xvf dejavu-fonts-ttf-2.33.tar.bz2
        svn add dejavu-fonts-ttf-2.33
    
* Check for new [unifont release](http://unifoundry.com/unifont.html)

### Release candidate

Consider first promoting a release candidate from master:

```sh
cd /tmp
MAPNIK_VERSION="2.2.0-rc1"
TARBALL_NAME="mapnik-v${MAPNIK_VERSION}"
git clone git@github.com:mapnik/mapnik.git ${TARBALL_NAME}
cd ${TARBALL_NAME}
git rev-list --max-count=2 HEAD | tail -n+2 > GIT_REVISION
git describe > GIT_DESCRIBE
cd ../
rm -rf ${TARBALL_NAME}/.git
rm -rf ${TARBALL_NAME}/.gitignore
tar cjf ${TARBALL_NAME}.tar.bz2 ${TARBALL_NAME}/
```

### Pre-tag updates

  * Update version number in [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp)
  * Set `MAPNIK_VERSION_IS_RELEASE` to 1 in [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp)
  * Update `abi_fallback` to right version and stripping any `-pre` in [SConstruct](https://github.com/mapnik/mapnik/blob/master/SConstruct)
  * then:

```
make uninstall && ./configure && make install
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
git ci -a -m "update CHANGELOG for mapnik v${MAPNIK_VERSION} release"
git push
```

### Tagging

Note: we use [annotated tags](http://stackoverflow.com/questions/4971746/why-should-i-care-about-lightweight-vs-annotated-tags/4971817#4971817) below instead of lightweight tags

```sh
MAPNIK_VERSION=`mapnik-config --version`
git tag --annotate "v${MAPNIK_VERSION}" -m "tagging v${MAPNIK_VERSION}"
git push --tags
```

* Create a clean tarball:

```sh
cd /tmp
MAPNIK_VERSION=`mapnik-config --version`
TARBALL_NAME="mapnik-v${MAPNIK_VERSION}"
git clone git@github.com:mapnik/mapnik.git ${TARBALL_NAME}
cd ${TARBALL_NAME}
git checkout "tags/v${MAPNIK_VERSION}"
# get one commit back to match the changelog
git rev-list --max-count=2 HEAD | tail -n+2 > GIT_REVISION
git describe > GIT_DESCRIBE
cd ../
rm -rf ${TARBALL_NAME}/.git
rm -rf ${TARBALL_NAME}/.gitignore
tar cjf ${TARBALL_NAME}.tar.bz2 ${TARBALL_NAME}/
```

Note: the GIT_REVISION/GIT_DESCRIBE files are used as per https://github.com/mapnik/mapnik/issues/1170. We write a file before making the tarball so that systems that do not have git installed or that download the raw tarball can still know the git revision and describe output mapnik-config will report after source build.

* Go back to the mapnik source checkout and generate Python API docs:

```sh
cd ${MAPNIK_SOURCES}
sudo pip install epydoc
cd utils/epydoc_config
./build_epydoc.sh
PYDOCS_DEST="../../../mapnik.github.com/docs/v`mapnik-config --version`/api/python/"
mkdir -p $PYDOCS_DEST
cp -r ./mapnik-python-`mapnik-config --version`/* $PYDOCS_DEST/
cd ${MAPNIK_SOURCES}
```

### Post tag updates

* Update master branches entries in [CHANGELOG](https://github.com/mapnik/mapnik/blob/master/CHANGELOG.md) from the new release (if relevant, e.g. if you are tagging and releasing a stable release not from the master branch).

If this was a major release and a stable series is likely, now branch it, for example a `2.1.0` release would warrant an immediate `2.1.x` branch for a stable series of bugfix releases.

```
cd ${MAPNIK_SOURCES}
git branch 2.1.x
git checkout 2.1.x
git push origin 2.1.x
git checkout master
```

Now bump versions again:

   * edit [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp) again, incrementing version # and changing `MAPNIK_VERSION_IS_RELEASE` back to `0` to set up for the next release
   * update the `abi_fallback` in SConstruct

```
make uninstall && ./configure && make install
MAPNIK_VERSION=`mapnik-config --version`
git ci include/mapnik/version.hpp SConstruct -m "now working on mapnik v${MAPNIK_VERSION}"
git push
```

_Now also repeat the above for any stable branches created._

Finally, create new github milestones for the newly created future release #s.

And create new launchpad PPA for the target release(s) and series at https://launchpad.net/~mapnik, then add these release PPA's to the list that gets build nightly: https://github.com/mapnik/mapnik-packaging/blob/master/debian-nightlies/nightly-build.sh#L22-40

### Update Mapnik.org

* Update the [download page](http://mapnik.org/download/)(download/index.markdown)
* Write new blog post with updated release links and links to changelog
* Push python api docs and update docs/index.markdown
    
### Packaging
    
* Package binaries for Windows, Mac, and Ubuntu Linux (PPA)
* Upload Mac/Win binary packages to the [github downloads page](https://github.com/mapnik/mapnik/downloads)
* Submit patch for updated [Mapnik Portfile](http://trac.macports.org/browser/trunk/dports/python/py26-mapnik/Portfile) and [homebrew Formula](https://github.com/mxcl/homebrew)
    
### Wiki Post-Release

* Update [[Mapnik-Installation]], [MacInstallation](MacInstallation), [LinuxInstallation](https://github.com/mapnik/mapnik/wiki/LinuxInstallation) and [WindowsInstallation](WindowsInstallation) links
* Create a release page from the relevant section of CHANGELOG like this page [Release0.7.1](Release0.7.1)
* Update [MapnikReleases](MapnikReleases), a starting page for users to learn about Mapnik development
    
### Announce
    
* Mapnik users list
* Mapnik news twitter account: http://twitter.com/mapnikproject
* OpenStreetMap : [OSM-Dev]
* Notify Packagers for Linux distros ([PackageBuilding](PackageBuilding))
* Notify Packagers for OSGEO4w: http://norbit.de/