
#  Death Table Start
Address   | 58A364
----------|-------------
Player ID | 0 (Byte Offset: 0)
Size 	  | 48
Length 	  | 228
SC:R      | Simple Data

Counts per player, per unit

First entry in the death table (P1 marine) for 1.16.1.

Structured like
P1 marine
P2 marine
...
P12 marine
P1 ghost
P2 ghost
...
P12 ghost
...
...

For each unit, 4 bytes per player, for 12 players.

offset + (unit*12 + player) * sizeof(u32)
