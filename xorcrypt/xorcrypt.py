import hashlib


def _hash(key, hash_type='sha1'):
    print 'key2 ' , key
    if(hash_type is 'sha1'):
        m = hashlib.sha1()
    else:
        m = hashlib.md5()
    m.update(key)
    return m.digest().encode('hex')

def _xor_merge(string, key):
    '''
    XOR Merge string and key  
    '''
    key_hash = _hash(key)
    print key_hash
    ret_str = ''
    for i in range(len(string)):
        ret_str += chr(ord(string[i]) ^ ord(key_hash[i%len(key_hash)]))
    return ret_str

def decrypt(string, key):
    '''
    XOR Decode a decoded string  
    '''

    string = _xor_merge(string, key)
    
    dec = ''
    for i in range(len(string)):
        if (i % 2) == 0:
            dec += chr(ord(string[i]) ^ ord(string[i+1]))
    return dec
