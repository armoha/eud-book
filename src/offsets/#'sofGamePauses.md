#  #'s of Game Pauses
Address   | 58D718
----------|-------------
Player ID | 3309 (Byte Offset: 0)
Size 	  | 1
Length 	  | 8
SC:R      | Simple Data

The base value of this address is: (P1 + P2 + P3 + P4) * 3 = 50529027

Player 1: *1 
Player 2: *256 
Player 3: *65536 
Player 4: *16777216 

Player 1, 2, 3, and 4 all have three remaining game pauses that they can use to stop the game from running temporarily. If Player 2 were to pause the game, and have only two remaining game pauses left as a result, the new value of the address is: 50529027 - 256 = 50528771.

The same as EPD 3310, except: 

Player 5: *1 
Player 6: *256 
Player 7: *65536 
Player 8: *16777216 

Challenge (Try it) - Create a easy formula from all of the information given.
