#  Trigger Execution Timer (Hyper triggers)
Address   | 6509A0
----------|-------------
Player ID | 203151 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | Simple Data

When this value reaches 0, trigger loop executes.

Preserve to 0 for single-tick hypers, or 1 for traditional hyper triggers (2 ticks).

Wait(n) will make this value 1 after ceil(n / 'ms per tick') + 1, so Wait(0) makes this value to 1, making the trigger loop execute every 2 ticks.
