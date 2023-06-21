#  Tile Flags Pointer
Address   | 6D1260
----------|-------------
Player ID | 334783 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | Backed By Code

Pointer to (Map Width)x(Map Height) array of u32 flags:
0x000000xx - Visibility Flags -- bits correspond to each player
0x0000xx00 - Explored Flags -- bits correspond to each player
0x00010000 - Walkable
0x00020000 - Unused?
0x00040000 - Unwalkable
0x00080000 - Unused?
0x00100000 - Unused?
0x00200000 - Unused?
0x00400000 - Has Creep
0x00800000 - Unbuildable (i.e., water tiles)
0x01000000 - Low Ground
0x02000000 - Med Ground
0x04000000 - High Ground
0x08000000 - Occupied (i.e. contains a building)
0x10000000 - Creep Receeding
0x20000000 - Cliff Edge
0x40000000 - Temporary Creep
0x80000000 - Unused?

Taken from: https://github.com/bwapi/bwapi/blob/master/bwapi/BWAPI/Source/BW/Structures.h#L80
