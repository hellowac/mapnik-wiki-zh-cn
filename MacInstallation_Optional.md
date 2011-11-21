<!-- Name: MacInstallation/Optional -->
<!-- Version: 10 -->
<!-- Last-Modified: 2009/10/12 16:43:17 -->
<!-- Author: springmeyer -->
# Optional Installs

  * The $ indicates a normal command prompt in the shell.
  * The # indicates a command that likely needs to be run by a superuser.
  * The ## indicates code comments that are not executed. 

You may install Proj.4, PostgreSQL/PostGIS, and GDAL if needed.

 * *Proj.4 and Datum data* from source

    $ wget ftp://ftp.remotesensing.org/proj/proj-4.6.1.tar.gz
    $ wget ftp://ftp.remotesensing.org/proj/proj-datumgrid-1.4.tar.gz
 * Extract the datum files into the main source code and build:

    $ tar xzf proj-4.6.1.tar.gz
    $ cd proj-4.6.1/nad
    $ tar xzf ../../proj-datumgrid-1.4.tar.gz
    $ cd ../
    $ ./configure
    $ make
    # make install 
    $ cd ../

 * *PostgreSQL and PostGIS* binaries - use [kyngchaos.com](http://www.kyngchaos.com/wiki/software:postgres) or from source:
  * You can build PostgreSQL from source just like any other linux/unix system - [Postgres Docs](http://www.postgresql.org/docs/8.3/interactive/install-procedure.html)
  * Next build PostGIS source (Install GEOS first if you wish to use Spatial Operations in Postgis separately - [http://code.djangoproject.com/wiki/GeoDjangoInstall#GEOS])

    $ wget http://postgis.refractions.net/download/postgis-1.3.4.tar.gz
    $ tar xzf postgis-1.3.4.tar.gz
    $ cd postgis-1.3.4
    $ ./configure --with-geos --with-proj # these flags are recommend but not needed for Mapnik
    $ make
    # make install

  * Alternatively, you may install PostgreSQL and PostGIS using MacPorts. First, run

    $ sudo port install postgresql83
    $ sudo port install postgis
  * Next, modify the SConstruct file to point to the libraries and header files installed by port. Change the lines that list PGSQL to:

    opts.Add(PathOption('PGSQL_INCLUDES', 'Search path for PostgreSQL include files', '/opt/local/include/postgresql83'))
    opts.Add(PathOption('PGSQL_LIBS', 'Search path for PostgreSQL library files', '/opt/local/lib/postgresql83'))
  * See [wiki:MacPostGIS_Setup] for setup instructions.
 * *GDAL* binary frameworks - use [kyngchaos.com](http://www.kyngchaos.com/wiki/software:frameworks) or build from source:

    $ wget http://download.osgeo.org/gdal/gdal-1.5.0.tar.gz
    $ tar xzf gdal-1.5.0.tar.gz
    $ cd gdal-1.5.0
    $ ./configure # --with-package (lots of available options here to support various raster formats)
    $ make
    # make install

### Install WMS dependencies

Install the Mapnik WMS dependencies if you wish to use the WMS (Web Mapping Service) server (Otherwise optional).

 * More details in the [source:trunk/docs/ogcserver/readme.txt WMS Readme] in SVN

    wget ftp://xmlsoft.org/libxml2/libxml2-2.7.6.tar.gz
    tar xvf libxml2-2.7.6.tar.gz
    cd libxml2-2.7.6
    ./configure
    make
    sudo make install
    
    cd ../
    
    wget ftp://xmlsoft.org/libxml2/libxslt-1.1.26.tar.gz
    tar xvf libxslt-1.1.26.tar.gz
    cd libxslt-1.1.26
    ./configure
    make
    sudo make install


    # easy_install lxml

    $ tar xzvf Imaging-1.1.6.tar.gz 
    $ cd Imaging-1.1.6
    # python setup.py install

You'll need either mod_fastcgi or mod_fcgid installed within apache.
 * FastCGI install notes are here: http://blog.cleverelephant.ca/2008/05/fastcgi-on-osx-leopard.html
 * Fcgid install notes are here: http://blog.brandonking.net//2008/01/django-app-modfcgid-apache-2-setup-on.html/
 * TODO FastCGI/mod_fcgi example installation
 * TODO PostGIS from kyngchaos setup instructions for mapnik 

