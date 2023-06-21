
#  Force Names
Address   | 58D5BC
----------|-------------
Player ID | 3222 (Byte Offset: 0)
Size 	  | 30
Length 	  | 4
SC:R      | Simple Data

4 byte integers: 1 integer for each force, string
number of the name per force:
	force 1: 0x0058D5BC (EPD 3222)
	force 2: 0x0058D5DC (EPD 3230)
	force 3: 0x0058D5F8 (EPD 3237)
	force 4: 0x0058D614 (EPD 3244)

untested: even forces strip two characters from
the start of the force name

advice: use [EUD] Text to Value converter

force flags
FORCE NAMES
player's force
