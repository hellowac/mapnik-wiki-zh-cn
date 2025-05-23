# Faster labeling

## Ideas and designs for faster label rendering

See also a ticket on code changes/ideas: [#1300](https://github.com/mapnik/mapnik/issues/1300)

* Pre-processing - give thought to pre-processing your data. Split or merge lines so they can easily be labeled nicely without fancy options like `spacing` (see below). Simplify vertices. Collapse attribute columns into boolean columns for fast filtering and lookups. Index those columns.

* `spacing` - do not use this parameter if you can avoid it - see [#1299](https://github.com/mapnik/mapnik/issues/1299). It can help achieve repeated labels along long lines, but this can also be achieved by splitting lines into more segments or breaking multilinestrings into linestrings.

* `encoding` - if rendering labels separately from other data - no background, polygons, lines - then tiles may be majority blank. In this case alternative encoding options may provide significantly encoding speeds, like `png:z=1` might not lead to much larger tiles but will result if much faster encoding. Also, oddly, usually png8 encoding is slower, but it can be just as fast or faster with blank or near-blank tiles so try `png8:z=1`. You could also try reducing colors with `png:c=64` since your labels may only be shades of grey, or even try encoding by passing in a fixed palette. See [https://github.com/mapnik/mapnik/wiki/OutputFormats](OutputFormats) for more details on options, and see the [encoding speed test](https://github.com/mapnik/mapnik/blob/master/tests/python_tests/image_encoding_speed_test.py) that can be run locally from your mapnik source checkout to see the speeds of various combinations of encoding options against test tiles like:

```sh
$ python tests/python_tests/image_encoding_speed_test.py
avg: 1.5909ms | min: 1.6526ms | total: 16.669ms <-- blank png8:z=1:c=50:m=h
avg: 1.5799ms | min: 1.6617ms | total: 16.766ms <-- blank png8:z=1:m=h
...
```

* `halos` - good looking text needs halos. When profiling your text rendering and you may see that halo rendering is a major bottleneck and takes an equal amount of time to placement logic. If should not be this way, please follow [#1298](https://github.com/mapnik/mapnik/issues/1298)

* `label cache` - are your labels coming from multiple layers and being rendered separately from other data? This is a common pattern with Mapnik stylesheets and is usually a good strategy because then layer queries for labels can be customized (e.g. only might pull the `name` column, or you might restrict using a where clause like `WHERE name is not null`). But if your stylesheet has many layers and some of the other layers hit the same tables and rows that your labels come from (for line drawing) then you can reduce the i/o burden on the database by moving your `TextSymbolizer` to the same `Rule` as your `LineSymbolizer`. Then the problem becomes that some labels with get rendered underneath some lines. This is where label caching could help, see: [#870](https://github.com/mapnik/mapnik/issues/870).

* Want sparse labels? Only rendering a few labels here and there is often stylistically desirable over rendering dense labels. It is also potentially very helpful for overall labeling performance, because usually (ideally) label drawing is more expensive than pulling label data (i/o) and doing label placement logic, so less drawing should equal measurably faster maps overall. But, good stylesheet design is needed to ensure this assumption holds: that i/o and placement logic are not the bottlenecks. In terms of placement logic, if you know you want sparse labels on lines, then setting a very high `max-char-angle-delta` can help knock out labels early on from being placed (the default is `22.5`). Also setting an aggressive `minimum-path-length` ([#865](https://github.com/mapnik/mapnik/issues/865)) can also help avoid Mapnik ever attempting to process short lines. Setting `minimum-distance` can also help (but make sure [#995](https://github.com/mapnik/mapnik/issues/995) is fixed in your version of mapnik), however this check comes at the end of most other placement logic, so while it might still help avoid labels being rendering it is not much of a fast track for avoiding placement logic overhead. Also, if you do not set the `spacing` parameter then labeling long lines should not be much more expensive than other lengths, but beware that small spacing values (like 1-50) will likely result in placement logic on lines greater than 50 pixels long becoming a bottleneck.
