(Packaged from 5cd3cb2efdaf7e9990a57e8e00b652a81aaa39ae)

- Support for PostGIS 2.0 (#956,#1083)

- Switched back to "libmapnik" and "import mapnik" rather than "mapnik2" (mapnik2 will still work from python) (#941)

- Restored Python 2.5 compatibility (#904)

- Fixed `mapnik-config --version` (#903)

- Cairo: Add full rendering support for markers to match AGG renderer functionality (#1071)

- Fix Markers rendering so that ellipse height/width units are pixels (previously were unintentially radii) (#1134)

- Added 'ignore-placement` attribute to markers-symbolizer (#1135)

- Removed svn_revision info from mapnik-config and python bindings as git is now used

- Removed OGCServer from core - now at https://github.com/mapnik/OGCServer (e7f6267)

- Fixed SQLite open stability across platforms/versions (#854)

- Workaround for boost interprocess compile error with recent gcc versions (#950,#1001,#1082)

- Fix possible memory corruption when using hextree mode for png color reduction (#1087)

- Fixed bug in shield line placement when dx/dy are used to shift the label relative to the placement point (Matt Amos) (#908)

- Fix to avoid modifying a feature if an attribute is requested that does not exist (0f5ab18ed)

- Fixed ability to save to jpeg format from python (7387afd9) (#896)
