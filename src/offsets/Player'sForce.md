#  Player's Force
Address   | 58D5B0
----------|-------------
Player ID | 3219 (Byte Offset: 0)
Size 	  | 1
Length 	  | 8
SC:R      | Simple Data

8 bytes: 1 byte for each active player, specifying
which of the 4 forces (0-based) that the player's
on:
	EPD 3219
	Player 1: 0x0058D5B0
	Player 2: 0x0058D5B1 force*256
	Player 3: 0x0058D5B2 force*65536
	Player 4: 0x0058D5B3 force*16777216
	EPD 3220
	Player 5: 0x0058D5B4
	Player 6: 0x0058D5B5 force*256
	Player 7: 0x0058D5B6 force*65536
	Player 8: 0x0058D5B7 force*16777216

each force have a multipler value to differentiate
themselves from one another:
	Force 1
	Force 2 (*2 to Player)
	Force 3 (*3 to Player)
	Force 4 (*4 to Player)

force flags
force names
PLAYER'S FORCE
