# READTC8
#(c) 2026  David Shadoff
#
# Program to read TC-8 encoded WAV files from TRS-80 Model 1 using TC-8
#
# Currently verified to read BINARY files
# Currently limited to 44100 Hz WAV files using Mono input (only one channel)


import os
import sys


POSITIVE            = 1
NEGATIVE            = -1
SAMPLE_BYTES        = 2
HALFWAVE_THRESHOLD  = 13


def read_int4(ptr, mem_block):
    byte1 = mem_block[ptr]
    byte2 = mem_block[ptr+1]
    byte3 = mem_block[ptr+2]
    byte4 = mem_block[ptr+3]
    value = (byte4 * 16777216) + (byte3 * 65536) + (byte2 * 256) + byte1
    return(value)

def read_int2(ptr, mem_block):
    byte1 = mem_block[ptr]
    byte2 = mem_block[ptr+1]
    value = (byte2 * 256) + byte1
    return(value)

def get_nextsample(mem_block):
    global fileptr
    global filesize

    if (fileptr >= filesize):
        print("END OF FILE FOUND")
        exit()
    nextval = read_int2(fileptr, mem_block)
    if nextval > 32767:
        nextval = nextval - 65536
    fileptr = fileptr + 2
    return(nextval)

def get_halfwave(mem_block):
    global fileptr
    global polarity
    global wavestart

    wavelength = 0
    while (True):
        val = get_nextsample(mem_block)
        if ((polarity == POSITIVE) and (val < 0)) or ((polarity == NEGATIVE) and (val > 0)):
            wavelength = int((fileptr - wavestart)/SAMPLE_BYTES)
            wavestart = fileptr
            if (val > 0):
                polarity = POSITIVE
            else:
                polarity = NEGATIVE
            break

    return(wavelength)

def get_bit(mem_block):
    halfwavelen = get_halfwave(mem_block)
    if (halfwavelen > HALFWAVE_THRESHOLD):
        return(0)
    else:
        return(1)

def read_bit(mem_block):
    val = get_bit(mem_block)
    if (val == 1):
        val2 = get_halfwave(mem_block)
#        if (val2 > HALFWAVE_THRESHOLD):
#            print("error - second half of one is not short, size = ", val2, " fileptr = ", fileptr)
#            exit()
    return(val)

def read_byte(mem_block):
    outval = 0
    if (read_bit(mem_block) == 1):
        outval = outval + 1
    if (read_bit(mem_block) == 1):
        outval = outval + 2
    if (read_bit(mem_block) == 1):
        outval = outval + 4
    if (read_bit(mem_block) == 1):
        outval = outval + 8
    if (read_bit(mem_block) == 1):
        outval = outval + 16
    if (read_bit(mem_block) == 1):
        outval = outval + 32
    if (read_bit(mem_block) == 1):
        outval = outval + 64
    if (read_bit(mem_block) == 1):
        outval = outval + 128

    return(outval)




file_stat = os.stat(sys.argv[1])
filesize = file_stat.st_size
print("filesize = {0:5} KB".format(int(filesize/1024)))

f = open(sys.argv[1], 'rb') 
memory = f.read()
f.close()
print("imported")

print("")

#val = read_int2(0, memory)
#print(hex(val))

val = read_int2(20, memory)
if val == 1:
    print("PCM")
else:
    print("Only handles PCM files")
    exit()

val = read_int2(22, memory)
print("Number of channels:", val)
if (val != 1):
    print("Currently only handles mono samples")
    exit()

val = read_int4(24, memory)
print("Sample Rate (Hz):", val)
if (val != 44100):
    print("Currently only handles 44100Hz samples")
    exit()

val = read_int4(28, memory)
print("Bytes Per Second:", val)

val = read_int2(34, memory)
print("Bits Per Sample:", val)
if (val != 16):
    print("Currently only handles 16-bit samples")
    exit()


# first file position in the actual data
fileptr = 44

val = read_int2(fileptr, memory)
fileptr = fileptr + 2
polarity = POSITIVE
if val > 32767:
    val = val - 65536
    polarity = NEGATIVE

count = 1
wavestart = fileptr

# read leader & toss first bit:

cksum = 0
startoffile = 0
while(startoffile == 0):
    bit = 0
    while(bit == 0):
        bit = get_bit(memory)

    firstbyte = read_byte(memory)
    if (firstbyte != 0xB3):
        continue

    garbagebit = get_bit(memory)
    secondbyte = read_byte(memory)
    if (secondbyte == 0x9D):
        startoffile = 1

print("")
print("Found leader and start bit")
print("")
print("Byte #01 = 0x{0:02X}".format(firstbyte))

cksum = cksum + secondbyte
print("Byte #02 = 0x{0:02X}".format(secondbyte))

garbagebit = get_bit(memory)
thirdbyte = read_byte(memory)
cksum = cksum + thirdbyte
if (thirdbyte == 0x24):
    type = "BASIC"
elif (thirdbyte == 0x25):
    type = "BINARY"
elif (thirdbyte == 0x26):
    type = "SOURCE"
else:
    type = "UNKNOWN"
print("Byte #03 = 0x{0:02X} ('{1:c}') = type ".format(thirdbyte, thirdbyte), type)

print("")

garbagebit = get_bit(memory)
byte4 = read_byte(memory)
garbagebit = get_bit(memory)
byte5 = read_byte(memory)
garbagebit = get_bit(memory)
byte6 = read_byte(memory)
garbagebit = get_bit(memory)
byte7 = read_byte(memory)
garbagebit = get_bit(memory)
byte8 = read_byte(memory)
garbagebit = get_bit(memory)
byte9 = read_byte(memory)
garbagebit = get_bit(memory)
byte10 = read_byte(memory)
garbagebit = get_bit(memory)
byte11 = read_byte(memory)
cksum = cksum + byte4 + byte5 + byte6 + byte7 + byte8 + byte9 + byte10 + byte11

print("Byte #04-#11 = 0x{0:02X} 0x{1:02X} 0x{2:02X} 0x{3:02X} 0x{4:02X} 0x{5:02X} 0x{6:02X} 0x{7:02X}  ('{8:c}{9:c}{10:c}{11:c}{12:c}{13:c}{14:c}{15:c}')".format(byte4,byte5,byte6,byte7,byte8,byte9,byte10,byte11, byte4,byte5,byte6,byte7,byte8,byte9,byte10,byte11))

garbagebit = get_bit(memory)
byte12 = read_byte(memory)
cksum = cksum + byte12
print("Byte #12 = 0x{0:02X}".format(byte12))

print("")

garbagebit = get_bit(memory)
startlow = read_byte(memory)
garbagebit = get_bit(memory)
starthigh = read_byte(memory)
start = (starthigh * 256) + startlow
cksum = cksum + startlow + starthigh
print("Byte #13-#14 = 0x{0:02X} 0x{1:02X}  (START = 0x{2:04X}) ".format(startlow, starthigh, start))

garbagebit = get_bit(memory)
endlow = read_byte(memory)
garbagebit = get_bit(memory)
endhigh = read_byte(memory)
end = (endhigh * 256) + endlow
cksum = cksum + endlow + endhigh
print("Byte #15-#16 = 0x{0:02X} 0x{1:02X}  (END   = 0x{2:04X}) ".format(endlow, endhigh, end))

garbagebit = get_bit(memory)
execlow = read_byte(memory)
garbagebit = get_bit(memory)
exechigh = read_byte(memory)
execaddr = (exechigh * 256) + execlow
cksum = cksum + execlow + exechigh
print("Byte #17-#18 = 0x{0:02X} 0x{1:02X}  (ENTRY = 0x{2:04X}) ".format(execlow, exechigh, execaddr))

print("")

garbagebit = get_bit(memory)
byte19 = read_byte(memory)
print("Byte #19 = 0x{0:02X} (checksum, match against 0x{1:02X})".format(byte19, (cksum & 0xff)))
if (byte19 == (cksum & 0xff)):
    print("--> MATCH !")
else:
    print("ERROR")


print("")

nextleader = 0
bit = 0
while(nextleader == 0):
    while(bit == 0):
        bit = get_bit(memory)

    headerbyte = read_byte(memory)
    if (headerbyte == 0xB3):
        nextleader = 1

print("")
print("Found second leader and start bit")

print("")

print("Block 2 Byte #01 = 0x{0:02X}".format(headerbyte))

print("")

cksum2 = 0

address = (start & 0xFFF0)
string = ""
if (address < start):
    print("0x{0:04X}:".format(address), end=" ")
while (address < start):
    print("  ", end=" ")
    string= string + " "
    address = address + 1

while (address <= end):
    if ((address & 0xF) == 0):
        print("  ", string)
        print("0x{0:04X}:".format(address), end=" ")
        string = ""
    garbagebit = get_bit(memory)
    nextbyte = read_byte(memory)
    if (nextbyte < 0x20) or (nextbyte > 0x7f):
        string = string + "."
    else:
        string = string + chr(nextbyte)
    cksum2 = cksum2 + nextbyte
    print("{0:02X}".format(nextbyte), end=" ")
    address = address + 1

if ((address & 0xF) == 0):
    print("  ", string)
print("")
print("")

garbagebit = get_bit(memory)
finalbyte = read_byte(memory)
print("Block 2 Final Byte = 0x{0:02X}  (checksum, match against 0x{1:02X})".format(finalbyte, (cksum2 & 0xff)))
if (finalbyte == (cksum2 & 0xff)):
    print("--> MATCH !")
else:
    print("ERROR")

print("")

print("END of FILE. fileptr = ", fileptr)

exit()

