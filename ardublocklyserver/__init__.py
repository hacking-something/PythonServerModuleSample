import os

# print (__file__)
# print (os.path.abspath(__file__))
# print (os.path.dirname(os.path.abspath(__file__)))
# print (os.path.join(os.path.dirname(os.path.abspath(__file__))))
import sys

local_package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(local_package_path)
__version__ = '0.0.1'
__author__ = 'Li Xiaolong'


