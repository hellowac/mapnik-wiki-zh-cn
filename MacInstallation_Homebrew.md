<!-- Name: MacInstallation/Homebrew -->
<!-- Version: 6 -->
<!-- Last-Modified: 2011/05/20 14:50:02 -->
<!-- Author: springmeyer -->

# Installing Mapnik on OS X with Homebrew


## Install Homebrew
Install homebrew as per: http://github.com/mxcl/homebrew/wiki/installation

Basically do:

    #!sh
    curl -Lsf http://github.com/mxcl/homebrew/tarball/master | tar xz --strip 1 -C/usr/local
    brew install git
    git clone http://github.com/mxcl/homebrew.git /tmp/homebrew
    mv /tmp/homebrew/.git /usr/local/
    rm -rf /tmp/homebrew

Yes, feel free to chmod /usr/local like:


    sudo chown -R $USER /usr/local

*But be aware:* running chmod on /usr/local will break things like postgres installed via Kyngchaos in `/usr/local/pgsql`. You will see:

    psql: could not connect to server: Connection refused
    	Is the server running locally and accepting
    	connections on Unix domain socket "/tmp/.s.PGSQL.5432"?

This can be fixed by simply re-installing postgres (which will fix permissions) from: http://www.kyngchaos.com/software/postgres

## Installing Mapnik 0.7.x via Homebrew

Simply type:


    #!sh
    brew install mapnik

Be aware that this will take a long time - hours maybe. The main reason is that homebrew installs *many* boost libraries that mapnik does not need and mapnik will not start building until boost is done.

## Installing Mapnik 2.0 via Homebrew

Homebrew only provides mapnik 0.7.x currently, so to install mapnik2 we need to create a new "formula".

Assuming that your homebrew installation is standard and in `/usr/local/Library' then just do this:


    #!sh
    wget https://gist.github.com/raw/983887/mapnik2.rb -O /usr/local/Library/Formula/mapnik2.rb

Then do:


    #!sh
    brew install mapnik2

Or you could copy the mapnik2.rb formula and apply a simple patch to it:


    #!diff
    diff --git a/Library/Formula/mapnik.rb b/Library/Formula/mapnik.rb
    index 04be7b7..e160920 100644
    --- a/Library/Formula/mapnik.rb
    +++ b/Library/Formula/mapnik.rb
    @@ -1,7 +1,7 @@
     require 'formula'
     
    -class Mapnik < Formula
    -  url 'http://download.berlios.de/mapnik/mapnik-0.7.1.tar.gz'
    +class Mapnik2 < Formula
    +  head 'http://svn.mapnik.org/trunk/', :using => :svn
       homepage 'http://www.mapnik.org/'
       md5 '3a070fdd7c6a3367ad78d95c2387b03b'
     
    @@ -17,11 +17,6 @@ class Mapnik < Formula
       def install
         ENV.x11 # for freetype-config
     
    -    # Allow compilation against boost 1.46
    -    inreplace ["src/datasource_cache.cpp", "src/libxml2_loader.cpp", "src/load_map.cpp", "
    -      "#include <boost/filesystem/operations.hpp>",
    -      "#define BOOST_FILESYSTEM_VERSION 2\n#include <boost/filesystem/operations.hpp>"
    -
         icu = Formula.factory("icu4c")
         system "scons",
             "PREFIX=#{prefix}",
