import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__),"..","hellomodule"))

from hellomodule import helloText
text = helloText()
print(text)