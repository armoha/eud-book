
#  CUnit - Status Flags
Address   | 59CD84
----------|-------------
Player ID | 19080 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | Supported

https://github.com/bwapi/bwapi/blob/master/bwapi/BWAPI/Source/BW/UnitStatusFlags.h
0x00000001 - Completed
0x00000002 - GroundedBuilding (Building on the ground)
0x00000004 - In Air
0x00000008 - Disabled (Protoss unpowered)
0x00000010 - Burrowed
0x00000020 - In Building
0x00000040 - In Transport
0x00000080 - Unknown (Target acquisition)
0x00000100 - Requires detection
0x00000200 - Cloaked
0x00000400 - Doodad State thing
0x00000800 - Cloaking for free (no energy to cloak)
0x00001000 - Cannot receive orders
0x00002000 - NoBrkCodeStart (Iscript)
0x00004000 - Unknown
0x00008000 - Cannot Attack (unknown)
0x00010000 - Is A Unit
0x00020000 - Is A Building
0x00040000 - Ignore Tile Collision
0x00080000 - Unknown
0x00100000 - Is Normal (set for normal units, not set for hallucinated units)
0x00200000 - No Collide
0x00400000 - unknown
0x00800000 - Is Gathering
0x01000000 - unknown
0x02000000 - unknown (turret related)
0x04000000 - Invincible
0x08000000 - Holding Position
0x10000000 - Speed Upgrade
0x20000000 - Cooldown Upgrade
0x40000000 - Is Hallucination (set for hallucinated units, not set for normal units)
0x80000000 - Is Self Destructing (Set for when the unit is self-destructing (scarab, scourge, infested terran))

Offset from CUnit Base: 0xDC (= 0x0059CD84 - 0x0059CCA8)
