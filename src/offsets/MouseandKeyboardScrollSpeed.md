
#  Mouse and Keyboard Scroll Speed
Address   | 513B68
----------|-------------
Player ID | -121343 (Byte Offset: 0)
Size 	  | 7
Length 	  | 7
SC:R      | Supported

Edited by PereC, 2021.04.12
For SC:R,
In menu - Options - Speed, you can set Key Scroll Speed and Mouse Scroll Speed, each has 7 levels.
For each level, the Scroll Speed has 7 different values, each 1 byte.
level 1: 0x513B68, 0x513B69, 0x513B6A, ..., 0x513B6E
level 2: 0x513B6F, 0x513B70, 0x513B71, ..., 0x513B72
...
level 7: 0x513B92, 0x513B93, 0x513B94, ..., 0x513B98

If you set all the 7 bytes of level2 to 0, then you can't scroll the screen by mouse if you set the Mouse Scroll Speed to level2 in game, but you can still scroll screen by keyboard if Key Scroll Speed is not in level2.
If you set all the 49 bytes to 0, then you can't scroll the screen using mouse or keyboard.

See: https://cafe.naver.com/edac/39325
