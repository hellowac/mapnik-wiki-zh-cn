<!-- Name: BuildingSymbolizer -->
<!-- Version: 3 -->
<!-- Last-Modified: 2009/02/06 07:56:36 -->
<!-- Author: jamierob -->
[[Symbolizer|SymbologySupport]] that specifies rendering of a pseudo 3D effect for polygons giving them a building-like appearance.

Often used instead of a [[PolygonSymbolizer]].

[[/images/BuildingSymbolizer.png]]

## Configuration Options

| **parameter** |             **value**              | **default** |
| :-----------: | :--------------------------------: | :---------: |
|     fill      |             CSS colour             |    gray     |
| fill-opacity  |               float                |     1.0     |
|    height     | float (static value or expression) |      0      |

## Examples

### Default

` FIXME: Add image `

#### XML

```xml
    <BuildingSymbolizer fill="#000000" height="8" fill-opacity="1" />
```

Height as expression:

```xml
    <BuildingSymbolizer fill="#000000" height="[height_db]" fill-opacity="1" />
```

#### Python

` FIXME `

#### C++

` FIXME `
