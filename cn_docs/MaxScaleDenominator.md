<!-- Name: MaxScaleDenominator -->
<!-- Version: 2 -->
<!-- Last-Modified: 2008/12/05 08:53:23 -->
<!-- Author: sven -->
# Max Scele Denominator

Activates the rule, if [ScaleAndPpi scale] < MaxScaleDenominator + 1e-6

Example:

```xml
    <Style name="text">
      <Rule>
        <Filter>[place] = 'city'</Filter>
          <MaxScaleDenominator>10000000</MaxScaleDenominator>
          <MinScaleDenominator>2000000</MinScaleDenominator>
        <TextSymbolizer name="name" face_name="DejaVu Sans Book" size="10" fill="#000" dy="0" halo_radius="1" wrap_width="0"/>
      </Rule>
    </Style>
```
