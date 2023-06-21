#  Sprite Table
Address   | 629D98
----------|-------------
Player ID | 163469 (Byte Offset: 0)
Size 	  | 36
Length 	  | 2500
SC:R      | Read Only

[SCR: See individual entries]

Difference between each entry: 9 Player ID's

Struct:
https://github.com/bwapi/bwapi/blob/master/bwapi/BWAPI/Source/BW/CSprite.h

Populates like CUnit, with 2nd entry at the rearmost of the table, and the 3rd the 2nd rearmost entry of the table; first entry will be a cursour sprite, having sprite ID of 318.
