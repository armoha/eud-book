#  Vanilla Location Table
Address   | 58D740
----------|-------------
Player ID | 3319 (Byte Offset: 0)
Size 	  | 20
Length 	  | 64
SC:R      | Simple Data

This Location Table is not used in the Expansion (Brood War)!

+0x00 (EPD 3319)

	This is the LEFT position of the location (X1).

+0x04 (EPD 3320)

	This is the TOP position of the location (Y1).

+0x08 (EPD 3321)

	This is the RIGHT position of the location (X2).

+0x0C (EPD 3322)

	This is the BOTTOM position of the location (Y2).

+0x10 (EPD 3323)

String ID: 
	1) Look in the String Editor of the Map Editor you're using
	2) Find the name of the location within it
	3) Now count all the strings that are above it, and add 1 to the total number.
	4) The number you came to is the String ID for that location

Flags (Affect Layers):
	Low Ground: 65536
	Med Ground: 131072
	High Ground: 262144
	Low Air: 524288
	Med Air: 1048576
	High Air: 2097152

When all flags are enabled, the value
of the address is: 4128768 + String ID

When all flags are disabled, the value
of the address is: String ID

Note: the 64th location is "Anywhere."
