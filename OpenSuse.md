<!-- Name: OpenSuse -->
<!-- Version: 4 -->
<!-- Last-Modified: 2010/02/06 16:38:24 -->
<!-- Author: TomasC -->
These instructions are verified on a clean Opensuse 11.2 install.

First, add the Geo repository:

    sudo zypper ar http://download.opensuse.org/repositories/Application:/Geo/openSUSE_11.2/ "Geo"
    sudo zypper refresh

To download and build Mapnik, you first need to install quite a bit of dependencies and tools:

    sudo zypper install subversion make gcc gcc-c++ libxml2-devel postgresql-devel libgeos-devel libbz2-devel libproj-devel libjpeg-devel libtiff-devel libpng-devel boost-devel python-cairo-devel cairomm-devel libicu-devel libtool

Use Subversion to fetch the latest stable version of Mapnik. At the time of writing, that was 0.7.0.

    svn export http://svn.mapnik.org/tags/release-0.7.0 mapnik-0.7.0

Build the Mapnik Python module. In the second line, you can omit everything after "scons.py" if you do not want to optimize the build or want to run the build on other machines.

    cd mapnik-0.7.0/
    python scons/scons.py CXX="g++ -march=native -O2 -fomit-frame-pointer" configure
    python scons/scons.py
    sudo python scons/scons.py install
    sudo ldconfig