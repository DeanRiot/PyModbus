import crc16 as crc
def createFrame(modbFrame):
    data=[]
    pdu = ''
    for sym in modbFrame:
        print(sym.encode('ascii'))
        data.append(chr(int(sym.encode('ascii'))))
        pdu = pdu + sym
    crcSumm = hex(crc.crc16(bytes(sym, 'ascii')))
    print(crcSumm)
    data.append(chr(int(crcSumm[0:2])))
    data.append(chr(int(crcSumm[2:0])))
    return data

def createStringFrame(byteFrame):
    frame = ''
    for char in byteFrame:
        frame = frame + char
    return frame

def decodeChar(dataString):
    byteArr = []
    for char in dataString:
        data = int(ord(char))
        byteArr.append(data)
    return byteArr

def parseFrame(stringFrame):
    data = stringFrame.split()
    return data

