'''
Documentation, License etc.

@package int_to_byte
'''
import struct


int_file = open( './unit_9_last_10000_no_newlines_10_17.out' ,'r')
byte_file = open('./bytes.out','a')
print int_file

for word in int_file:
    i = struct.pack("Q",int(word))
    byte_file.write(i)
    
