<!-- Name: MacInstallationPorts -->
<!-- Version: 10 -->
<!-- Last-Modified: 2009/11/05 11:15:11 -->
<!-- Author: springmeyer -->
# Installing Mapnik on Mac OS X

This page describes how to build/install Mapnik from source on Mac OS X >= 10.5, using Macports. 

Unlike the MacInstallation guide, this page assumes you grok [the command-line](http://en.wikipedia.org/wiki/In_the_Beginning...was_the_Command_Line).

## Dependencies

 * Install [MacPorts](http://www.macports.org/): http://www.macports.org/install.php (requires XCode. Version 1.6 may not set up a .profile, see [ProblemHotlist](https://trac.macports.org/wiki/ProblemHotlist#a4..profilenotsetup) to fix)

Run


```sh
    $ sudo port install proj libpng jpeg tiff icu jam
    $ sudo port install boost +python25 +icu
```

For optional dependencies (such as Cairo or PostGIS), see MacInstallation/Optional (MacInstallation_Optional)

## Building

Grab source:


```sh
    $ git clone https://github.com/mapnik/mapnik.git
```

Patch [SConstruct](http://www.scons.org/doc/1.0.1/HTML/scons-user/x348.html) (get [SConstruct.osx.patch](http://trac.mapnik.org/attachment/wiki/MacInstallationPorts/SConstruct.osx.patch), [download here](http://trac.mapnik.org/raw-attachment/wiki/MacInstallationPorts/SConstruct.osx.patch))


```sh
    $ patch -p1 < SConstruct.osx.patch
```

Compile/Install


```sh
    $ cd mapnik
    $ python scons/scons.py DEBUG=y
    $ sudo python scons/scons.py install DEBUG=y
```

Add the following line to your ~/.profile

```sh
    export PYTHONPATH="/usr/lib/python2.5/site-packages"
```

## Testing

```sh
    $ python
    >>> import mapnik
    registered datasource : gdal
    registered datasource : postgis
    registered datasource : raster
    registered datasource : shape
    >>> dir(mapnik) # This gets you a list of symbols
    ['BoostPythonMetaclass', 'Color', 'Coord', 'CreateDatasource', ...]
    >>> help(mapnik)
```

## References

 * [The Official Mapnik installation guide](http://mapnik.org/documentation/install/)
 * Conventional MacInstallation guide
 * http://www.codingadventures.com/2008/04/howto-building-mapnik-on-osx-leopard/


 