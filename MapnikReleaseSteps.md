# Steps for Mapnik Releases
    
### Prepare
    
- Ensure the [CHANGELOG](https://github.com/mapnik/mapnik/blob/master/CHANGELOG.md) is up to date.
- Announce release plans to [group list](http://groups.google.com/group/mapnik)
- Ensure [milestone](https://github.com/mapnik/mapnik/milestones) is closed out

### Testing

- Ensure all tests pass (`make test`)
- Test Mapnik with `INPUT_PLUGINS=''` and ensure tests pass for what functionality is available
- Test with `./configure WARNING_CXXFLAGS="-Wextra"` to ensure all problematic warnings are solved or triaged.

### Bundled fonts and scons

Consider updating Scons-local to [latest release](http://www.scons.org/download.php): The last SCons update was 2.3.4.
    
```sh
wget http://prdownloads.sourceforge.net/scons/scons-local-2.3.4.zip
rm -rf scons
unzip -o scons-local-*.zip -d scons/
rm scons-local-*.zip
```

Consider updating DeJaVu Fonts: The [last version](http://dejavu-fonts.org/wiki/Download) updated was 2.33

```sh
cd fonts
svn rm dejavu-fonts-ttf-
wget http://sourceforge.net/projects/dejavu/files/dejavu/2.33/dejavu-fonts-ttf-2.33.tar.bz2
tar xvf dejavu-fonts-ttf-2.33.tar.bz2
svn add dejavu-fonts-ttf-2.33
```
    
Check for new [unifont release](http://unifoundry.com/unifont.html)

### Release candidate

Consider first promoting a release candidate tag:

```sh
git tag -a v3.0.0-rc1 -m 'Release Candidate 1 for Mapnik v3.0.0'
git push --tags
```

### Pre-tag updates

  * Update version number in [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp)
  * Set `MAPNIK_VERSION_IS_RELEASE` to 1 in [version.hpp](https://github.com/mapnik/mapnik/blob/master/include/mapnik/version.hpp)

```
make uninstall && ./configure && make
MAPNIK_VERSION=`./utils/mapnik-config/mapnik-config --version`
git commit -a -m "setting up for mapnik v${MAPNIK_VERSION} release" 
git push
```

  * Update CHANGELOG with the git hash of latest commit using the output of:

```
git describe # take hash after 'g'
```

  * Then, push change:

```
git commit -a -m "update CHANGELOG for mapnik v${MAPNIK_VERSION} release"
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
git submodule init
git submodule update
rm -rf test/data/.git
rm -rf test/data/.gitignore
rm -rf test/data-visual/.git
rm -rf test/data-visual/.gitignore
rm -rf .git
rm -rf .gitignore
cd ../
tar cjf ${TARBALL_NAME}.tar.bz2 ${TARBALL_NAME}/
# upload to s3
aws s3 cp --acl public-read ${TARBALL_NAME}.tar.bz2 s3://mapnik/dist/v${MAPNIK_VERSION}/
```


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

* Create a new `mapnik-reference` entry for the release: https://github.com/mapnik/mapnik-reference

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
* Upload Mac/Win binary packages to the s3 bucket: <http://mapnik.s3.amazonaws.com/dist/>
* Submit pull request for homebrew formula: <https://github.com/mxcl/homebrew/blob/master/Library/Formula/mapnik.rb>
    
### Wiki Post-Release

* Add https://github.com/mapnik/mapnik/wiki/Release${VERSION} (needed by ubuntu packages)
* Update [[Mapnik-Installation]], [MacInstallation](MacInstallation), [LinuxInstallation](https://github.com/mapnik/mapnik/wiki/LinuxInstallation) and [WindowsInstallation](WindowsInstallation) links
* Create a release page from the relevant section of CHANGELOG like this page [Release0.7.1](Release0.7.1)
* Update [MapnikReleases](MapnikReleases), a starting page for users to learn about Mapnik development
    
### Announce
    
* Mapnik users list
* Mapnik news twitter account: http://twitter.com/mapnikproject
* OpenStreetMap : [OSM-Dev]
* Notify Packagers for Linux distros ([PackageBuilding](PackageBuilding))
* Notify Packagers for OSGEO4w: http://norbit.de/