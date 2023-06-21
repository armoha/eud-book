
#  Weapons.dat - Target Flags
Address   | 657998
----------|-------------
Player ID | 210317 (Byte Offset: 0)
Size 	  | 2
Length 	  | 130
SC:R      | Simple Data

0x001 Air
0x002 Ground
0x004 Mechanical
0x008 Organic
0x010 non-Building
0x020 non-Robotic
0x040 Terrain
0x080 Organic or Mechanical
0x100 Own

This is actually better thought of "which units can this weapon deal damage to". Eg if you give a ground weapon the air + ground target as well as splash, then when it attacks a ground unit, any air units in the vicinity will also take splash damage. If you also set it to have Mechanical targeting, then the weapon will be able to attack all types of ground units, but only deal damage to ones with the mechanical flag.
