# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in dollars.

| Parameter | Values | Notes |
|-----------|--------|-------|
| `weight_kg` | positive float | Parcel weight in kilograms |
| `zone` | `"local"`, `"regional"` | Delivery zone |
| `service` | `"standard"` *(default)*, `"express"` | Express adds a flat $7 surcharge |

Unknown zones or service levels raise `ValueError`.

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
# Standard quote – 2 kg to local zone
python -m warehouse.cli 2 local

# Express quote – 2 kg to regional zone
python -m warehouse.cli 2 regional --service express
```
