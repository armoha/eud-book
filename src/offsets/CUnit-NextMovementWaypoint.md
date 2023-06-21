
#  CUnit - Next Movement Waypoint
Address   | 59CCC0
----------|-------------
Player ID | 19031 (Byte Offset: 0)
Size 	  | 2
Length 	  | 2
SC:R      | Unsupported

0x0000FFFF x-coord
0xFFFF0000 y-coord

The next way point in the path the unit is following to get to its destination. Equal to moveToPos for air units since they don't need to navigate around buildings or other units. (bwapi)
