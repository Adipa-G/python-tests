import unittest
from hellomodule import helloText

class TestHello(unittest.TestCase):

    def test_helloText(self):
        text = helloText()
        self.assertEqual(text, 'Hello World.')

if __name__ == '__main__':
    unittest.main()