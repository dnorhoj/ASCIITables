# ASCIITables

Simple tool for making tables, no requirements. Check out example.py

## Usage

The best way to get started is by using the `asciitables.create_table()` function.

```py
import asciitables

# Some two dimensional list
data = [
    ["First", "Row", "(header)"],
    ["Second", "Row", "data"],
    ["Third", "Row", "data"],
]

table = asciitables.create_table(data, theme=asciitables.THIN_THEME)

print(table)
```

This code produces the following output:

```
┌────────┬─────┬──────────┐
│ First  │ Row │ (header) │
├────────┼─────┼──────────┤
│ Second │ Row │ data     │
│ Third  │ Row │ data     │
└────────┴─────┴──────────┘
```