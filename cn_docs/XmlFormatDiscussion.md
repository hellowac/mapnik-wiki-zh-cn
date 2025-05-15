<!-- Name: XmlFormatDiscussion -->
<!-- Version: 6 -->
<!-- Last-Modified: 2008/09/08 17:15:20 -->
<!-- Author: springmeyer -->
## XML Format Discussion

The mapnik XML file format needs a revision. This page exists to collect
ideas, sketches and examples. The idea is to paste XML snippets here and
to discuss them on the (user) mailing list. The changes we agree upon should
be added to the list of
[query:status=new|assigned|reopened&keywords=XML XML tasks]
by adding a ticket with the keyword `XML`.

If we do ticket [#58](https://github.com/mapnik/mapnik/issues/58) it would be consequent to make the denominators attributes too:

```xml
    <Style name="some_style">
        <Rule max_denominator="6000000" min_denominator="600000">
            <Filter> ... </Filter>
            <PointSymbolizer/>
        </Rule>
    </Style>
```
(David Siegel)