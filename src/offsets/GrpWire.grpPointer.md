#  GrpWire.grp Pointer
Address   | 68C1FC
----------|-------------
Player ID | 264102 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | Backed By Code

Overwriting a particular unit's frame offset with a different frame offset can change the image used for that unit.

GRP header:
u16 frameCount
u16 width
u16 height

GRP Frame (* frameCount)
u8 x
u8 y
u8 w
u8 h
u32 offset
