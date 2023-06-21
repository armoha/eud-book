#  Start Locations
Address   | 58D720
----------|-------------
Player ID | 3311 (Byte Offset: 0)
Size 	  | 4
Length 	  | 8
SC:R      | Simple Data

Point:
u16 X
u16 Y

EPD 3311
+0x00: P1 Start Location (X, Y*65536)
+0x01: P2 Start Location (X*16777216, Y*256) *256
+0x02: Unknown (4194352) *65536
+0x03: Unknown (805322752) *16777216
EPD 3312
+0x04: Unknown (3145792)
+0x05: P3 Start Location (X*16777216, Y*256) *256
+0x06: Unknown (4194352) *65536
+0x07: Unknown (805322752) *1677216
EPD 3313
+0x08: Unknown (3145792)
+0x09: P4 Start Location (X*16777216, Y*256) *256
+0x0A: Unknown (4194352) *65536
+0x0B: Unknown (805322752) *16777216
EPD 3314
+ 0x0C: Unknown (3145792)
+0x0D: P5 Start Location (X*16777216, Y*256) *256
+0x0E: Unknown (12582960) *65536
+0x0F: Unknown (805355520) *16777216
EPD 3315
+0x10: Unknown (3145920)
+0x11: P6 Start Location (X*16777216, Y*256) *256
+0x12: Unknown (12582960) *65536
+0x13: Unknown (805355520) *16777216
EPD 3316
+0x14: Unknown (3145920)
+0x15: P7 Start Location (X*16777216, Y*256) *256
+0x16: Unknown (12582960) *65536
+0x17: Unknown (805355520) *16777216
EPD 3317
+0x18: Unknown (3145920)
+0x19: P8 Start Location (X*16777216, Y*256) *256
+0x1A: Unknown (12582960) *65536
+0x1B: Unknown (805355520) *16777216

Base Value (when start locations are placed top-left of the map)
Player 1: 3145792
Player 2-8: 1073754112

Already you can tell that all of this is confusing and doesn't make a lot of sense on its own, so here's a tutorial that will hopefully clear up some things:

1.To check if the position of Player 3's Start Location is at the location you placed it at, look at EPD 3312. 

2. Look at the X pixel placement of P3 start location in your map editor and
write it down.

3. Look at the Y pixel placement of P3 start location in your map editor
and write it down.

4. Now plug those numbers into this formula:
Memory at Death Table + 3312 is exactly (3145792 + (((Start Location X * 16777216) + (Start Location Y * 256)) * 256) + (4194352 * 65536) + (805322752 * 16777216))

3145792, 4194352, and 805322752 are "constants," that you need to know and account for in the equation. Because EPD reads 4 bytes at once (this formula does not work for Player 1 and Player 2 Start Location. If you understood everything that was said so far, then coming up with another formula that's specific to those two will be easy).

5. The trigger should work, and if it doesn't, then either you have miscalculated or these "unknowns", are not constant.

Challenge - Find out what those unknowns are actually for, and/or create an easier formula than the one I have come up with.
