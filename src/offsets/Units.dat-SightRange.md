
#  Units.dat - Sight Range
Address   | 663238
----------|-------------
Player ID | 222133 (Byte Offset: 0)
Size 	  | 1
Length 	  | 228
SC:R      | Simple Data

Set value from 0-11.  Values greater than 11 will crash.

Example: Setting SCV Sight Range to 5.

Base Address = 0x00663238
SCV Units.dat Index = 0x7

0x00663238 + 0x7 = 0X66323F

0x0066323F is not divisible by 4, next lowest multiple of 4 is 0x0066323C
Went down 3 bytes to get from 0x0066323F to 0x0066323C
Therefore, need to modify 0xFF000000 at 0x0066323C to the change value at 0x0066323F

// set SCV sight range to 5
Masked MemoryAddr(0x0066323C, Set To, 0x05000000, 0xFF000000);
