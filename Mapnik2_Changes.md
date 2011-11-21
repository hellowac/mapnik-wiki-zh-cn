<!-- Name: Mapnik2/Changes -->
<!-- Version: 21 -->
<!-- Last-Modified: 2011/11/16 09:31:04 -->
<!-- Author: artem -->
# Changes between Mapnik 0.7.x and Mapnik 2.0

## XML

## Global Changes

### Underscores --> Dashes

All properties that previously used underscores, ie '_' now use dashes ('-'). So, for example: 'allow_overlap' is now 'allow-overlap'
   * Mapnik 0.7.2 has compatibility with both syntaxes as of r2579
   * Mapnik 2.0 moved to only dashes in r2582
   * Note: branch of trunk tagged before r2582: https://trac.mapnik.org/browser/branches/mapnik2-pre-dashes
   * properties changed include: 

    #!python
    ['paths_from_xml','minimum_version','buffer_size','face_name,fonset_name','clear_label_cache','vertical_alignment','halo_fill','halo_radius','text_ratio','wrap_width','wrap_before','wrap_character','text_transform','line_spacing','label_position_tolerance','character_spacing','min_distance','minimum_distance','avoid_edges','allow_overlap','max_char_angle_delta','horizontal_alignment','justify_alignment','unlock_image','no_text']

### CSSParameters --> Properties

This change affects the PolygonSymbolizer, LineSymbolizer, RasterSymbolizer, and BuildingSymbolizer only.

All CSSParameters have been removed, so for example, this:


    #!xml
    <PolygonSymbolizer>
        <CssParameter name="fill">yellow</CssParameter>
    </PolygonSymbolizer>

is now:


    #!xml
    <PolygonSymbolizer fill="yellow" />

## Changes by Element

### Map
|| *component*       ||                  *old*             ||                    *new* ||
|| Map                         ||     bgcolor            ||     background-color                           ||
|| Map                         ||      did not exist  ||     background-image                           ||

### Symbolizers

|| *component* ||                  *old* ||                    *new* ||
|| TextSymbolizer   || name='field'  ||     name='[field]'                            ||
|| TextSymbolizer   || text_convert  ||      text-transform                            ||
|| TextSymbolizer   || min_distance  ||      minimum-distance                            ||
|| TextSymbolizer   || did not exist  ||     minimum-padding                            ||
|| PointSymbolizer / PolygonPatternSymbolizer / LinePatternSymbolizer   || width  ||     removed                            ||
|| PointSymbolizer / PolygonPatternSymbolizer / LinePatternSymbolizer   || height  ||     removed                            ||
|| PointSymbolizer / PolygonPatternSymbolizer / LinePatternSymbolizer   || type  ||     removed                            ||


# Python API

|| *component* ||                  *old* ||                    *new* ||
|| mapnik             ||               mapnik.Envelope  ||                   mapnik.Box2d ||
|| TextSymbolizer   || set_displacement (function)  ||     displacement (property)    ||
|| TextSymbolizer   || first argument was string  ||    first argument now mapnik2.Expression(['field'])    ||
|| ShieldSymbolizer   || first argument was string  ||    first argument now mapnik2.Expression(['field'])    ||
|| ShieldSymbolizer   || fifth argument was string  ||    fifth argument now mapnik2.PathExpression('/path/to/[field].png')    ||


# C++ API
|| *component* ||                  *old* ||                    *new* ||
|| mapnik::Map ||                 getWidth  ||                   width ||
|| mapnik::Map ||                 getHeight  ||                   height ||
|| mapnik::Map ||                 zoomToBox  ||                  zoom_to_box ||
|| mapnik::Map ||                 setBackground  ||                  set_background ||
|| mapnik::Map ||                 getCurrentExtent  ||                  get_current_extent  ||
|| mapnik::Map ||                 zoomToBox  ||                  zoom_to_box ||
|| mapnik:: ||                 mapnik::Layer  ||                   mapnik::layer ||
|| mapnik:: ||                 mapnik::Envelope  ||                   mapnik::box2d ||
|| mapnik:: ||                 mapnik::ImageData32  ||                   mapnik::image_data_32 ||
|| mapnik:: ||                 mapnik::Image32  ||                   mapnik::image_32 ||
|| mapnik:: ||                 mapnik::Image8  ||                   mapnik::image_8 ||


# Planned/Proposed Before Release
## Python API
 * Image.tostring -> Image.encode() 
 * All remaining uses of 'envelope' -> 'box2d' (like ds.envelope())
