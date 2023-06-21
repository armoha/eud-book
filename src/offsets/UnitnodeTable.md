#  Unitnode Table
Address   | 59CCA8
----------|-------------
Player ID | 19025 (Byte Offset: 0)
Size 	  | 336
Length 	  | 1700
SC:R      | Backed By Code

[SCR: See individual entries]

See Unitnode Structure in the Reference page or https://github.com/bwapi/bwapi/blob/master/bwapi/BWAPI/Source/BW/CUnit.h

Units are loaded to index 0 then 1699, 1698, 1697... (this includes pre-placed map units)

Compute the memory location of an index using:
0x0059CCA8 + (0x150 * index)

Example:
Index 1699 is at 0x00628298 = 0x0059CCA8 + (0x150 * 0x6A3)  (player 161,741)
where 0x0059CCA8 is the base address, 0x150 = 336 is the size and 0x6A3 = 1699 is the unit index

Index 1698 is at 0x00628148 = 0x0059CCA8 + (0x150 * 0x6A2)
Index 1697 is at 0x00627FF8 = 0x0059CCA8 + (0x150 * 0x6A1)
Index 1696 is at 0x00627EA8 = 0x0059CCA8 + (0x150 * 0x6A0)
etc. (difference between each index is the size, 336 = 0x150)
