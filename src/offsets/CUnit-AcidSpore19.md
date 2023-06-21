#  CUnit - Acid Spore 1/9
Address   | 59CDCF
----------|-------------
Player ID | 19098 (Byte Offset: 3)
Size 	  | 1
Length 	  | 1
SC:R      | See Description

[SCR: Other acid spore timers are NOT supported and give EUD errors on access]

Timer for 1st of 9 acid spores applied to a unit (*16777216)

Initialised to 150 (2,516,582,400). Timers decay 1 tick per 8 frames, so 150 / 2.9762 = 50.4 RL seconds on Fastest.

This is the timer for the first acid spore that hits a target, you can reduce the value and the spore will decay quickly as expected. 

When a 2nd spore is applied that timer is recorded separately and independently. The first spore will decay as per its timer and the 2nd one decays based on its timer.
