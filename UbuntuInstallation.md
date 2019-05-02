# Installing Mapnik on Ubuntu

For all versions of Ubuntu it is a good idea to be fully up to date before starting:

```sh
sudo apt-get update
sudo apt-get upgrade
```

For older versions, see the archived notes at [[UbuntuInstallationOld]]

## Install Mapnik from source

```
# you might have to update your outdated clang
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo apt-get update -y
sudo apt-get install -y gcc-6 g++-6 clang-3.8
export CXX="clang++-3.8" && export CC="clang-3.8"

# install mapnik
git clone https://github.com/mapnik/mapnik mapnik --depth 10
cd mapnik
git submodule update --init
sudo apt-get install python zlib1g-dev clang make pkg-config curl
source bootstrap.sh
./configure CUSTOM_CXXFLAGS="-D_GLIBCXX_USE_CXX11_ABI=0" CXX=${CXX} CC=${CC}
make
make test
sudo make install

```

NOTE: there used to be a community PPA maintained for Mapnik apt packages (https://launchpad.net/~mapnik/+archive), but it is no longer maintained or in use.

----

## Detailed/historical notes

First, remove any other old mapnik packages:

```sh
sudo apt-get purge libmapnik* mapnik-* python-mapnik
```

### Ensure your boost version is recent enough (at least 1.47)

Mapnik master may require a boost version more recent than provided by your Ubuntu distribution. 

Ubuntu 12.04 Precise ships with 2 different boost versions: 1.46 and 1.48. Make sure you install the correct version.

Note: You can see the boost version offered by your distro with the below command.

```sh
apt-cache policy libboost-dev
```

### Set up build environment

```sh
    # On Ubuntu 12.04 Precise, make sure you get the 1.48 boost packages:
    sudo apt-get install \
    libboost-filesystem1.48-dev \
    libboost-program-options1.48-dev \
    libboost-python1.48-dev libboost-regex1.48-dev \
    libboost-system1.48-dev libboost-thread1.48-dev

    # On on some systems just:
    sudo apt-get install \
    libboost-filesystem-dev \
    libboost-program-options-dev \
    libboost-python-dev libboost-regex-dev \
    libboost-system-dev libboost-thread-dev \

    # get a build environment going...
    sudo apt-get install \
    libicu-dev \
    python-dev libxml2 libxml2-dev \
    libfreetype6 libfreetype6-dev \
    libjpeg-dev \
    libpng-dev \
    libproj-dev \
    libtiff-dev \
    libcairo2-dev python-cairo-dev \
    libcairomm-1.0-dev \
    ttf-unifont ttf-dejavu ttf-dejavu-core ttf-dejavu-extra \
    git build-essential python-nose \
    libgdal-dev python-gdal

    sudo apt-get install -y postgresql-9.1 postgresql-server-dev-9.1 postgresql-contrib-9.1 postgresql-9.1-postgis \
    libsqlite3-dev
```

Note: for Ubuntu >=14.04 postgres/postgis versions have shifted, so do:

```
sudo apt-get install -y postgresql-9.3 postgresql-server-dev-9.3 postgresql-contrib-9.3 postgresql-9.3-postgis-2.1
```

In Ubuntu >=18 :

```
sudo apt install postgresql-server-dev-10 postgresql-10 postgresql-contrib postgresql-10-postgis-scripts
```

### Source install of Mapnik 2.3.x

```sh
# For the development branch:
git clone https://github.com/mapnik/mapnik mapnik-2.3.x -b 2.3.x --depth 10
cd mapnik-2.3.x
./configure && make && sudo make install
```

### Source install of Mapnik Master (3.x)

First download, compile and install harfbuzz
```sh
wget http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-0.9.34.tar.bz2
tar xf harfbuzz-0.9.34.tar.bz2
cd harfbuzz-0.9.34
./configure && make && sudo make install
sudo ldconfig
cd ../
```

Upgrade your compiler to at least g++ 4.7 so it supports c++11 features. <br>`apt-get upgrade` should give you g++-4.8 and gcc-4.8):
```sh
apt-get update
apt-get upgrade
git clone https://github.com/mapnik/mapnik --depth 10
cd mapnik
git submodule update --init deps/mapbox/variant
./configure
make && sudo make install
```

If that doesn't work, here is an example for ubuntu precise to upgrade compilers:

```sh
CLANG_VERSION=3.6
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test;
sudo add-apt-repository "deb http://llvm.org/apt/precise/ llvm-toolchain-precise-${CLANG_VERSION} main";
wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key|sudo apt-key add -
sudo apt-get update -y
sudo apt-get install -y clang-3.6;
export CXX="clang++-3.6" && export CC="clang-3.6";
git clone https://github.com/mapnik/mapnik --depth 10
cd mapnik
./configure CXX=${CXX} CC=${CC}
make && sudo make install
```





### Testing

To test mapnik:

```sh
make test
```