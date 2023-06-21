
#  CUnit - HP
Address   | 59CCB0
----------|-------------
Player ID | 19027 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | Supported

Amount of HP that a unit currently has.

Value displayed in-game is divided by 256.  For example, a Marine that has 40 HP in-game would have 10240 or 0x2800 HP in memory.

Offset from unit index address: 0x08
Unit Index 0 HP = 0x0059CCA8 + 0x08 = 0x0059CCB0
Unit Index 1 HP = 0x00628298 + 0x08 = 0x006282A0
Unit Index 2 HP = 0x00628148 + 0x08 = 0x00628150

Example: Regenerate HP for unit at index 2 to a max of 100 HP

Unit Index 2 HP = 0x00628148 + 0x08 = 0x00628150

Trigger("Player 1"){
Conditions:
  // HP is less than 100
  MemoryAddr(0x628150, At most, 25599);

Actions:
  // Add 16/256 HP
  MemoryAddr(0x628150, Add, 16);
  Preserve Trigger();
}

//-----------------------------------------------------------------//

Trigger("Player 1"){
Conditions:
  // HP is over 100
  MemoryAddr(0x628150, At least, 25601);

Actions:
  // Set to 100 HP
  MemoryAddr(0x628150, Set To, 25600);
  Preserve Trigger();
}
