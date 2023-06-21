#  Unit Infomation
Address   | 5193A0
----------|-------------
Player ID | -115697 (Byte Offset: 0)
Size 	  | 12
Length 	  | 228
SC:R      | See Description

Edited by PereC, 2021-06-05
In SC:R, 64-bit starcraft ignores this part. You are suggested to use 32-bit starcraft if this part of memory is modified by EUD triggers.
+0x0: Unit ID
+0x4: Status Function
+0x8: Display Function
