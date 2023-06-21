
#  Trigger Current Player  aka CP Trick
Address   | 6509B0
----------|-------------
Player ID | 203155 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | Simple Data

Used to dynamically run EUDs or dereference pointers.

Sets "Current Player" in triggers to be a reference to a different base address for the deaths table.

e.g.
Set Deaths("Int:203155", "Terran Marine", Set to, EPD);
Set Deaths("Int:203155", "Terran Marine", Add/Subtract, whatever);
Set Deaths("Current Player", "Terran Marine", Set to/Add/Subtract, whatever);


Example: Implement Set Minerals for current player
// Add -11421 to 0x006509B0 (player ID corresponding to 0x0057F0F0) 
SetMemory(0x6509B0, Add, 0xFFFFD363);
// Add 50 to byte offset for that address -- current player will increase target address by 4 bytes for each player that runs it
SetDeaths(CurrentPlayer, Add, 50, "Terran Marine");
// Add +11421 to 0x006509B0 to set it back to what it was
SetMemory(0x6509B0, Add, 0x00002C9D);


Example: Implement a SetKills action for Current Player
// Add -2736 to 0x6509B0 (player ID corresponding to 0x005878A4)
SetMemory(0x6509B0, Add, 0xFFFFF550);
// Current player combined with unit ID now references the correct target address in the Kills table)
// This SetDeaths is now really SetKills to add/subtract/set to for unit of choice
SetDeaths(CurrentPlayer, Subtract, 1, "Terran Ghost");
// Add +2736 to 0x006509B0 to set it back to what it was
SetMemory(0x6509B0, Add, 0x00000AB0);
Note: Set Deaths needs to be for current player, P1/P2/etc. would modify the normal deaths table.
Note2: Cannot use Any Unit/Men/Buildings/Factories for the unit, those do have Unit IDs, are not stored in the Kills table, and would overflow into other areas.
