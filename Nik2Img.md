<!-- Name: Nik2Img -->
<!-- Version: 12 -->
<!-- Last-Modified: 2009/10/10 17:37:57 -->
<!-- Author: springmeyer -->

# Mapnik Maps on the Command-Line

*Nik2img* is a _third-party_ program that allows you to easily generate mapnik graphics from Mapnik xml or Cascadenik mml.

 * No python coding is required, only a working Mapnik installation and an XML mapfile.
 * *Nik2img* has a variety of options that make it a useful mapfile debugger.
 * Using *Nik2img* is an easy way to test and develop your xml mapfiles before launching on a server.
 * *Nik2img* should automatically open the rendered map once completed.
 * Like Mapnik, it should run on both Mac, Linux, and Windows

To Install:
 * Download from http://code.google.com/p/mapnik-utils/
 * Or use easy_install:

    $ sudo easy_install -U nik2img

*Note:* These instructions are for the nik2img 0.3.0 release or above.

[[/images/states.png]]

### If you want to render your XML mapfile just do:


    #!python
    $ nik2img.py your_mapfile.xml your_map_rendered.png
 * ,,*Note*: The nik2img.py default output is a 600,300 pixel png, rendered at the maximum extent of all your layers

### And say you want to see your map reprojected ('--srs') to [Google Spherical Mercator](http://spatialreference.org/ref/user/6/), use the url (or an epsg:code):

    #!python
    $ nik2img.py map.xml map.png --srs http://spatialreference.org/ref/user/6/
 * ,,*Note*: the above projection can also be called with '--srs 900913',,

### Or you want to test all the output formats ('-f all') of Mapnik's AGG and Cairo renderers and see Verbose debugging output ('-v'):


    #!python
    $ nik2img.py map.xml maps/ -f all -v

### Or you want to run in 'Dry Run' mode('-n') and output no maps, but step through each part of the rendering process using 2 second pauses ('--pause') at each step to watch the progress, and finally set a python debugger trace ('--trace-steps') at step 5 to enter interactive mode:

Well, admit you are _crazy_, but do it like:


    #!python
    $ nik2img.py map.xml maps -n --pause 2 --trace-step 5 # in this case the pdb_trace() is set immediately following load_map()
 * ,,*Note*: The python debugger tool emulates your map being loaded and rendered by a custom python script within the python interpreter, allowing you to play around and learn the Mapnik python bindings like:,,
 
    #!python
    STEP: 5 // --> BBOX (max extent of all layers) is: Envelope(-180.0,-93.188202,180.0,86.811798)
    Total time: 6.58748102188 seconds | Last step: 5.00679016113e-06 seconds
    
    >>> Entering PDB interpreter
    --Return--
    > /usr/local/bin/nik2img.py(131)set_trace()->None
    -> pdb.set_trace()
    
    (Pdb) self.map
    <mapnik_utils.metaclass_injectors.Map object at 0x40ef30>
    (Pdb) self.map.scale()
    0.096269288333333425
    (Pdb) self.map.envelope()
    Envelope(-124.731422,17.9099933333,-66.969849,56.4177086667)
    (Pdb) self.map.envelope().center()
    Coord(-95.8506355,37.163851)
    (Pdb) self.map.background
    <mapnik._mapnik.Color object at 0x454bc8>
    (Pdb) print(self.map.background)
    rgb(140,182,211)
    (Pdb) self.map.srs
    '+proj=latlong +datum=WGS84'
     }}}
     * ,,Then do:,,
     {{{
    #!python
    (Pdb) continue # will leave the pdb intepreter
     }}}
    
    
    === And for all the options available do: ===
     
    {{{
    #!python
    $ nik2img.py -h
