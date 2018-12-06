"""Port of the Adafruit NeoPixel library to python using the FTDI MPSSE.

Learn more about NeoPixels here:
  http://learn.adafruit.com/adafruit-neopixel-uberguide/overview

This library is meant to be used with a FT232H USB to MPSSE chip or cable, like
the C232HM-EDHSL-0 here:
  http://www.ftdichip.com/Products/Cables/USBMPSSE.htm

This library requires the libmpsse library to be installed with python support:
  https://code.google.com/p/libmpsse/

Created by Tony DiCola (tony@tonydicola.com)
Released under an MIT license (http://opensource.org/licenses/MIT)

"""

import itertools
import operator
import time
import csv
from mpsse import *
import csv
import pandas as pd
import numpy
from IPython.display import display as ds
import KaboomImages as k
import sneaky as s
import Dropin as d

hashtag1 = "#IMEC18"
hashtag2 = "#GiraMexicoPorSiempre"
hashtag3= "#ToinasMakerRegresa"

intel_blue=[0,0,255]
black=[0,0,0]
white=[255,255,255]
red=[255,0,0] #253,106,2
brown=[218,165,32]

# Open/create a file to append data to
df_current = pd.DataFrame()
df_in = pd.DataFrame()
#csvFile = open('result.csv', 'a')
#Use csv writer

filename='/home/upsquared/Adafruit_NeoPixel_FTDI/tweet.csv'
csvFile = open('/home/upsquared/Adafruit_NeoPixel_FTDI/tweet.csv', 'rb')
csvWriter = csv.writer(csvFile)

imec_image=[1,1,1,2,2,2,2,2,2,2,2,2,2,1,1,2,
2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,2,
1,1,1,1,2,2,2,1,2,2,2,2,2,1,1,1,
2,2,2,1,1,2,1,1,2,2,2,2,2,1,1,1,
2,2,2,1,2,1,2,1,2,2,2,2,2,1,2,1,
2,2,2,1,2,2,2,1,2,2,2,2,2,1,2,1,
2,2,2,2,2,2,2,1,1,1,2,2,2,1,1,1,
2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,
2,2,2,2,2,2,2,1,1,2,2,2,2,2,1,2,
2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,
2,2,2,2,2,2,2,1,1,1,2,2,2,1,1,1,
2,2,2,2,2,2,2,2,2,1,1,1,2,1,2,1,
2,2,2,2,2,2,2,2,2,1,2,2,2,2,1,2,
2,2,2,2,2,2,2,2,2,1,2,2,2,1,2,1,
2,2,2,2,2,2,2,2,2,1,1,1,2,1,1,1]

spy_down=[0,0,2,0,0,0,0,0,0,0,0,0,2,0,0,0,
0,0,2,0,0,2,2,2,2,2,0,0,2,0,0,0,
0,0,2,0,2,1,1,1,1,1,2,0,2,0,0,0,
0,0,2,0,2,1,2,1,2,1,2,0,2,0,0,0,
0,0,2,0,2,1,1,1,1,1,2,0,2,0,0,0,
0,0,2,0,2,1,1,1,1,1,2,0,2,0,0,0,
0,0,2,0,0,2,2,2,2,2,0,0,2,0,0,0,
0,0,0,2,0,0,2,2,2,0,0,2,0,0,0,0,
0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,
0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,
0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,
0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

spy_image=[0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,
	0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,
	0,0,0,1,1,2,2,2,2,2,2,2,1,1,0,0,
	0,0,0,1,1,2,2,2,2,2,2,2,1,1,0,0,
	0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,
	0,0,0,1,1,2,1,1,2,1,1,2,1,1,0,0,
	0,0,0,1,1,2,1,1,2,1,1,2,1,1,0,0,
	0,0,0,1,1,2,2,2,2,2,2,2,1,1,0,0,
	0,0,0,0,1,1,2,2,2,2,2,1,1,0,0,0,
	0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,
	1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
	0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,
	0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,
	0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,
	0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]


# Bit values which represent the zero and one bit pulses.
_ZERO = bytearray([0b11100000])
_ONE  = bytearray([0b11111000])


def _build_byte_lookup():
	"""Return lookup table to map from every byte value 0-255 and the associated
	raw SPI data."""
	lookup = {}
	for i in range(256):
		value = bytearray()
		for j in range(7, -1, -1):
			if ((i >> j) & 1) == 0:
				value += _ZERO
			else:
				value += _ONE
		lookup[i] = value
	return lookup

_byte_lookup = _build_byte_lookup()

def get_default_mpsse(speed_mhz):
	"""Open the first MPSSE device found and return it.  Throws an exception if 
	no MPSSE device is found."""
	from mpsse import MPSSE
	mpsse = MPSSE(SPI0, speed_mhz, MSB)
	if mpsse is None:
		RuntimeError('Could not find a connected MPSSE device!')
	return mpsse

def color(r, g, b):
	"""Convert an RGB triplet of 0-255 values to a 24 bit representation."""
	if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
		raise ValueError('Color values must be 0 to 255.')
	return (r << 16) | (g << 8) | b

def color_to_rgb(c):
	"""Convert a 24 bit color to RGB triplets."""
	return ((c >> 16) & 0xFF, (c >> 8) & 0xFF, c & 0xFF)
def _encode_color_grb(c):
	"""Encode an RGB tuple into NeoPixel GRB 24 byte SPI bit stream."""
	return _byte_lookup[c[1]] + _byte_lookup[c[0]] + _byte_lookup[c[2]]

def _encode_color_rgb(c):
	"""Encode an RGB tuple into NeoPixel RGB 24 byte SPI bit stream."""
	return _byte_lookup[c[0]] + _byte_lookup[c[1]] + _byte_lookup[c[2]]

class Adafruit_NeoPixel(object):
	
	def __init__(self, n, mpsse=None, neo_rgb=False, neo_khz400=False):
		"""Create set of NeoPixels.

		The only required parameter is the number of NeoPixels.  By default the
		first MPSSE device found will be used, and it is assumed to be NeoPixels
		which support 800khz GRB signals.  Set either neo_rgb or neo_khz400
		keywoard parameters to True to use RGB or 400 khz NeoPixels respectively.

		"""
		print('starting Adafruit_NeoPixel class')
		self._n = n
		self._pixels = [0] * n
		# Initialize the mpsse to a default one if not explicitly set.
		if mpsse is None:
			# Default to 6mhz, unless overridden to 3mhz.
			speed = 3000000 if neo_khz400 else 6000000
			mpsse = get_default_mpsse(speed)
		self.setMPSSE(mpsse)
		# Default to GRB encoding, unless overridden to RGB.
		self._encode = _encode_color_rgb if neo_rgb else _encode_color_grb
		self._brightness = 1.0
		self._lastupdate = 0

	def close(self):
		"""Close the NeoPixel MPSSE connection."""
		if self._mpsse is not None:
			self._mpsse.Close()

	def show(self):
		"""Write the current pixel data to the NeoPixels."""
		# Ensure there's at least a 50 micro-second delay between show calls.
		delta = time.time() - self._lastupdate
		if delta < 0.00005:
			time.sleep(0.00005 - delta)
		#print('starting show')
		self._mpsse.Start()
		# Scale pixels based on brightness and accumulate raw SPI bitstream.
		rgb = itertools.imap(color_to_rgb, self._pixels)
		scaled = itertools.imap(lambda c: (int(c[0] * self._brightness),
						   int(c[1] * self._brightness),
						   int(c[2] * self._brightness)),
					rgb)
		encoded = itertools.imap(self._encode, scaled)
		# Send data to the wire.
		self._mpsse.Write(str(reduce(operator.add, encoded)))
		self._mpsse.Stop()
		self._lastupdate = time.time()

	def setMPSSE(self, mpsse):
		"""Change the MPSSE device associated with this NeoPixelimageString instance."""
		if mpsse is None:
			raise ValueError('MPSSE is null.')
		self._mpsse = mpsse

	def setPixelColorRGB(self, n, r, g, b):
		"""Update pixel at position n to the provided RGB color."""
		self.setPixelColor(n, color(r, g, b))

	def setPixelColor(self, n, c):
		"""Update pixel at position n to the provided 24 bit RGB color."""
		self._checkIndex(n)
		if not isinstance(c, int):
			raise ValueError('Expected integer value for color.')
		self._pixels[n] = c

	def setBrightness(self, b):
		"""Scale brightness of NeoPixels to provided value that is between 0 and
		1.0.  A value of 0 is completely dark and 1.0 is normal color brightness.
		Note that brightness is only reflected in the final output shown to the 
		hardware and not getPixels or getPixelColor."""
		if b < 0.0 or b > 1.0:
			raise ValueError('Brightness must be 0 to 1.0.')
		self._brightness = b

	def getPixels(self):
		"""Return all the pixels as an array of 24 bit RGB colors."""
		return self._pixels

	def numPixels(self):
		"""Return the number of NeoPixels."""
		return self._n

	def getPixelColor(self, n):
		"""Return the 24 bit RGB color of the pixel at position n."""
		self._checkIndex(n)
		return self._pixels[n]

	def _checkIndex(self, n):
		if n < 0 or n >= self._n:
			raise ValueError('Pixel id {0} is outside the range of expected values.'.format(n))

def Image_Setup():		
	"""device = Adafruit_NeoPixel(256)		
	device.setBrightness(0.01)"""
	intel_blue=[0,0,255]
	black=[0,0,0]
	white=[255,255,255]
	red=[255,0,0]
	image = []
	for idx in range(len(spy_image)):
		if spy_image[idx] == 0:
			image.append(white)
		if spy_image[idx]== 1:
			image.append(intel_blue)
		if spy_image[idx]== 2:
			image.append(black)
	return image

def Image_Setup_Tag(imageString):	        
	intel_blue=[0,0,255]
	black=[0,0,0]
	white=[255,255,255]
	red=[255,0,0]
	
	image = Translate_Image(imageString)
	return image

def Translate_Image(image_in):
    image_out=[]
    for idx in range(len(image_in)):
        if image_in[idx] == 0:
            image_out.append(white)
        if image_in[idx]== 1:
            image_out.append(intel_blue)
        if image_in[idx]== 2:
            image_out.append(black)
	if image_in[idx]== 3:
            image_out.append(red)
	if image_in[idx]==4:
	    image_out.append(brown)
    return image_out
   
def Free_Image_Setup():
	intel_blue=[0,0,255]
	black=[0,0,0]
	white=[255,255,255]
	red=[255,0,0] #orange = 253,106,2
	free_image = Translate_Image(imec_image)
	print "I am free"
	return free_image

def blit(image, img_width, location, frame_size):
    frame=[black] * frame_size ** 2
    vert_offset=0

    img_lines = [image[x:x+img_width] for x in range(0,len(image),img_width)]
    for line in img_lines:
        for idx, value in enumerate(line):
	    coord = idx+vert_offset+(location[0] % frame_size)+((location[1] % frame_size)*frame_size)
	    # HANDLE EDGE SCROLLING
	    #print coord, idx, vert_offset, (vert_offset+(location[1]*frame_size)+frame_size)-1, location, frame_size
	    if (coord > (vert_offset+(location[1]*frame_size)+frame_size)-1):
		coord = coord - frame_size

	    coord = coord % (frame_size ** 2)
            frame[coord] = value
        vert_offset += frame_size
    return frame

def display(width, frame):

    lines = [frame[x:x+width] for x in range(0,len(frame),width)]
    flipped_frame =[]
    for idx,line in enumerate(lines):
	if idx % 2 == 0:
	    flipped_frame+=reversed(line)
	else:
	    flipped_frame+=line
    
    for idx, color in enumerate(flipped_frame):
	#print idx
	device.setPixelColorRGB(idx, color[0], color[1], color[2])
    device.show()
 
def Vertical_Scroll(image):
	x=0
	y=0
	vert=1
	horiz=0
	while y < 16:
            #frame = blit(image, 3, [x,int(y)], 16)
		frame = blit(image, 16, [x,int(y)], 16)
		print frame		
		display(16, frame)
		time.sleep(0.2)
		y+=1
		
def Horizontal_Scroll(image):
	x=0
	y=0
	vert=0
	horiz=1
	
	while x < 16:
		if x == 0:
			time.sleep(1)
			print "Show before scroll "+ str(x) + " times"
            #frame = blit(image, 3, [x,int(y)], 16)
		frame = blit(image, 16, [x,int(y)], 16)
		#print "me "+ str(x) + " times"
		display(16, frame)
	    	time.sleep(0.2)
		x+=1
def Image_No_Scroll(image):
    x=0
    y=0
    frame = blit(image, 16, [x,int(y)], 16)
    display(16, frame)
    time.sleep(0.2)

def Horizontal_Scroll_opposite(image):
	x=16
	y=0
	vert=0
	horiz=1
	
	while x > 0:
		#print "scrolling backwards"
		if x == 16:
			#time.sleep(1)
			print "Show before scroll "+ str(x) + " times"
            #frame = blit(image, 3, [x,int(y)], 16)
		frame = blit(image, 16, [x,int(y)], 16)
		#print "me "+ str(x) + " times"
		display(16, frame)
	    	time.sleep(0.1)
		x-=1

def show_kaboom():
	
	imageToDisplay= Image_Setup_Tag(k.kaboom_0)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_0)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_1)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_2)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_3)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_4)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_5)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_6)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_7)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_8)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_9)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_10)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_11)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_12)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_13)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_14)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_pre_15)
	Image_No_Scroll(imageToDisplay)
	#Horizontal_Scroll_opposite(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_1)
	Horizontal_Scroll_opposite(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_2)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_3)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_4)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_5)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_6)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_7)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_8)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_9)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_10)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(k.kaboom_11)
	Image_No_Scroll(imageToDisplay)
	print("show kaboom")

def show_sneaky():
	imageToDisplay= Image_Setup_Tag(s.sneaky_0)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_1)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_2)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_3)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_4)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_5)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_6)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_7)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_8)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_9)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_10)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_11)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_12)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_13)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_14)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_15)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_16)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_17)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_18)
	Image_No_Scroll(imageToDisplay)
	ImageToDisplay= Image_Setup_Tag(s.sneaky_19)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_20)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_21)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_22)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_23)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(s.sneaky_24)
	Image_No_Scroll(imageToDisplay)
	print("show sneaky")

def show_dropin():
	#imageToDisplay= Image_Setup("dropin")
	print("show dropin")
	imageToDisplay= Image_Setup_Tag(d.dropin_1)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_2)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_3)
	Image_No_Scroll(imageToDisplay)
	ImageToDisplay= Image_Setup_Tag(d.dropin_4)
	Image_No_Scroll(imageToDisplay)
	ImageToDisplay= Image_Setup_Tag(d.dropin_5)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_6)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_7)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_8)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_9)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_10)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_11)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_12)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_14)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_15)
	Image_No_Scroll(imageToDisplay)
	imageToDisplay= Image_Setup_Tag(d.dropin_16)
	Image_No_Scroll(imageToDisplay)

def show_free():
	imageToDisplay=Free_Image_Setup()
	Image_No_Scroll(imageToDisplay)
	
def find_populartweet(dif_ls):
	spy = 0
	kaboom = 0
	dropin = 0
	sneaky = 0
	
	if (dif_ls.shape[0] > 0):
		print dif_ls
		dif = dif_ls
		dif.columns =['number','tweet','exists']

		kaboom = dif.tweet.str.count("#IMEC18 kaboom").sum()
		print "kaboom: " + str(kaboom)
		
		dropin = dif.tweet.str.count("#IMEC18 drop").sum()
		print "dropin: " + str(dropin)
		
		sneaky = dif.tweet.str.count("#IMEC18 sneaky").sum()
		print "sneaky: " + str(sneaky)
		
		if (kaboom > dropin and kaboom > sneaky):
			print "kaboom wins"
			show_kaboom()
			time.sleep(1)
			show_free()
		if (dropin > sneaky and dropin > kaboom):
			print "dropin wins"
			show_dropin()
			time.sleep(1)
			show_free()

		if (sneaky > kaboom and sneaky > dropin):
			print "sneaky wins"
			show_sneaky()
			time.sleep(1)
			show_free()
#Dataframe code

def printdiffs(df_in):	
	diff_df = find_diffs(df_in)
	return diff_df
	
def find_diffs(df_in):	
	diff_df = pd.DataFrame()
	df_latest = pd.read_csv(filename)
	print 'old dataframe size is' + str(df_in.size)
	print 'new dataframe size is' + str(df_latest.size)
		
	diff_df = pd.merge(df_latest, df_in, how='outer', indicator='Exist')
	diff_df = diff_df.loc[diff_df['Exist'] != 'both']

	
	"""if diff_df.size > 0:

		print 'diff found' + str(diff_df.size)		

		df_current = df_latest

		print df_current

		ds_list = df_latest.values[-1].tolist()

		print ds_list[1]	"""
	return diff_df
if __name__ == "__main__":
	device = Adafruit_NeoPixel(256)	
	device.setBrightness(0.01)
	df_last = pd.DataFrame()	
	df_in = pd.read_csv(filename)	
	i=0
	imageToDisplay=[]

	while True:  
		print("Polling Tweets")
		show_free()
		#print ("tweet caught " + str(df_last.size))
		dif_ls= printdiffs(df_in)
				
		if (dif_ls.shape[0] > 0):
			find_populartweet(dif_ls) 
			print str((dif_ls._slice(slice(0, None))))
			if ('#IMEC18 spy' in str(dif_ls._slice(slice(0, None)))):
				print ("show spy")
			if ('#IMEC18 kaboom' in str((dif_ls._slice(slice(0, None))))):
				print("show kaboom")
			if ('#IMEC18 drop' in str((dif_ls._slice(slice(0, None))))):
				print("show drop-in")
			if ('#IMEC18 sneaky' in str((dif_ls._slice(slice(0, None))))):
				print("show sneaky")
            		df_in = pd.read_csv(filename)
        	print  "waiting 10 seconds"
		time.sleep(5)



		

	"""device = Adafruit_NeoPixel(256)		
	device.setBrightness(0.01)
	df_last = pd.DataFrame()
	df_in = pd.DataFrame()
	df_in = pd.read_csv(filename)	 
	i=0
	
	while True:   
		print("Polling Tweets")
		df_in= printdiffs(df_in)
		time.sleep(7)
		i = i +1 
	
		if (df_in.size >> 1):			
			imageToDisplay=Image_Setup()
			print("tweet received")
			print(imageToDisplay)
			Horizontal_Scroll(imageToDisplay)
		else:
			imageToDisplay=Free_Image_Setup()
			print("no tweet")
			print(imageToDisplay)
			Horizontal_Scroll(imageToDisplay)

		#time.sleep(0.5)
	#Go back and make sure that when there is more than one  tweet we display all"""
