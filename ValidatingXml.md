<!-- Name: ValidatingXml -->
<!-- Version: 3 -->
<!-- Last-Modified: 2011/01/06 08:35:39 -->
<!-- Author: phispi -->
# Validating Xml

To validate the Map xml file, reference mapnik's mapfile DTD as in:

```
    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE Map SYSTEM "mapnik2.dtd">
    <Map>
    ...
    </Map>
```

The DTD file can be found here: https://github.com/mapnik/mapnik/blob/master/utils/xml/mapnik.dtd


## Validating in editors

 * *Eclipse*
  * One time validation: right click on the xml file -> validate
  * Automatic validation: right click on project -> properties -> Validation -> Add Validation Builder to project -> OK


## Validating from the command line

```sh
    xmllint --valid --noout path/to/file.xml
```