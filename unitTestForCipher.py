import unittest
import caesarcypher as c

message = "Hello World"
key = 3
class MyTest(unittest.TestCase):
    def test(self):
        encoded = c.encode(message, key)
        self.assertEqual(c.decode(encoded, key), message)