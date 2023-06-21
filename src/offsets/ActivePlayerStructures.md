#  Active Player Structures
Address   | 57EEE0
----------|-------------
Player ID | -11553 (Byte Offset: 0)
Size 	  | 36
Length 	  | 12
SC:R      | Backed By Code

A structure for each player containing their HumanID, StormID, Type, Race, Team, and Name.
+0x00 = HumanID (4 bytes)
+0x04 = StormID (4 bytes)
+0x08 = Type (1 byte; 0 = inactive, 1 = computer, 2 = human, 3 = rescuable, 7 = neutral)
+0x09 = Race (1 byte; 0 = zerg, 1 = terran, 2 = protoss)
+0x0A = Team (1 byte)
+0x0B = Name (25 bytes)
