#  Switch Table
Address   | 58DC40
----------|-------------
Player ID | 3639 (Byte Offset: 0)
Size 	  | 32
Length 	  | 1
SC:R      | Simple Data

+0x00 (EPD 3639)
	Switch 1: *1
	Switch 2: *2
	Switch 3: *4
	Switch 4: *8
	Switch 5: *16
	Switch 6: *32
	Switch 7: *64
	Switch 8: *128
	...
	Switch 32: *2147483648

When none of the switches from 1 to 32 
are set, the value of the address is: 0

When only switch 8 is set, the value of the
address is: 128.

When only switch 2 and switch 8 are set,
the value of the address is: 2 + 128 = 130.

+0x04 (EPD 3640): Switch 33-64
+0x08 (EPD 3641): Switch 65-96
+0x0C (EPD 3642): Switch 97-128
+0x10 (EPD 3643): Switch 129-160
+0x14 (EPD 3644): Switch 161-192
+0x18 (EPD 3645): Switch 193-224
+0x1C (EPD 3646): Switch 225-256
