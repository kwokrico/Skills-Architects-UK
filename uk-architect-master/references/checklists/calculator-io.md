# Calculator I/O reference

All calculators are advisory only. Implementations live in `scripts/calculators.py`.

## part_l_screen

```json
{
  "proposed_u": 0.18,
  "target_u": 0.20,
  "dwelling_area": 95,
  "design_emission_rate": 12.5,
  "notional_emission_rate": 14.0
}
```

- `proposed_u`, `target_u` (required): fabric U-value comparison
- `design_emission_rate`, `notional_emission_rate` (optional): TER check

## part_o_screen

```json
{
  "glazing_ratio": 0.35,
  "orientation": "S",
  "purge_ventilation_available": true,
  "external_shading": false,
  "urban_context": "normal"
}
```

- `urban_context`: `normal`, `dense`, or `urban_heat_island`
- Risk bands: Low / Medium / High — escalate High per compliance thresholds

## ipms_converter

```json
{
  "value": 1000,
  "from_type": "GIA",
  "to_type": "IPMS2"
}
```

Supported pairs: GIA↔IPMS2, NIA↔IPMS3 (advisory factors only).

## egress_screen

```json
{
  "length": 18,
  "width": 12,
  "sprinklered": false,
  "use_type": "residential"
}
```

Returns diagonal distance vs advisory limit; `Review` requires full AD B / fire strategy.
