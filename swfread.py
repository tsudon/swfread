#!/usr/bin/python
# SWF File TAG READER ( - v19)
# use python 2.7 ,not test Python3
# 2018/09/01-02 created by tsudon

import struct
import zlib
import io
import sys

class ByteReader:
	
	def __init__ (self,path):
		self.f = open (path,"rb") 
		self.bitoffset = 0
		
	def __del__(self):
		self.f.close

#File after header decode all
	def setCompressed(self):
		buf = zlib.decompress(self.f.read())
		self.f.close
		self.f = io.BytesIO(buf) 
	
	def getByte(self):
		byte = struct.unpack('<B', self.f.read(1))[0]
		return byte
		
	def getBytes(self,num):
		return self.f.read(num)	

	def getUINT16(self):
		num	=	struct.unpack('<H',self.f.read(2))[0]
		return num

	def getTag(self):
		num = self.getUINT16()
		tag = (num >> 6) & 0x3ff
		if ( num & 0x3f == 0x3f):
			length = self.getUINT32()
		else:
			length = num & 0x3f
		return (tag,length)

	def getSINT16(self):
		num=	struct.unpack('<h',self.f.read(2))[0]
		return num

	def getUINT32(self):
		num	=	struct.unpack('<L',self.f.read(4))[0]
		return num

	def getSINT32(self):
		num	=	struct.unpack('<l',self.f.read(4))[0]
		return num
		
	def getUINT64(self):
		num	=	struct.unpack('<Q',self.f.read(8))[0]
		return num

	def getSINT64(self):
		num	=	struct.unpack('<q',self.f.read(8))[0]
		return num

#no debug
	def getFIXED(self):
		num0 = struct.unpack('<H',self.f.read(2))[0]
		num1 = struct.unpack('<h',self.f.read(2))[0]
		return (num1,num0)

#no debug
	def getFIXED8(self):
		num0=	struct.unpack('<B',self.f.read(1))[0]
		num1=	struct.unpack('<b',self.f.read(1))[0]
		return (num1,num0)

#do not test
	def getFloat16(self):
		# for Python 3.6 and lator
		num	=	struct.unpack('<2',self.f.read(2))[0]
		return num

#do not test
	'''
		num = self.getUINT16()
		if (num & 0x8000) == 0x8000:
			sign = -1
		else:
			sign = +1
		exp = (num >> 10) & 0x001f
		frac = float(num & 0x03ff)
		if exp == 0:
			num = sign * 2**(-14) * (frac * 2**-10)	
		elif exp == 0x1f:
			num = float('inf') * sign
		else:
			exp -= 15
			num = sign * 2**(exp-15) * (1 + (frac * 2**-10) )
		return num
	'''

	def getFloat32(self):
		num	=	struct.unpack('<f',self.f.read(4))[0]
		return num

	def getDouble(self):
		num	=	struct.unpack('<d',self.f.read(8))[0]
		return num

# return UI[Nbit]
	def getBits(self,bits):
		if (bits <= 0):
			return 0
		num = 0

		if (self.bitoffset <= 0)  :
			self.byte = self.getByte()
			self.bitoffset = 8
	
		byte = self.byte
		if (bits <= self.bitoffset):
			mask = (1 << bits) -1
			self.bitoffset -= bits
			num = byte >> self.bitoffset
			return num & mask 
			
		mask = (1 << (self.bitoffset)) -1
		num = (byte  & mask)
		nextbits = bits - self.bitoffset
		self.bitoffset = 0
		return (num << nextbits) | self.getBits(nextbits) 

#no debug
	def getUB(self,bits):
		return self.getBits(bits)	

	def getSB(self,bits):
		num = self.getBits(bits)
		if  num & 1<<(bits-1) ==0:
			return self.getBits(bits)	
		num = num & (1<<(bits-1) -1 ) # if nbit=4 , num = num & 0x7 
		return   num  - (1<bits -1)  # if nbit=4, 0x0f=-1 0x0e = -2 ... 0x10 = -7 , 0x08 = 8

	def getFB(self,bits): 
		num = self.getBits(bits)
		## make FIX16.16 SINGED
		num1 = num &0xfffff
		bits -= 16
		num0 = num >> 16
		if  num & 1<<(bits-1) !=0:
			num = num & (1<<(bits-1) -1 ) 
			num0 = num0 - (1<bits -1) 
		return (num0,num1)

#def getEncodedU32(self):

	def bitclear(self):
		self.bitoffset = 0

# Logger
def Logger(s):
	print (s)
	
def End(reader,length):
	return


def ShowFrame(reader,length):
	return


def DefineShape(reader,length):
	return


def PlaceObject(reader,length):
	return


def RemoveObject(reader,length):
	return


def DefineBits(reader,length):
	return


def DefineButton(reader,length):
	return


def JPEGTables(reader,length):
	return


def SetBackgroundColor(reader,length):
	return


def DefineFont(reader,length):
	return


def DefineText(reader,length):
	return


def DoAction(reader,length):
	return


def DefineFontInfo(reader,length):
	return


def DefineSound(reader,length):
	return


def StartSound(reader,length):
	return


def DefineButtonSound(reader,length):
	return


def SoundStreamHead(reader,length):
	return


def SoundStreamBlock(reader,length):
	return


def DefineBitsLossless(reader,length):
	return


def DefineBitsJPEG2(reader,length):
	return


def DefineShape2(reader,length):
	return


def DefineButtonCxform(reader,length):
	return


def Protect(reader,length):
	return


def PlaceObject2(reader,length):
	return


def RemoveObject2(reader,length):
	return


def DefineShape3(reader,length):
	return


def DefineText2(reader,length):
	return


def DefineButton2(reader,length):
	return


def DefineBitsJPEG3(reader,length):
	return


def DefineBitsLossless2(reader,length):
	return


def DefineEditText(reader,length):
	return


def DefineSprite(reader,length):
	return


def FrameLabel(reader,length):
	return


def SoundStreamHead2(reader,length):
	return


def DefineMorphShape(reader,length):
	return


def DefineFont2(reader,length):
	return


def ExportAssets(reader,length):
	return


def ImportAssets(reader,length):
	return


def EnableDebugger(reader,length):
	return


def DoInitAction(reader,length):
	return


def DefineVideoStream(reader,length):
	return


def VideoFrame(reader,length):
	return


def DefineFontInfo2(reader,length):
	return


def EnableDebugger2(reader,length):
	return


def ScriptLimits(reader,length):
	return


def SetTabIndex(reader,length):
	return


def FileAttributes(reader,length):
	return


def PlaceObject3(reader,length):
	return


def ImportAssets2(reader,length):
	return


def DefineFontAlignZones(reader,length):
	return


def CSMTextSettings(reader,length):
	return


def DefineFont3(reader,length):
	return


def SymbolClass(reader,length):
	return


def Metadata(reader,length):
	return


def DefineScalingGrid(reader,length):
	return


def DoABC(reader,length):
	return


def DefineShape4(reader,length):
	return


def DefineMorphShape2(reader,length):
	return


def DefineSceneAndFrameLabelData(reader,length):
	return


def DefineBinaryData(reader,length):
	return


def DefineFontName(reader,length):
	return


def StartSound2(reader,length):
	return


def DefineBitsJPEG4(reader,length):
	return


def DefineFont4(reader,length):
	return

def EnableTelemetry(reader,length):
	return



TAG = {
	0:End,
	1:ShowFrame,
	2:DefineShape,
	4:PlaceObject,
	5:RemoveObject,
	6:DefineBits,
	7:DefineButton,
	8:JPEGTables,
	9:SetBackgroundColor,
	10:DefineFont,
	11:DefineText,
	12:DoAction,
	13:DefineFontInfo,
	14:DefineSound,
	15:StartSound,
	17:DefineButtonSound,
	18:SoundStreamHead,
	19:SoundStreamBlock,
	20:DefineBitsLossless,
	21:DefineBitsJPEG2,
	22:DefineShape2,
	23:DefineButtonCxform,
	24:Protect,
	26:PlaceObject2,
	28:RemoveObject2,
	32:DefineShape3,
	33:DefineText2,
	34:DefineButton2,
	35:DefineBitsJPEG3,
	36:DefineBitsLossless2,
	37:DefineEditText,
	39:DefineSprite,
	43:FrameLabel,
	45:SoundStreamHead2,
	46:DefineMorphShape,
	48:DefineFont2,
	56:ExportAssets,
	57:ImportAssets,
	58:EnableDebugger,
	59:DoInitAction,
	60:DefineVideoStream,
	61:VideoFrame,
	62:DefineFontInfo2,
	64:EnableDebugger2,
	65:ScriptLimits,
	66:SetTabIndex,
	69:FileAttributes,
	70:PlaceObject3,
	71:ImportAssets2,
	73:DefineFontAlignZones,
	74:CSMTextSettings,
	75:DefineFont3,
	76:SymbolClass,
	77:Metadata,
	78:DefineScalingGrid,
	82:DoABC,
	83:DefineShape4,
	84:DefineMorphShape2,
	86:DefineSceneAndFrameLabelData,
	87:DefineBinaryData,
	88:DefineFontName,
	89:StartSound2,
	90:DefineBitsJPEG4,
	91:DefineFont4,
	93:EnableTelemetry
}

if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	print("Usage: swfread.py [filename]")
	sys.exit(1)

reader = ByteReader(path)

#CWS or FWS
header =  bytearray()
header.append( reader.getByte())
header.append( reader.getByte())
header.append( reader.getByte())
header = header.decode('ascii','ignore')
Logger("Signature:" + header)


#SWF version
version = reader.getByte()
Logger("Version:" +str(version))

#File length
filelength = reader.getUINT32()
Logger("FIlelegth:" + str(filelength))

if (header == 'FWS') : 
	Logger('Uncompressed data')
elif (header == 'CWS') : 
	Logger('Compressed data')
	reader.setCompressed() #If swf file is compressed, decode ZLIB
else:
	Logger('unknown')
	sys.exit(-1)

#Frame Size
nbits = reader.getBits(5)

Logger ("Nbits" + str(nbits))

x_min = reader.getBits(nbits)
x_max = reader.getBits(nbits)
y_min = reader.getBits(nbits)
y_max = reader.getBits(nbits)
reader.bitclear()

Logger("RECT(x20 pixels):" + str(x_min)  + "," + str(y_min)   + "," + str(x_max)   + "," + str(y_max)    )

framerate = reader.getUINT16()
framecount = reader.getUINT16()

Logger( str(framerate)  + "fps  count:" + str(framecount))

#Read TAG
while True:
	(tag,length) = reader.getTag()
	Logger( TAG[tag].__name__ + ":" + str(length) + "byte")
	reader.getBytes(length)
	if tag == 0:
		break

Logger('EOF')

