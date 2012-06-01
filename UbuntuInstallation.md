# Installing Mapnik on Ubuntu

For all versions of Ubuntu it is a good idea to be fully up to date before starting:

```sh
sudo apt-get update
sudo apt-get upgrade
```

For older versions see the archived notes at [[UbuntuInstallationOld]]

----

# Ubuntu >= (11.10)

## Install from packages

**For nightly builds from master (2.x)**

This is the bleeding edge - build nightly - directly from https://github.com/mapnik/mapnik/commits/master

```sh
    sudo add-apt-repository ppa:mapnik/nightly-trunk
    sudo apt-get update
    sudo apt-get install libmapnik mapnik-utils python-mapnik
```

These packages come from: https://launchpad.net/~mapnik/+archive/nightly-trunk/+packages

**For v2.0.x version**

This is the stable 2.0.x series, updated whenever there is a commit pushed to the 2.0.x branch (which is only bugfix backports) - the next release in this series is 2.0.1.

```sh
    sudo add-apt-repository ppa:mapnik/nightly-2.0
    sudo apt-get update
    sudo apt-get install libmapnik mapnik-utils python-mapnik
```

These packages come from: https://launchpad.net/~mapnik/+archive/nightly-2.0/+packages

**For v0.7.2 version**

```sh
    sudo add-apt-repository ppa:mapnik/nightly-0.7
    sudo apt-get update
    sudo apt-get install libmapnik mapnik-utils python-mapnik
```

## Install Mapnik from source

First, remove any other old mapnik packages:

```sh
    sudo apt-get purge libmapnik* mapnik-utils python-mapnik
```

### Ensure your boost version is recent enough

Mapnik master may require a boost version more recent than provided by your Ubuntu distribution.

You can use the latest Boost version (that works with Mapnik) by installing Boost from the `mapnik/boost` PPA:

```sh
sudo add-apt-repository ppa:mapnik/boost
sudo apt-get update
sudo apt-get install libboost-dev libboost-filesystem-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-system-dev libboost-thread-dev 
```
Note: You can see the boost version offered by your distro with the below command. And if you are using the above PPA then its version should show up as a candidate for installation:

```sh
apt-cache policy libboost-dev
```

### Set up build environment

```sh
    # get a build environment going...
    sudo apt-get install -y g++ cpp \
    libicu-dev \
    libboost-filesystem-dev \
    libboost-program-options-dev \
    libboost-python-dev libboost-regex-dev \
    libboost-system-dev libboost-thread-dev \
    python-dev libxml2 libxml2-dev \
    libfreetype6 libfreetype6-dev \
    libjpeg-dev \
    libltdl7 libltdl-dev \
    libpng-dev \
    libgeotiff-dev libtiff-dev libtiffxx0c2 \
    libcairo2 libcairo2-dev python-cairo python-cairo-dev \
    libcairomm-1.0-1 libcairomm-1.0-dev \
    ttf-unifont ttf-dejavu ttf-dejavu-core ttf-dejavu-extra \
    git build-essential python-nose
    
    # install plugin dependencies
    sudo apt-get install libgdal1-dev python-gdal \
    postgresql-9.1 postgresql-server-dev-9.1 postgresql-contrib-9.1 postgresql-9.1-postgis \
    libsqlite3-dev
```

### Then compile and install Mapnik

```sh
    git clone http://github.com/mapnik/mapnik
    cd mapnik
    ./configure && make && sudo make install
```

To test mapnik:

```sh
    make test
```