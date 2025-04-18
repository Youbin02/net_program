import socket
import struct
import binascii

class UPphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!H', self.src_port)
        packed += struct.pack('!H', self.dst_port)
        packed += struct.pack('!H', self.length)
        packed += struct.pack('!H', self.checksum)
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

ip = UPphdr(5555, 80, 1000, 0xFFFF) 
packed_Udphdr = ip.pack_Udphdr()
print(binascii.b2a_hex(packed_Udphdr))
unpacked_Udphdr = unpack_Udphdr(packed_Udphdr)
print(unpacked_Udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'\
.format(getSrcPort(unpacked_Udphdr), getDstPort(unpacked_Udphdr), 
        getLength(unpacked_Udphdr), getChecksum(unpacked_Udphdr)))