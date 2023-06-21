
#  Replay Header - Player Entries
Address   | 6D0FD1
----------|-------------
Player ID | 334619 (Byte Offset: 1)
Size 	  | 36
Length 	  | 12
SC:R      | Read Only

Unfortunately this struct is not dword-aligned.

+0 - u32 slot (0x006D0FD1)
+4 - u32 storm ID (0x006D0FD5)
+8 - u8 type (0x006D0FD9)
+9 - u8 race (0x006D0FDA)
+A - u8 team (0x006D0FDB)
+B - char name[25] (0x006D0FDC)

For next player add 9 player ID's.
