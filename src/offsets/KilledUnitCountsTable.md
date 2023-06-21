
#  Killed Unit Counts Table
Address   | 5878A4
----------|-------------
Player ID | -2736 (Byte Offset: 0)
Size 	  | 48
Length 	  | 228
SC:R      | Simple Data

Counts per player, per unit.

For each unit, 4 bytes per player, for 12 players.

offset + (unit*12 + player) * sizeof(u32)
