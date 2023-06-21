#  Units.dat - Building Dimensions
Address   | 662860
----------|-------------
Player ID | 221503 (Byte Offset: 0)
Size 	  | 4
Length 	  | 228
SC:R      | Simple Data

Struct:
2 bytes - Width
2 bytes - Height

Setting to 0 will make the unit (not just buildings) invisible:
- It won't appear on the minimap
- It won't appear on the main map
- It can't be selected by the mouse in any way
- 'Bring' triggers will not locate it
- Units can still attack (and will display missile graphics)
- Units still cause and are affected by collision
- Units can't be targetted by other units

This dimension is used when determining if units with the Building flag can fit in the available spaace. Units without the Building flag will rely on their collision dimensions instead.

Setting this to a size of 31x31 or smaller will allow buildings to be built on any terrain, including water and cliffs, although the placement mechanics are a little wonky.
