#  Units.dat - Group Flags
Address   | 6637A0
----------|-------------
Player ID | 222479 (Byte Offset: 0)
Size 	  | 1
Length 	  | 228
SC:R      | Simple Data

0x01 - Zerg (Uses underlings, can build on creep)
0x02 - Terran (Uses Supply, has sublabel, buildings will burn)
0x04 - Protoss (Uses Psi)
0x08 - Men
0x10 - Building
0x20 - Factory
0x40 - Independent
0x80 - Neutral

Example:
Set Protoss Observatory as Terran and Unset Protoss so it will burn and can be repaired.
Protoss Observatory Units.dat Index = 159 = 0x9F
0x006637A0 + 0x9F = 0x0066383F
0x0066383F is not divisible by 4, next lowest multiple of 4 = 0x0066383C
Therefore, modify 0xFF00000 at 0x0066383C to hit 0x0066383F
// set Protoss Observatory Terran
MemoryAddr(0x0066383C, Add, 0x02000000);
// unset Protoss Observatory Protoss
MemoryAddr(0x0066383C, Subtract, 0x04000000);
