from xorcrypt.xorcrypt import *
import unittest

class Decryption(unittest.TestCase):
    def test_simple(self):
        key = 'absd34DScx98SewlcCsDwp1297Snmde2'
        orig = "This is a test string"
        assert decrypt(encrypt(orig, key), key)
        return


