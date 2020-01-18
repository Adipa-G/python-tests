import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__),"..\..\..","hellomodule"))

import unittest
from hellomodule import helloText

class TestHello(unittest.TestCase):

    def test_helloText(self):
        text = helloText()
        self.assertEqual(text, 'Hello World.')

if __name__ == '__main__':
    unittest.main()