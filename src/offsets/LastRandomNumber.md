
#  Last Random Number
Address   | 51CA14
----------|-------------
Player ID | -112212 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | Simple Data

Randomization seed for the next random number, mask with 0x7FFF0000 for the last returned number.

int getRandomNumber(){
  lastRandomNumber = lastRandomNumber * 0x15A4E35 + 1;
  return (lastRandomNumber >> 16) & 0x7FFF;
}
