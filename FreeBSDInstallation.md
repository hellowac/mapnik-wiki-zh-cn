<!-- Name: FreeBSDInstallation -->
<!-- Version: 3 -->
<!-- Last-Modified: 2010/11/23 09:40:38 -->
<!-- Author: bcrosby -->
## Installing on FreeBSD

In most cases the FreeBSD port of Mapnik (located in /usr/ports/graphics/mapnik) will work. However, if the port is broken, or you'd like to install another version the following instructions will help.

You will need to install the following ports/packages to ensure that mapnik will compile for you:



    graphics/png
    graphics/tiff
    graphics/jpeg
    graphics/proj
    devel/icu
    print/freetype2
    graphics/cairo
    graphics/cairomm
    devel/pkg-config
    graphics/py-cairo
    devel/boost-python-libs
    devel/libtool22
    devel/libltdl22

If you want postgres support, ensure that the postgres libs are installed:


    database/postgresqlXX-client (where XX is the version of Postgres libs you'd like to install)

Once these libs are installed, you should be able to compile/install source by doing:


    python scons/scons.py configure
    python scons/scons.py install
