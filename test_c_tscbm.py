
##Run a Shared Library version of the TSCBM parser function.
import ctypes
from ctypes import util

##Attach to our library
lib = ctypes.CDLL('./libtscbm.so')
##Attach to C library so we can free memory when done with it.
libc = ctypes.CDLL(util.find_library('c'))
test = '1100110100010000000000010000000011011100000000101010101000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000001111101000000001101110000000010101010100000000000000000000000000000000000000011000000001101110000000001110110110000000000000000000000000000000000000000000000000000000000000000000001000000000000111111000000001011110000000000001111110000000010111100000000000000000000000000000000000000010100000000001111110000001011010100000000000000000000000000000000000000000000000000000000000000000000000110000000000000000000000000100100110000000000111111000000101101010000000000000000000000000000000000000001110000000000111111000000001101001000000000000000000000000000000000000000000000000000000000000000000000100000000000001111110000000110100001000000000011111100000001101000010000000000000000000000000000000000001001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011011101000000000000000000000000001000100000000011111111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100001011101000000000011111011001010000000111100111000000000000000000000000000000000'.encode('utf-8')
test_id = '10'.encode('utf-8')
test_time = '2019-08-12 10:41:55'.encode('utf-8')

##Specify the function parameters and types for our functions.
lib.parseTSCBM.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
lib.parseTSCBM.restype = ctypes.c_void_p
libc.free.argtypes = (ctypes.c_void_p,)

## Wrap the call in a function so we can ensure the free is called each time.
def parse_TSCBM(in_hex, in_id, in_date):
    _ptr = lib.parseTSCBM(in_hex, in_id, in_date)
    result = ctypes.cast(_ptr, ctypes.c_char_p,).value
    #print(hex(_ptr))
    libc.free(_ptr)
    return result

import json
print (parse_TSCBM(test, test_id, test_time).decode('utf-8'))
#test2 = json.loads(parse_TSCBM(test, test_id, test_time).decode('utf-8'))
#import pickle
#print (pickle.dumps(test2))