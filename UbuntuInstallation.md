<!-- Name: UbuntuInstallation -->
<!-- Version: 57 -->
<!-- Last-Modified: 2010/10/12 16:08:23 -->
<!-- Author: springmeyer -->


# Installing Mapnik on Ubuntu
For all versions of Ubuntu make sure you are up to date before starting to install:


```sh
    sudo apt-get update
    sudo apt-get upgrade
```

For previous versions see the archived notes at [[UbuntuInstallationOld]]

----

# Ubuntu Maverick (10.10)

This release has Mapnik packages for 0.7.1 (to check run `apt-cache show libmapnik*`), so you can either install Mapnik from packages or source.

 * Packages are available in the 'universe' repositories so make sure your `/etc/apt/sources.list` has the below lines (or similar):

```
    deb http://us.archive.ubuntu.com/ubuntu/ maverick universe
    deb http://us.archive.ubuntu.com/ubuntu/ maverick-updates universe
```

## Install from packages

```sh
    sudo apt-get install libmapnik0.7 mapnik-utils python-mapnik
```

*Note:* then you will likely also want to install Postgres + PostGIS (see below)

## Install Mapnik from source

First, remove any apt installing packages:

```sh
    sudo apt-get remove libmapnik* mapnik-utils python-mapnik
```

### Set up build environment

```sh
    # get a build environment going...
    sudo apt-get install -y g++ cpp \
    libboost-filesystem1.42-dev \
    libboost-iostreams1.42-dev libboost-program-options1.42-dev \
    libboost-python1.42-dev libboost-regex1.42-dev \
    libboost-system1.42-dev libboost-thread1.42-dev \
    python-dev libxml2 libxml2-dev \
    libfreetype6 libfreetype6-dev \
    libjpeg62 libjpeg62-dev \
    libltdl7 libltdl-dev \
    libpng12-0 libpng12-dev \
    libgeotiff-dev libtiff4 libtiff4-dev libtiffxx0c2 \
    libcairo2 libcairo2-dev python-cairo python-cairo-dev \
    libcairomm-1.0-1 libcairomm-1.0-dev \
    ttf-unifont ttf-dejavu ttf-dejavu-core ttf-dejavu-extra \
    subversion build-essential python-nose
    
    # install plugin dependencies
    sudo apt-get install libgdal1-dev python-gdal \
    postgresql-8.4 postgresql-server-dev-8.4 postgresql-contrib-8.4 postgresql-8.4-postgis \
    libsqlite3-dev
```

### Then compile and install Mapnik

For instructions on compiling trunk (aka Mapnik2) see [[Mapnik2]]

```sh
    svn co http://svn.mapnik.org/tags/release-0.7.1/ mapnik-0.7.1
    cd mapnik-0.7.1
    python scons/scons.py configure INPUT_PLUGINS=all OPTIMIZATION=3 SYSTEM_FONTS=/usr/share/fonts/
    python scons/scons.py
    sudo python scons/scons.py install
```

Then run:

```sh
    $ sudo ldconfig
```

To test mapnik:

```python
    $ Python
    >>> import mapnik
    >>>
```

 * No output is good. 

Then run the full test suite

```sh
    cd mapnik-0.7.1
    python tests/run_tests.py
```

If you are interested what libraries mapnik linked against do (for example):

```sh
    ldd /usr/lib/python2.6/site-packages/mapnik/_mapnik.so | grep boost
```