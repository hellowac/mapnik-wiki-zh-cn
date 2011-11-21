<!-- Name: BuildingOnWindows -->
<!-- Version: 1 -->
<!-- Last-Modified: 2011/02/23 14:19:34 -->
<!-- Author: roel_v -->
To build mapnik on Windows with Visual Studio you need experience with Visual Studio and C++ development experience in general. Mapnik has a relatively large list of dependencies. I've tried to automate a large part of the process with the batch file below. I've only tested with the versions of the libraries listed below. Boost is not included here, it needs to be build separately.

This build includes all libraries statically. That way you can make one self-contained binary.

To build under MSVC, you need to patch the code a bit (as of mapnik 0.7.1). Search the trac for patches by me (roel_v), there are 4 of them.

For the libraries where no build system is available out of the box, you can download the project files from the mapnik php extension at https://github.com/roel-v/php_mapnik .

This setup assumes a directory structure where all libraries are stored under a 'thirdparty' directory, where the .lib files will be copied to.

Working as of Januari 2011. Don't just blindly copy and paste, it's more a recipe for the steps to take than an actual working script. You still need to follow the instructions in the comments.




    @echo off
    
    rem Script to build all prereq libraries for mapnik on Windows
    rem using msvc, with as little external dependencies as possible.
    rem For all these libraries, build the static version.
    
    "c:\program files\microsoft visual Studio\vc\bin\vcvars32.bat"
    
    cd thirdparty
    
    rem zlib - www.zlib.org, 1.2.5
    rem Uses standard makefile, build with nmake
    rem Add to win32/Makefile.msc: LOC = -DGAS_COFF
    rem Output: zlib.lib
    cd zlib-1.2.5
    nmake -f win32/Makefile.msc zlib.lib
    copy zlib.lib ..
    cd ..
    
    rem freetype
    rem Uses arcane Makefile (not sure what format) or jam. PITA
    rem to get working, use own project. Check docs\INSTALL.ANY
    rem because for some reason some files cannot be included in
    rem the build.
    rem Output: freetype.lib
    cd freetype-2.4.4
    copy ..\..\vs_project\Debug\freetype.lib ..
    cd ..
    
    rem icu
    rem Uses autotools or MSVC 10 project files. Use own project.
    rem Output: icu.lib
    cd icu\source
    
    cd data
    nmake -f makedata.mak ICUMAKE="C: \tmp\mapnik-0.7.1\thirdparty\icu\source\data"
    cd ..
    
    copy ..\..\..\vs_project\Debug\icu.lib ..\..
    cd ..\..
    
    rem libjpeg
    rem Makefile-based, provides VC version.
    rem Output: libjpeg.lib
    cd jpeg-8b
    copy jconfig.vc jconfig.h
    nmake -f makefile.vc
    copy libjpeg.lib ..
    cd ..
    
    rem libxml2
    rem Used an autotool emulation file based on cscript.
    rem Note that it seems to have a bug, and the Makefile.msvc needs to
    rem be edited to remove a + from some lines.
    rem Output: bin.msvc\libxml2_a.lib
    cd libxml2-2.7.8
    cd win32
    cscript configure.js zlib=yes icu=yes debug=yes static=yes iconv=no include=..\..\icu\source\common;..\..\zlib-1.2.5
    nmake -f Makefile.msvc libxmla
    copy bin.msvc\libxml2_a.lib ..\..
    cd ..
    cd ..
    
    rem libpng
    rem Uses hardcoded zlib header path in makefile.vcwin32, edit as needed
    rem Output: libpng.lib
    cd lpng145
    nmake -f scripts/makefile.vcwin32 libpng.lib
    copy libpng.lib ..
    cd ..
    
    rem proj4
    rem Make-based system
    rem Output: proj.lib
    cd proj-4.7.0
    nmake -f makefile.vc
    copy src\proj.lib ..
    cd ..
    
    rem libtiff
    rem Make based
    rem Output:
    cd tiff-3.9.4
    nmake -f Makefile.vc
    copy libtiff\libtiff.lib ..
    cd..
    
    rem Back into root directory
    cd ..
    
