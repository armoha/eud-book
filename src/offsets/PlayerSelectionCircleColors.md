#  Player Selection Circle Colors
Address   | 581D6A
----------|-------------
Player ID | -8575 (Byte Offset: 2)
Size 	  | 1
Length 	  | 12
SC:R      | Simple Data

Each byte sets the color of the selection circle:
000 - Green
001 - Yellow
002 - Red
017 - Grey Blue*
136 - Light Grey*
138 - Dark Grey*
Higher values can give different colors (most give solid black.) Asterisk colors are inconsistent.

p1 = -8575 with mask 0x00FF0000
p2 = -8575 with mask 0xFF000000
p3 = -8574 with mask 0x000000FF
p4 = -8574 with mask 0x0000FF00
p5 = -8574 with mask 0x00FF0000
p6 = -8574 with mask 0xFF000000
p7 = -8573 with mask 0x000000FF
p8 = -8573 with mask 0x0000FF00
p9 = -8573 with mask 0x00FF0000
p10 = -8573 with mask 0xFF000000
p11 = -8572 with mask 0x000000FF
p12 = -8572 with mask 0x0000FF00
