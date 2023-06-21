#  Hotkeyed Unit
Address   | 57FE60
----------|-------------
Player ID | -10561 (Byte Offset: 0)
Size 	  | 864
Length 	  | 8
SC:R      | Simple Data

Purpose


To detect the hotkey and then the slot that a unit is stored in and/or the unit 

that is stored in a slot within a hotkey for any player. 


Math


The total amount of units that can be hotkeyed
is 12.

There are 18 hotkeys in existence.

12 * 18 = 108 

108 is the total amount of EPD values for each
player.

	If we want to check if there's a unit in the
	seventh slot within the hotkey CTRL+0 for
	Player 1, 

	-10561 + 7 = -10555.

	If we want to check if there's a unit in the
	first slot within the hotkey CTRL+1 for Player
	1,

	-10561 + 12 = -10550.

	If we want to check if there's a unit in
	the first slot within the hotkey CTRL+0 for
	Player 2,

	-10561 + 109 = -10452.

12 * 9 * 8 = 864

864 is the total combined number of all players' EPD
value.

	We can check any slots within any hotkeys for 
	any player to detect if any unit exist. 

		At least 1

	We can check any slots within any hotkeys for
	any player to detect if no unit exist.

		At least 3749

	but what if we want to detect if a specific unit
	within the map is hotkeyed in a certain slot?
                       
Unit alpha ID (Unit Entity)

Index #        Alpha ID
0	       2049
1	       3748 [+1700]
2	       3747 [-1]
3	       3746 [-1]

Confused? Hint: http://www.staredit.net/topic/14226/ (Read Section 6)

^^^^^^^Parts of this seem to be wrong.

This is the magic formula:
with the variables

p = player number (starting at 0 up to 7)
h = hotkey number
i = index in a hotkey (starting at 0 up to 11)
u = unit id

then if player p has unit u hotkeyed in index i of hotkey h, we have, for u > 0
memory(-10561+(p*216)+(h*12)+i) == 3749 - u,
and for u = 0,
memory(-10561+(p*216)+(h*12)+i) == 2049.

==============
Edited by PereC, 2021.06.25:
Each u32 stores the Alpha ID of a hotkeyed unit:
Starting from 0x57FE60: All the hotkeyed unit of P1
0x57FE60: Alpha ID of the 1st unit in P1 hotkey 0
0x57FE64: Alpha ID of the 2nd unit in P1 hotkey 0
0x57FE68: Alpha ID of the 3rd unit in P1 hotkey 0
...
0x57FE60 + 4 * 11: Alpha ID of the 12th unit in P1 hotkey 0
0x57FE60 + 4 * 12: Alpha ID of the 1st unit in P1 hotkey 1
0x57FE60 + 4 * 13: Alpha ID of the 2nd unit in P1 hotkey 1
...
0x57FE60 + 4 * 119: Alpha ID of the 12th unit in P1 hotkey 9
From 0x57FE60 + 4 * 120 to 0x57FE60 + 4 * 216: ??????
-----------
Starting from 0x57FE60 + 216: All the hotkeyed unit of P2
-----------
Starting from 0x57FE60 + 216 * 2: All the hotkeyed unit of P3
-----------
...
-----------
Starting from 0x57FE60 + 216 * 7: All the hotkeyed unit of P8
-----------

Personally I don't know why there are 864 bytes for each player. Intuitively there should be 4 * 12 * 10 = 480 bytes for each player, cuz there are 10 hotkeys and 12 units within a hotkey.



======================================
Further written by AINukeHere. (2021.08.24)
The above is very confusing because there are many wrong parts.

There are 12 unit slots for each hotkey, and each unit ID (Alpha ID) is 4 bytes.
That is, 48 bytes per hotkey.
Each player holds 18 hotkeys.
The 10 hotkeys (indices 0 to 9) are hotkeys designated by Ctrl+Number.
The remaining 8 (indices 10 to 17) hotkeys are units that are automatically saved whenever multiple units are selected.
It can be selected with Alt+Left Mouse Click.

So the allocated memory per player is 4*12*18 = 864 bytes.
