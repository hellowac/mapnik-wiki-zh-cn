<!-- Name: BuildingSymbolizer -->
<!-- Version: 3 -->
<!-- Last-Modified: 2009/02/06 07:56:36 -->
<!-- Author: jamierob -->
## Configuration Options for BuildingSymbolizer

A BuildingSymbolizer is used to create a pseudo 3D effect on polygons.

|**parameter**|**value**|**default**|
|:-----------:|:-------:|:---------:|
| fill             |  CSS colour    | gray      |
| fill-opacity     |  float         | 1.0       |
| height           |  float         | 0         |

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

----

Example output:

[[/images/BuildingSymbolizer.png]]