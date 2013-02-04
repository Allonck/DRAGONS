
#for line in tlines:
# ss=line.split()
# print "(%-10r,%7r,%12r): %.1f,"%(ss[0],ss[1],ss[2],float(ss[3]))

yoffsets = {    # from gemini-iraf/f2/f2offsets.fits
 # __grism___ __filter__ ___slit___r: _yoffset_ (pixels)
('HK_G5802', 'HK',      '1pix-slit'): -100.0,
 ('HK_G5802', 'HK',      '2pix-slit'): -100.0,
 ('HK_G5802', 'HK',      '3pix-slit'): -100.0,
 ('HK_G5802', 'HK',      '4pix-slit'): -100.0,
 ('HK_G5802', 'HK',      '6pix-slit'): -100.0,
 ('HK_G5802', 'HK',      '8pix-slit'): -100.0,
 ('HK_G5802', 'HK',      'mos'):       -100.0,
 ('HK_G5802', 'JH',      '1pix-slit'): 34.0,
 ('HK_G5802', 'JH',      '2pix-slit'): 34.0,
 ('HK_G5802', 'JH',      '3pix-slit'): 34.0,
 ('HK_G5802', 'JH',      '4pix-slit'): 34.0,
 ('HK_G5802', 'JH',      '6pix-slit'): 34.0,
 ('HK_G5802', 'JH',      '8pix-slit'): 34.0,
 ('HK_G5802', 'JH',      'mos'):       34.0,
 ('JH_G5801', 'JH',      '1pix-slit'): -75.0,
 ('JH_G5801', 'JH',      '2pix-slit'): -75.0,
 ('JH_G5801', 'JH',      '3pix-slit'): -75.0,
 ('JH_G5801', 'JH',      '4pix-slit'): -75.0,
 ('JH_G5801', 'JH',      '6pix-slit'): -75.0,
 ('JH_G5801', 'JH',      '8pix-slit'): -75.0,
 ('JH_G5801', 'JH',      'mos'):       -75.0,
 ('R3K_G5803', 'H',      '1pix-slit'): 175.0,
 ('R3K_G5803', 'H',      '2pix-slit'): 175.0,
 ('R3K_G5803', 'H',      '3pix-slit'): 175.0,
 ('R3K_G5803', 'H',      '4pix-slit'): 175.0,
 ('R3K_G5803', 'H',      '6pix-slit'): 175.0,
 ('R3K_G5803', 'H',      '8pix-slit'): 175.0,
 ('R3K_G5803', 'H',      'mos'):       175.0,
 ('R3K_G5803', 'J',      '1pix-slit'): 350.0,
 ('R3K_G5803', 'J',      '2pix-slit'): 350.0,
 ('R3K_G5803', 'J',      '3pix-slit'): 350.0,
 ('R3K_G5803', 'J',      '4pix-slit'): 350.0,
 ('R3K_G5803', 'J',      '6pix-slit'): 350.0,
 ('R3K_G5803', 'J',      '8pix-slit'): 350.0,
 ('R3K_G5803', 'J',      'mos'):       350.0,
 ('R3K_G5803', 'J-lo',   '1pix-slit'): -20.0,
 ('R3K_G5803', 'J-lo',   '2pix-slit'): -20.0,
 ('R3K_G5803', 'J-lo',   '3pix-slit'): -20.0,
 ('R3K_G5803', 'J-lo',   '4pix-slit'): -20.0,
 ('R3K_G5803', 'J-lo',   '6pix-slit'): -20.0,
 ('R3K_G5803', 'J-lo',   '8pix-slit'): -20.0,
 ('R3K_G5803', 'J-lo',   'mos'):       -20.0,
 ('R3K_G5803', 'Ks',     '1pix-slit'): 126.0,
 ('R3K_G5803', 'Ks',     '2pix-slit'): 126.0,
 ('R3K_G5803', 'Ks',     '3pix-slit'): 126.0,
 ('R3K_G5803', 'Ks',     '4pix-slit'): 126.0,
 ('R3K_G5803', 'Ks',     '6pix-slit'): 126.0,
 ('R3K_G5803', 'Ks',     '8pix-slit'): 126.0,
 ('R3K_G5803', 'Y',      '1pix-slit'): 610.0,
 ('R3K_G5803', 'Y',      '2pix-slit'): 610.0,
 ('R3K_G5803', 'Y',      '3pix-slit'): 610.0,
 ('R3K_G5803', 'Y',      '4pix-slit'): 610.0,
 ('R3K_G5803', 'Y',      '6pix-slit'): 610.0,
 ('R3K_G5803', 'Y',      '8pix-slit'): 610.0,
 ('R3K_G5803', 'Y',      'mos'):       610.0}

#f2filters.fits

#filter   center width cuton80 cutoff80 cuton50 cutoff50 transmission (units in microns)

filter_table = {
'Y':   (1.020 ,0.0894 ,0.985 ,1.066 ,0.969 ,1.068 ,'Y_G0811.dat'),
'J-lo': (1.122 ,0.1323 ,1.056 ,1.189 ,1.048 ,1.192 ,'Jlow_G0801.dat'),
'J':   (1.256 ,0.1512 ,1.178 ,1.328 ,1.175 ,1.333 ,'J_G0802.dat'),
'H':   (1.631 ,0.2741 ,1.490 ,1.767 ,1.486 ,1.775 ,'H_G0803.dat'),
'Ks':   (2.157 ,0.3177 ,1.997 ,2.313 ,1.991 ,2.320 ,'Ks_G0804.dat'),
'JH':   (1.390 ,0.7200 ,1.163 ,1.774 ,0.970 ,1.805 ,'JH_G0809.dat'),
'HK':   (1.871 ,1.0670 ,1.308 ,2.401 ,1.261 ,2.511 ,'HK_G0806.dat'),
}

