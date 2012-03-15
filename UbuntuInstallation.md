# Installing Mapnik on Ubuntu

For all versions of Ubuntu it is a good idea to be fully up to date before starting:

```sh
    sudo apt-get update
    sudo apt-get upgrade
```

For previous versions see the archived notes at [[UbuntuInstallationOld]]

----

# Ubuntu Oneiric (11.10)

## Install from packages

**For nightly builds from master (2.x)**

```sh
    sudo add-apt-repository ppa:mapnik/nightly-trunk
    sudo apt-get update
    sudo apt-get install libmapnik mapnik-utils python-mapnik
```
**For v2.0.x version**

```sh
    sudo add-apt-repository ppa:mapnik/nightly-2.0
    sudo apt-get update
    sudo apt-get install libmapnik mapnik-utils python-mapnik
```

**For v0.7.2 version**

```sh
    sudo add-apt-repository ppa:mapnik/nightly-0.7
    sudo apt-get update
    sudo apt-get install libmapnik mapnik-utils python-mapnik
```

## Install Mapnik from source

First, remove any apt installing packages:

```sh
    sudo apt-get remove libmapnik* mapnik-utils python-mapnik
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