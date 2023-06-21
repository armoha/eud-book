#  Force Flags
Address   | 58D5B8
----------|-------------
Player ID | 3221 (Byte Offset: 0)
Size 	  | 1
Length 	  | 4
SC:R      | Simple Data

4 bytes: 1 byte for each force specifying the flags;
	force 1: 0x0058D5B8
	force 2: 0x0058D5B9 bits*256
	force 3: 0x0058D5BA bits*65536
	force 4: 0x0058D5BB bits*16777216

7 bits: 1 bit per flag per force;
	bit 0: randomize location (+1 to byte)
	bit 1: ally (+2 to byte)
	bit 2: allied victory (+4 to byte)
	bit 3: shared vision (+8 to byte)
	bit 4: unknown/unused (+16 to byte)
	bit 5: unknown/unused (+32 to byte)
	bit 6: unknown/unused (+64 to byte)
	bit 7: unknown/unused (+128 to byte)

EPD 3221: read not one byte, but all four bytes 
and 12 bits
	
FORCE FLAGS
force names
player's force
