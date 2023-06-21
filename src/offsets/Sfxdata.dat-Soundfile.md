#  Sfxdata.dat - Sound file
Address   | 68DAA0
----------|-------------
Player ID | 265679 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1144
SC:R      | 

Direct pointer to SFXData.tbl string. This can be changed as long as the wav hasn't been loaded. This means that any wav without the 'preload' flag should be able to be pointed to a different wav file.
