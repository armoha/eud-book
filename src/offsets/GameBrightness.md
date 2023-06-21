#  Game Brightness
Address   | 657A9C
----------|-------------
Player ID | 210382 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | Simple Data

Darkens the screen without affecting UI elements. Appears to be a modifier for Fog of War Masks? Technically a 1 byte value, but the high bytes are padding and not used.

Valid values are 0-31, with 0 being black and 31 being maximum brightness. Values >31 appear to just be black.

The value appears to be the index in tileset\*\dark.pcx remapping palette.
