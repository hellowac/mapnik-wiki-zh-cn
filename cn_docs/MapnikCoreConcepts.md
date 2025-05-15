# Core Concepts of Mapnik

Mapnik can be used with XML, Python or C++, but the key concepts are the same across these technologies. For details on how to use the different APIs, see [LearningMapnik](LearningMapnik).

Mapnik creates maps. The *map* object is therefore central to Mapnik's API. The map object provides methods for rendering a map to a graphical output format (usually PNG or PDF).

Maps are (mainly) made up of arbitrary numbers of *layers*. Each layer has a *datasource* that provides the geometry data (provided by one of several *plugins* that read and parse the data). For rendering the data, each layer can be assigned one or multiple styles.

A *style* defines how the objects in a layer are rendered. A style contains one or more *rules* that can optionally constrain its output to *filter* out a subset of the objects provided by the layers datasource, for example to show only these objects who have a specific attribute set. Filters are optional – a common case for simple maps is to have one rule for each layer without any filters. Each rule holds one or more *symbolizers* which are responsible for actually drawing geometry in the output. Depending on the symbolizer class and settings, geometry can be rendered in a variety of ways.

The order of layers, rules and symbolizers is generally important in Mapnik, as the layering of output in the result image is not modelled explicitly (like, for example the `z-index` property in CSS), but determined by the order of these elements. It is therefore important to set these elements up in the correct order to produce the desired results.

There are 3 different coordinate systems in Mapnik.
- lat/lon coordinates where geometric objects placed.
- x/y coordinates after map projection applied where you set bbox/envelope.
- pixmap x/y coordinates used in pan function.

## Further Reading

- [SymbologySupport](SymbologySupport)
- [GettingStartedInPython](GettingStartedInPython)
- [Mapnik API](XMLConfigReference) 

---
Back to [LearningMapnik](LearningMapnik)