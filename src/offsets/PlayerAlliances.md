
#  Player Alliances
Address   | 58D634
----------|-------------
Player ID | 3252 (Byte Offset: 0)
Size 	  | 12
Length 	  | 12
SC:R      | Simple Data

EPD 3252
+ 0x00: P1 ally status to P1
+ 0x01: P1 ally status to P2 (*256).
+ 0x02: P1 ally status to P3 (*65536).
+ 0x03: P1 ally status to P4 (*16777216).
EPD 3253
+ 0x04: P1 ally status to P5.
+ 0x05: P1 ally status to P6 (*256).
+ 0x06: P1 ally status to P7 (*65536).
+ 0x07: P1 ally status to P8 (*16777216).
EPD 3254
P1 ally status to P9-P12.
EPD 3255
+ 0x0C: P2 ally status to P1.
+ 0x0D: P2 ally status to P2 (*256).
etc

0x00: Enemy, 0x01: Ally, 0x02: Allied Victory

Note - A player is always allied OR allied victory to themself. I could not confirm through testing if it was just one of them, but in most cases, it's allied. Otherwise assume allied victory instead.
