import time
import codecs

def readByte():
    byte = file.read(188)
    decodedByte = codecs.encode(byte,'hex')
    #print(byte)
    if decodedByte != b'':
        binaryByte = "{:0>32}".format(bin(int(decodedByte, 16))[2:34])
        toReturn = [binaryByte, byte]
        return binaryByte
    else:
        return "EOF"

def bitRate(layer, version, input):
    bitRate = 0
    if version == '11':
        if layer == '11':
            if input == '0001':
                bitRate = 32
            elif input == '0010':
                bitRate = 64
            elif input == '0011':
                bitRate = 96
            elif input == '0100':
                bitRate = 128
            elif input == '0101':
                bitRate = 160
            elif input == '0110':
                bitRate = 192
            elif input == '0111':
                bitRate = 224
            elif input == '1000':
                bitRate = 256
            elif input == '1001':
                bitRate = 288
            elif input == '1010':
                bitRate = 320
            elif input == '1011':
                bitRate = 352
            elif input == '1100':
                bitRate = 384
            elif input == '1101':
                bitRate = 416
            elif input == '1110':
                bitRate = 448
        elif layer == '10':
            if input == '0001':
                bitRate = 32
            elif input == '0010':
                bitRate = 48
            elif input == '0011':
                bitRate = 56
            elif input == '0100':
                bitRate = 64
            elif input == '0101':
                bitRate = 80
            elif input == '0110':
                bitRate = 96
            elif input == '0111':
                bitRate = 112
            elif input == '1000':
                bitRate = 128
            elif input == '1001':
                bitRate = 160
            elif input == '1010':
                bitRate = 192
            elif input == '1011':
                bitRate = 224
            elif input == '1100':
                bitRate = 256
            elif input == '1101':
                bitRate = 320
            elif input == '1110':
                bitRate = 384
        elif layer == '01':
            if input == '0001':
                bitRate = 32
            elif input == '0010':
                bitRate = 40
            elif input == '0011':
                bitRate = 48
            elif input == '0100':
                bitRate = 56
            elif input == '0101':
                bitRate = 64
            elif input == '0110':
                bitRate = 80
            elif input == '0111':
                bitRate = 96
            elif input == '1000':
                bitRate = 112
            elif input == '1001':
                bitRate = 128
            elif input == '1010':
                bitRate = 160
            elif input == '1011':
                bitRate = 192
            elif input == '1100':
                bitRate = 224
            elif input == '1101':
                bitRate = 256
            elif input == '1110':
                bitRate = 320
    elif version == '00' or version == '10':
        if layer == '11':
            if input == '0001':
                bitRate = 32
            elif input == '0010':
                bitRate = 48
            elif input == '0011':
                bitRate = 56
            elif input == '0100':
                bitRate = 64
            elif input == '0101':
                bitRate = 80
            elif input == '0110':
                bitRate = 96
            elif input == '0111':
                bitRate = 112
            elif input == '1000':
                bitRate = 128
            elif input == '1001':
                bitRate = 144
            elif input == '1010':
                bitRate = 160
            elif input == '1011':
                bitRate = 176
            elif input == '1100':
                bitRate = 192
            elif input == '1101':
                bitRate = 224
            elif input == '1110':
                bitRate = 256
        elif layer == '10' or layer == '01':
            if input == '0001':
                bitRate = 8
            elif input == '0010':
                bitRate = 16
            elif input == '0011':
                bitRate = 24
            elif input == '0100':
                bitRate = 32
            elif input == '0101':
                bitRate = 40
            elif input == '0110':
                bitRate = 48
            elif input == '0111':
                bitRate = 56
            elif input == '1000':
                bitRate = 64
            elif input == '1001':
                bitRate = 80
            elif input == '1010':
                bitRate = 96
            elif input == '1011':
                bitRate = 112
            elif input == '1100':
                bitRate = 128
            elif input == '1101':
                bitRate = 144
            elif input == '1110':
                bitRate = 160
    return str(bitRate)

def samplingRateIndex(version, input):
    samplingRateIndex = 0
    if version == '11':
        if input == '00':
            samplingRateIndex = 44100
        elif input == '01':
            samplingRateIndex = 48000
        elif input == '10':
            samplingRateIndex = 32000
    elif version == '10':
        if input == '00':
            samplingRateIndex = 22050
        elif input == '01':
            samplingRateIndex = 24000
        elif input == '10':
            samplingRateIndex = 16000
    elif version == '00':
        if input == '00':
            samplingRateIndex = 11025
        elif input == '01':
            samplingRateIndex = 12000
        elif input == '10':
            samplingRateIndex = 8000
    return str(samplingRateIndex)

def modeExtension(layer, input):
    result = ""
    if layer == '11' or layer == '10':
        if input == '00':
            result = "bands 4 to 31"
        elif input == '01':
            result = "bands 8 to 31"
        elif input == '10':
            result = "bands 12 to 31"
        elif input == '00':
            result = "bands 16 to 31"
    elif layer == '01':
        if input == '00':
            result = "M/S stereo: OFF, Intensity stereo: OFF"
        elif input == '01':
            result = "M/S stereo: OFF, Intensity stereo: ON"
        elif input == '10':
            result = "M/S stereo: ON, Intensity stereo: OFF"
        elif input == '00':
            result = "M/S stereo: ON, Intensity stereo: ON"
    return result

print("Program start")
time.sleep(1)
fName = "input.mp3"
file = open(fName, "rb")
if file:
    print("Read success")

toRead = readByte()
flag = toRead.startswith('11111111111')
#print(toRead)
while toRead != "EOF" and flag == False:
    #print(toRead)
    toRead = readByte()
    flag = toRead.startswith('11111111111')
    #print(flag)

print("----------------------------------------------------------------------")
print("Full MPEG header: " + toRead)
print("----------------------------------------------------------------------")

print("Frame sync bits:\n\t" + toRead[0:11])
print("----------------------------------------------------------------------")

print("Audio Version ID:")
if toRead[11:13] == '00':
    print("\tMPEG ver 2.5")
elif toRead[11:13] == '10':
    print("\tMPEG ver 2")
elif toRead[11:13] == '11':
    print("\tMPEG ver 1")
print("----------------------------------------------------------------------")

print("Layer index:")
if toRead[13:15] == '01':
    print("\tLayer III")
elif toRead[13:15] == '10':
    print("\tLayer II")
elif toRead[13:15] == '11':
    print("\tLayer I")
print("----------------------------------------------------------------------")

print("Protection bit:")
if toRead[15] == '0':
    print("\tProtected by 16-bit CRC")
elif toRead[15] == '1':
    print("\tNo CRC")
print("----------------------------------------------------------------------")

print("Bitrate:\n\t" + bitRate(toRead[13:15], toRead[11:13], toRead[16:20]) + " kbps")
print("----------------------------------------------------------------------")

print("Sampling rate index:\n\t" + samplingRateIndex(toRead[11:13], toRead[20:22]) + " Hz")
print("----------------------------------------------------------------------")

print("Padding bit:")
if toRead[22] == '0':
    print("\tData not padded")
elif toRead[22] == '1':
    print("\tData padded with one slot")
print("----------------------------------------------------------------------")

print("Private bit:\n\t" + toRead[23])
print("----------------------------------------------------------------------")

print("Channel mode:")
if toRead[24:26] ==  '00':
    print("\tStereo")
elif toRead[24:26] ==  '01':
    print("\tJoint stereo (Stereo)")
elif toRead[24:26] ==  '10':
    print("\tDual Channel (Two Mono Channels)")
elif toRead[24:26] ==  '11':
    print("\tSingle Channel (Mono)")
print("----------------------------------------------------------------------")

print("Mode Extension:\n\t" + modeExtension(toRead[13:15], toRead[26:28]))
print("----------------------------------------------------------------------")

print("Copyright bit:\n\t" + toRead[28])
print("----------------------------------------------------------------------")

print("Original bit:\n\t" + toRead[29])
print("----------------------------------------------------------------------")

print("Emphasis:")
if toRead[30:32] == '00':
    print("\tnone")
elif toRead[30:32] == '01':
    print("\t50/15 ms")
elif toRead[30:32] == '11':
    print("\tCCIT J.17")
print("----------------------------------------------------------------------")

file.close()
print("Program end")
