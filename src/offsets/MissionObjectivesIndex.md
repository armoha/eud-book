
#  Mission Objectives Index
Address   | 58D6C4
----------|-------------
Player ID | 3288 (Byte Offset: 0)
Size 	  | 4
Length 	  | 12
SC:R      | Simple Data

EPD 3288 (+0x00):

This is the Mission Objective String ID for Player 1.

To find the String ID for a Mission Objective:

	1) Look at Player 1's Mission Objective text.
	2) Go into the String Editor of the Map Editor you're using.
	3) Find the exact string used in Player 1's Mission Objective text 		within the String Editor.
	4) Now count all of the string above it, and add 1 to the total 	number.

Note: This does not work if Player 1 does not have any text in his Mission Objective. In fact, the value of the address would be 0.

EPD 3289 (+0x04): This is the Mission Objective String ID for Player 2.
EPD 3290 (+0x08): This is the Mission Objective String ID for Player 3.
EPD 3291 (+0x0C): This is the Mission Objective String ID for Player 4.
EPD 3292 (+0x10): This is the Mission Objective String ID for Player 5.
etc
