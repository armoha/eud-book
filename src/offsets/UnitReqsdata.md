#  Unit Reqs data
Address   | 514178
----------|-------------
Player ID | -120955 (Byte Offset: 0)
Size 	  | 1090
Length 	  | 1
SC:R      | Simple Data

Packed list of opcodes/parameters for data requiremens.

First u16 is the unit ID for the script, followed by the script. 0x##FF is an opcode, 0x##00 is a parameter, FFFF is the end of the script.
