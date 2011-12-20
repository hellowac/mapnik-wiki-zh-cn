<!-- Name: WindowsInstallation -->
<!-- Version: 36 -->
<!-- Last-Modified: 2011/06/09 09:06:43 -->
<!-- Author: springmeyer -->


# Installing Mapnik in Windows

Mapnik binaries can be installed and configured manually, or installed using OSGEO4W. The instructions below highlight these options.

If you are interested in installing Mapnik on other operating systems see: MapnikInstallation

If you an interested in compiling Mapnik from source on windows see the windows scripts at https://github.com/mapnik/mapnik-packaging


## Supported Features

The Windows builds have a slightly less complete feature set than is possible from source builds. Full support is planned, and this table tracks the versions in which new features are added:

| *Mapnik Feature*                |    *0.5.0*  |  *0.5.1*  |     *0.6.0* | *0.6.1*   | *0.7.0*   | *0.7.1* |
|:--------------------------------|-------------|-----------|-------------|-----------|-----------|--------:|
| Cairo Rendering                    | -                 | -               | -                | -               | -               | -              |
| ICU Unicode Support            | -                  | -               |  ***          |  ***         |  ***         | ***          |
| Python 2.5 Support               |  ***           |  ***         |  ***           |  ***         |  ***         | ***         |
| Python 2.6 Support               | -                 | -               | -                | -               |  ***         | ***         |
| Libxml2 Parser Support        | -                 | -               | -                | ***          |  ***         | ***         |
| Shapefile Plugin                     |  ***            |  ***         |  ***          |  ***          |  ***         | ***         |
| Raster Plugin                          |  ***            |  ***         |  ***          |  ***          |  ***         | ***         |
| PostGIS Plugin                        |  ***            |  ***         |  ***          |  ***          |  ***         | ***         |
| GDAL Plugin                           | -                  | -               |  ***          |  ***          |  ***         | ***         |
| OGR Plugin                             | -                  | -               | -                | ***          |  ***         | ***         |
| SQLite Plugin                          | -                  | -               |  ***          |  ***          |  ***         | ***         |
| OSM Plugin                             | -                  | -               | -                | -               | -               | -              |
| shapeindex.exe                     | -                  | ***           |  ***          |  ***          |  ***         | ***         |
| pgsql2sqlite.exe                   | -                  | -                |  ***          |  ***          |  ***         | ***         |

 * - : not available
 * ***: available

* Note: as of Mapnik 0.6.1 memory-mapped files are disabled in the Shapefile Plugin in windows builds (see #342)


# OSGEO4W 0.7.0 Install

1) Download OSGEO4W installer: http://trac.osgeo.org/osgeo4w/

2) Select 'Advanced Install'

3) Choose the Mapnik Python package under '''Libs > mapnik: mapnik python bindings""" which will install both mapnik.dll and the python bindings.

4) Once OSGEO4W finishes installing you should be able to use the OSGEO4W shell to test:


```python
    >>> import mapnik
```

  * Note: this mapnik version will only be available under default settings from the OSGEO4W shell, and other previously installed versions should be disabled through editing your 'PATH' and 'PYTHONPATH' system variables


# Manual Install 0.7.1

To download and manually configure the Mapnik 0.7.1, please follow the instructions below.

## Prerequisites

 * Windows XP or Vista (not yet tested in Windows 7)
 * Python 2.5 or Python 2.6 - [python.org](http://www.python.org)
 * [Mapnik 0.7.1 Binary Files](http://prdownload.berlios.de/mapnik/mapnik-0.7.1-win32-py25_26.zip) ([Alt link](http://download.berlios.de/mapnik/mapnik-0.7.1-win32-py25_26.zip))
 * [PROJ4 binary files](http://download.osgeo.org/proj/proj446_win32_bin.zip), if you are planning to use the OGC WMS server or wish to specify projections using EPSG codes

## Overview

This Guide will walk you through installing Mapnik and then running a test script to generate the sample map below:

[[/images/demo.png]]

## Manual Instructions

 1. Download the Mapnik binary

 2. Place the unzipped folder into *"C:\mapnik-0.7.1\"*
   a. open the `python\VERSION\site-packages\mapnik\paths.py` file and confirm that the 'mapniklibpath' points to 'C:/mapnik-0.7.1/lib/mapnik'
   b. do this for whichever python version you want to use, or both.
 
 3. Set your system and/or users environment variables:
  * Hint: _Control Panel->System->Advanced->Environment Variables_
   a.  add *"C:\mapnik-0.7.1\lib"* to the `PATH` variable.
    * Note: you may also need to set your user path environment variable.
    * If the variable `PATH` is not already present, add it.
    * Setting this correctly allows the Mapnik python bindings to find the `mapnik.dll`
   b. for PYTHON support add:
    * PYTHON 2.5:   '''"C:\mapnik-0.7.1\python\2.5\site-packages"''' to the `PYTHONPATH` variable.
    * PYTHON 2.6:   '''"C:\mapnik-0.7.1\python\2.6\site-packages"''' to the `PYTHONPATH` variable.
    * Setting this correctly allows Python to find the Mapnik python bindings when you do `>>> import mapnik`

 4. Open a new console by running "cmd" to test settings:
  * Type "path" to make sure your PATH contains *"C:\mapnik-0.7.1\lib"*

 5. Run "C:\Python25\python.exe" , then type at a python prompt:

```python
    from mapnik import *
```

  * If you get no error message, you made it!
  * If you do get an error message, see *Troubleshooting* below
 
 6. open explorer, go to *"C:\mapnik-0.7.1\demo\python"*, double click `rundemo.py`
  * you should see several demo.* files output.

 7. If you run into errors, confirm that you've added the right paths to your environment.
  * Post further errors to the mailing list for assistance.

 8. Head over to GettingStarted for your first tutorial on the Mapnik Python API.




# Manual Install 0.6.1

To download and manually configure the Mapnik 0.6.1, please follow the instructions below.

## Prerequisites

 * Windows XP or Vista (not yet tested in Windows 7)
 * Python 2.5 - [python.org](http://www.python.org)
  * If you'd like to see support for Python 2.6 let us know by sending a note to the mailing list
 * [Mapnik 0.6.1 Binary Files](http://prdownload.berlios.de/mapnik/mapnik-0.6.1-win32-py25.zip) ([Alternate download link](http://media.mapnik.org/mapnik_0.6.1-win32_py25.zip))
 * [PROJ4 binary files](http://download.osgeo.org/proj/proj446_win32_bin.zip), if you are planning to use the OGC WMS server or wish to specify projections using EPSG codes
  * For installation information see the *readme.txt* in the zip download


## Overview

 This Guide will walk you through installing Mapnik and then running a test script to generate the sample map below:

[[/images/demo.png]]

## Manual Instructions

 1. Download the Mapnik binary

 2. Place the unzipped folder into *"C:\mapnik_0_6_1\"*
 
 3. Set your system and/or users environment variables:
  * Hint: _Control Panel->System->Advanced->Environment Variables_
   a.  add *"c:\mapnik_0_6_1\lib"* to the `PATH` variable.
    * Note: you may also need to set your user path environment variable.
    * If the variable `PATH` is not already present, add it.
    * Setting this correctly allows the Mapnik python bindings to find the `mapnik.dll`
   b. add *"c:\mapnik_0_6_1\site-packages"* to the `PYTHONPATH` variable.
    * Setting this correctly allows Python to find the Mapnik python bindings

 4. Open a new console by running "cmd" to test settings:
  * Type "path" to make sure your PATH contains *"c:\mapnik_0_6_1\lib"*

 5. Run "C:\Python25\python.exe" , then type at a python prompt:

```python
    from mapnik import *
```

  * If you get no error message, you made it!
  * If you do get an error message, see *Troubleshooting* below
 
 6. open explorer, go to *"c:\mapnik_0_6_1\demo\python"*, double click `rundemo.py`
  * you should see several demo.* files output.  (The demo folder is currently missing from the
    Windows  0_6_1 package but can be found in the 0_6_0 Windows package or the 0_6_1 linux package.) 

 7. If you run into errors, confirm that you've installed Boost and added the right paths to your environment.
  * Post further errors to the mailing list for assistance.

 8. Head over to GettingStarted for your first tutorial on the Mapnik Python API.

## Trouble Shooting

### Mapnik DLL not found

You get an error like:

    Can't find mapnik.dll

Solution: make sure that you complete *Step 3.a* properly.


### Mapnik Python not found

Problem: When importing mapnik in python you get:

```python
    >>> import mapnik
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: No module named mapnik
```

Solution: make sure that you have put the 'site-packages' folder on your PYTHONPATH by completing *Step 3.b.*

### Unknown (Windows) Dependency not found

Problem: When importing mapnik in python you get:

```python
    >>> import mapnik
    [...snip...]
    from _mapnik import *
    ImportError: DLL load failed: This application has failed to start because the application configuration is incorrect. Reinstalling the application may fix this problem.
```

Solution:
 * You likely have an older system and need to install the 2008 Visual Studio Runtime Libraries (msvcrt90.dll) from the [Microsoft Developer Network](http://www.microsoft.com/downloads/details.aspx?familyid=9B2DA534-3E03-4391-8A4D-074B9F2BC1BF&displaylang=en). If that does not fix it you may also be missing the [2005 version](http://www.microsoft.com/downloads/details.aspx?familyid=32BC1BEE-A3F9-4C13-9C99-220B62A191EE&displaylang=en)
 * This problem may also occur on a freshly installed system that is missing some dependecies or has an incompatible version of some DLLs. In my case I had to install the MSVC dependencies (vcredist_x86.exe) and additionally put a downloaded msvcr90.dll into the mapnik/lib folder.
 * You can get more information on what is missing or incompatible by examining mapnik.dll with [Dependency Walker](http://www.dependencywalker.com/). On a 64bit system you must use the 32bit Version.

## Previous Releases

[Mapnik Win32 0.5.0](http://prdownload.berlios.de/mapnik/mapnik_win32_py25-0.5.1.zip)
