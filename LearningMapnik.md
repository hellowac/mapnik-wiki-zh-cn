### Important Note: The Mapnik documentation is currently in the process of being restructured and updated for Mapnik 2.0 and the move to GitHub -- please double check all information found here and fix / report any errors you may find. Thanks for your patience.
---

Mapnik can be used in a variety of ways. The most widely used options are using XML config files, using the Python bindings or using the API directly in C++.

## General Concepts

* [[MapnikCoreConcepts]]
* [[IntroductionToGIS]] -- a brief intro to the world of mapping systems

## Getting started

Mapnik is written in C++, but many users use its bindings to higher-level languages, including Python or Javascript. If you've got an application that wraps Mapnik entirely, you might only need to concern yourself with the XML stylesheets that describe Mapnik's map styles.

To get first results, choose your weapon: XML, Python, C++, or node.js

* [[Getting started using XML|GettingStartedInXML]]
* [[Getting started using Python|GettingStartedInPython]]
* [[Getting started using C++|GettingStartedInC]]
* [node.js bindings](http://github.com/mapnik/node-mapnik)

### Further Resources:

- [[Mapnik API]]
- [[Notes and Caveats]]
- [[MapnikTutorials]]
- [[ExampleCode]]

## How to Style your Maps

* [[SymbologySupport]]
* [[MapDesign]] -- use Mapnik to design better looking maps!

## How to combine Map styles and Layers

* See the [[MapnikTutorials]]
* XML Mapfile details [[XMLConfigReference]]

## How to read in data

* [[PluginArchitecture]]

## How to use the Mapnik Python Bindings

* See the python api docs [here](http://media.mapnik.org/api_docs/python/)
* Check out the [[MapnikTutorials]] and  the references at [[ExampleCode]]
* Study applications like Cascadenik or Nik2img at http://mapnik-utils.googlecode.com/

## Advanced Topics
 
* [[MapnikRenderers]] -- Render with AGG or Cairo
* [[OutputFormats]] -- Which format to use based on speed, quality, and rendering tradeoffs.
* [[LabelingSupport]] -- Discover the intricacies of label placement.

[Generating Contours](http://wiki.openstreetmap.org/index.php/Contours) - Using Mapnik with GDAL to build contours of the world.

[[ManagingLargeXmlFiles]] -- Do things once and only once using XML entities.

[[Hooking up Mapnik to PostGIS|PostGIS]]

[[MapnikReferences]] -- Various other resources related to Mapnik and Mapping