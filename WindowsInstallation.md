# Installing Mapnik in Windows

Mapnik binaries can be installed and configured manually on windows. See http://mapnik.org/download/ for the latest download and instructions on installing.

If you are interested in installing Mapnik on other operating systems see [[Mapnik-Installation]]

If you an interested in compiling Mapnik from source on windows see the windows scripts at https://github.com/mapnik/mapnik-packaging

## Supported Features

The Windows builds have a slightly less complete feature set than is possible from source builds. Full support is planned, and this table tracks the versions in which new features are added:

| *Mapnik Feature* |*0.5.0*  |  *0.5.1*  | *0.6.0* | *0.6.1* | *0.7.0* | *0.7.1* | *2.2.0* |
|:-----------------|---------|-----------|---------|---------|---------|---------|--------:|
| Cairo Rendering | -| -| - | -| -| - | *** |
| ICU Unicode Support| - | -|  ***  |  *** |  *** | ***  | *** |
| Python 2.5 Support|  ***   |  *** |  ***   |  *** |  *** | *** | - |
| Python 2.6 Support| -| -| - | -|  *** | *** | - |
| Python 2.7 Support| -| -| - | -|  *** | *** | *** |
| Libxml2 Parser Support| -| -| - | ***  |  *** | *** | *** |
| Shapefile Plugin|  ***|  *** |  ***  |  ***  |  *** | *** | *** |
| Raster Plugin |  ***|  *** |  ***  |  ***  |  *** | *** | *** |
| PostGIS Plugin   |  ***|  *** |  ***  |  ***  |  *** | *** | *** |
| GDAL Plugin  | - | -|  ***  |  ***  |  *** | *** | *** |
| OGR Plugin| - | -| - | ***  |  *** | *** | *** |
| SQLite Plugin | - | -|  ***  |  ***  |  *** | *** | *** |
| GeoJSON Plugin | - | -|  -  |  -  |  - | - | *** |
| CSVJSON Plugin | - | -|  -  |  -  |  - | - | *** |
| OSM Plugin| - | -| - | -| -| -  | -  |
| shapeindex.exe| - | ***   |  ***  |  ***  |  *** | *** | *** |
| pgsql2sqlite.exe  | - | - |  ***  |  ***  |  *** | *** | *** |

 * - : not available
 * ***: available

* Note: as of Mapnik 0.6.1 memory-mapped files are disabled in the Shapefile Plugin in windows builds (see #342)

## Overview

This Guide will walk you through installing Mapnik and then running a test script to generate the sample map below:

[[/images/demo.png]]

## Manual Instructions

 1. Download the Mapnik binary

 2. Place the unzipped folder into *"C:\mapnik-v2.2.0\"*
 
 3. Set your system and/or users environment variables:
  * Hint: _Control Panel->System->Advanced->Environment Variables_
   a.  add *"C:\mapnik-v0.2.2\lib"* to the `PATH` variable.
    * Note: you may also need to set your user path environment variable.
    * If the variable `PATH` is not already present, add it.
    * Setting this correctly allows the Mapnik python bindings to find the `mapnik.dll`
   b. for PYTHON support add:
    * PYTHON 2.7:   '''"C:\mapnik-v2.2.0\python\2.7\site-packages"''' to the `PYTHONPATH` variable.
    * Setting this correctly allows Python to find the Mapnik python bindings when you do `>>> import mapnik`

 4. Open a new console by running "cmd" to test settings:
  * Type "path" to make sure your PATH contains *"C:\mapnik-v2.2.0\lib"*

 5. Run "C:\Python27\python.exe" , then type at a python prompt:

```python
import mapnik
```

  * If you get no error message, you made it!
  * If you do get an error message, see *Troubleshooting* below
 
 6. open explorer, go to *"C:\mapnik-v2.2.0\demo\python"*, double click `rundemo.py`
  * you should see several demo.* files output.

 7. If you run into errors, confirm that you've added the right paths to your environment.
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

