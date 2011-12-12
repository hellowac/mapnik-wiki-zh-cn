<!-- Name: GlyphSymbolizer -->
<!-- Version: 3 -->
<!-- Last-Modified: 2011/09/02 09:03:22 -->
<!-- Author: herm -->
# GlyphSymbolizer

*New in 0.8 (aka Mapnik2) but about to be removed again in Mapnik 2.1*

Renders a TrueType Glyph at the Feature's label location (usually the center of polygons/lines and on the point themselves).

(see [source](https://github.com/mapnik/mapnik/blob/master/tests/python_tests/glyph_symbolizer_test.py) for sample usage)


## Sample XML Configuration

```xml
    
    <?xml version="1.0" encoding="utf-8"?>
    <Map>
        <Style name="arrows">
        <Rule>
          <GlyphSymbolizer
            face_name="DejaVu Sans Condensed"
            size="10"
            char="'í'"
            allow_overlap="true"
            avoid_edges="false"
            halo_fill="rgba(0%,0%,0%,4%)"
            halo_radius="1"
            value="[value]"
            angle="[azumuth]+90"
          >
            <RasterColorizer>
              <ColorBand value="0" color="#0044cc"/>
              <ColorBand value="10" color="#00cc00"/>
              <ColorBand value="20" color="#ffff00"/>
            </RasterColorizer>
          </GlyphSymbolizer>
        </Rule>
      </Style>
    </Map>
```

TODO: Describe all parameters