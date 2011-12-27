<!-- Name: InternationalText -->
<!-- Version: 14 -->
<!-- Last-Modified: 2011/09/06 11:31:00 -->
<!-- Author: springmeyer -->
# International Text

Mapnik supports unicode text and Right-to-left (RTL) languages (through ICU library).

This page is to document and discuss improvements needed to unicode text handling.

## Current Tickets

 * [#364](https://github.com/mapnik/mapnik/issues/364) / [#404](https://github.com/mapnik/mapnik/issues/404) - RTL mirroring
 * [#519](https://github.com/mapnik/mapnik/issues/519) - RTL spacing wrong with numbers (UBIDI_MIXED)
 * [#112](https://github.com/mapnik/mapnik/issues/112) - Indic RTL font shaping
 * [#189](https://github.com/mapnik/mapnik/issues/189) / [#409](https://github.com/mapnik/mapnik/issues/409) - RTL wrapping (line breaks)
  * from osm trac: http://trac.openstreetmap.org/ticket/2182 and http://trac.openstreetmap.org/ticket/1515
 * [#550](https://github.com/mapnik/mapnik/issues/550) - line-follow: perhaps made worse by unicode chars, perhaps not, needs closer look
 * [#558](https://github.com/mapnik/mapnik/issues/558) - Character spacing not correct for nepali text
 * [#582](https://github.com/mapnik/mapnik/issues/582) - TextSymbolizer bug with Armenian letters

## Issues

 * Better leveraging of ICU
  * Does ICU support any mirroring that we are not yet leveraging?
    * It seems that ICU *does not* support shaping for anything other than Arabic RTL, but need to dig deeper

 * Other libraries that solve some of these problems:
  * In the past developer discussions have mentioned using the [pango library](http://www.pango.org/), or ideas from [liblinebreak](http://vimgadgets.sourceforge.net/liblinebreak/)
    * If used Pango would need to be an optional dependecy because we don't want to have to depend on whole GLib/GTK stack.
    * Artem is not interested in a pango dependency
    * (MapOSMatic is using pango via python: http://news.maposmatic.org/?p=125)
    * What about http://www.freedesktop.org/wiki/Software/HarfBuzz?

 * http://behdad.org/text/
