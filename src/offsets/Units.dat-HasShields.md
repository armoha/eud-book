#  Units.dat - Has Shields
Address   | 6647B0
----------|-------------
Player ID | 223507 (Byte Offset: 0)
Size 	  | 1
Length 	  | 228
SC:R      | Simple Data

Example: Unset "has shields" for Protoss Observatory

Base Address = 0x006647B0
Protoss Observatory Units.dat Index = 159 = 0x9F 

0x006647B0 + 0x9F = 0x0066484F

0x0066484F is not divisible by 4, next lowest multiple of 4 = 0x0066484C
Went down by 3 bytes to reach the multiple of 4

Therefore, modify 0xFF00000 at 0x0066484C to change value at 0x0066484F

// set observatory "has shields" to 0
Masked MemoryAddr(0x0066484C, Set To, 0, 0xFF000000);
