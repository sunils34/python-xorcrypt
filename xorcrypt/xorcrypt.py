import sys
import hashlib
from random import randint


def _hash(key, hash_type='sha1'):
    if(hash_type is 'sha1'):
        m = hashlib.sha1()
    else:
        m = hashlib.md5()
    m.update(key)
    return m.digest().encode('hex')

def _xor_merge(data, key):
    '''
    XOR Merge data and key  
    '''
    key_hash = _hash(key)
    ret_str = ''
    for i in range(len(data)):
        ret_str += chr(ord(data[i]) ^ ord(key_hash[i%len(key_hash)]))
    return ret_str

def xor_decrypt(data, key):
    '''
    XOR Decode a decoded data  
    '''

    data = _xor_merge(data, key)
    
    dec = ''
    for i in range(len(data)):
        if (i % 2) == 0:
            dec += chr(ord(data[i]) ^ ord(data[i+1]))
    return dec

def xor_encrypt(data, key):
    '''
    XOR Encrypt a data
    '''
    rand = ''
    while (len(rand) < 32):
        rand += str(randint(0, sys.maxint))
    
    rand = _hash(rand)
    enc = ''
    
    for i in range(len(data)): 
        enc += rand[i%len(rand)] + chr(ord(rand[i%len(rand)]) ^ ord(data[i]))
    return _xor_merge(enc, key)

