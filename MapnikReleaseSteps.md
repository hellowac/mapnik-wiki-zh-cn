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
git rm -r dejavu-fonts-ttf-
wget http://sourceforge.net/projects/dejavu/files/dejavu/2.33/dejavu-fonts-ttf-2.33.tar.bz2
tar xvf dejavu-fonts-ttf-2.33.tar.bz2
git add dejavu-fonts-ttf-2.33
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

* Create and upload clean tarball:

Before running this you'll need:

 - The submodules update to date (otherwise the --depth 1 will fail) (TODO: use branches or tags for submodules?)
 - Ability to post to s3://mapnik/dist/. Test like `aws s3 ls s3://mapnik/dist/`

```sh
make release
```

* Test the uploaded tarball:

```sh
cd /tmp
rm -rf mapnik-v${MAPNIK_VERSION}.tar.bz2
wget https://mapnik.s3.amazonaws.com/dist/v${MAPNIK_VERSION}/mapnik-v${MAPNIK_VERSION}.tar.bz2
tar xf mapnik-v${MAPNIK_VERSION}.tar.bz2
cd mapnik-v${MAPNIK_VERSION}
source bootstrap.sh
./configure && make && make test
```

* CURRENTLY NOT WORKING (https://github.com/mapnik/mapnik/pull/2906): Go back to the mapnik source checkout and generate Python API docs:

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

1) Submit pull request for homebrew formula

 - Fork homebrew
 - Edit https://github.com/mxcl/homebrew/blob/master/Library/Formula/mapnik.rb
 - Change the version
 - Run `brew install mapnik`, will fail on `sha256` check
 - grab expected `sha256` from error message, edit `mapnik.rb`
 - test building `brew install mapnik`
 - submit pull request - learning from older ones like https://github.com/Homebrew/homebrew/pull/41474
   
2) Package binaries for Ubuntu Linux (PPA)

 - Scripts are at https://github.com/mapnik/debian
 - Create a new version by copying `master` scripts (or appropriate dir)
 - Add an entry for the new version to https://github.com/mapnik/debian/blob/master/nightly-build.sh
 - The `nighly-build.sh` is run on a cron by robert.coup@koordinates.com (@rcoup) - TODO - should we move this to travis?

3) Upload Mac/Win binary packages to the s3 bucket: <http://mapnik.s3.amazonaws.com/dist/>

TODO - currently do not have bandwidth or set process for this. For Mac: In the past @springmeyer created mac easy installer but just recommending homebrew is better now (since they support binaries/bottles). For Windows: https://github.com/mapbox/windows-builds is used to create SDK's but we've not yet formalized document how these can be used (those they are viable).

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