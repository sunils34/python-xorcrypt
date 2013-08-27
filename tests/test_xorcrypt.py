from xorcrypt.xorcrypt import xor_encrypt
from xorcrypt.xorcrypt import xor_decrypt
import unittest
import random
import string

class XorCryptTestSuite(unittest.TestCase):

    def assert_encrypt_then_decrypt(self, data, key):
        assert data == xor_decrypt(xor_encrypt(data, key), key)

    def test_simple(self):
        key = 'absd34DScx98SewlcCsDwp1297Snmde2'
        data = "This is a test string"
        self.assert_encrypt_then_decrypt(data, key)

    def test_rand_small(self):
        #test this with 10 random strings
        for i in range(10):
            rand_key_10 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
            rand_data_10 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
            self.assert_encrypt_then_decrypt(rand_data_10, rand_key_10);

