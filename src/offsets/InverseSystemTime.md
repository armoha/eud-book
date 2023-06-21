
#  Inverse System Time
Address   | 51CE8C
----------|-------------
Player ID | 0 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | 

Value : -GetTickCount()
 (about 10ms error)
Used for input polling. See .text:004D98D8 for more info. Can be used to detect lagging
or syncing with game audio.
