
#  Fog of War Masks
Address   | 657AA0
----------|-------------
Player ID | 210383 (Byte Offset: 0)
Size 	  | 1
Length 	  | 4096
SC:R      | Backed By Code

Sets the brightness parts of the fog of war masks. Corresponds to dark.pcx indexes, with valid values from 0 (black) to 31 (full brightness). Values >31 in 1.16.1 are glitched colors.

4 bytes at 0x00657AA0 correspond to unexplored fog.
4 bytes at 0x0065825C correspond to explored areas in fog.
4 bytes at 0x00658A9C correspond to visible areas.
Other addresses relate to the transitions between these areas.

Setting to 0x1F1F1F1F will fully clear the mask, though units and buildings may not be visible or selectable depending on the actual fog state. Additionally, using different values for each byte, e.g. 0x1F001F00, will create vertical stripes (tested in 1.16.1).
