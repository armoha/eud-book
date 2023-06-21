#  Tile Function Pointers
Address   | 6D0C70
----------|-------------
Player ID | 334403 (Byte Offset: 0)
Size 	  | 4
Length 	  | 4
SC:R      | Unsupported

0x006D0C70 -> 0x0047E2D0 -- refreshes map tiles for drawing?
0x006D0C74 -> isCreepCovered -- checks if a tile is creep
0x006D0C78 -> isTileVisible -- checks if a player can see the tile
0x006D0C7C -> null pointer? -- I couldn't find what function is actually put here
