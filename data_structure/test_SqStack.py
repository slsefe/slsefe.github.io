import unittest
from Stack import SqStack

class TestSqStack(unittest.TestCase):
    '''针对SqStack类的测试'''

    def setUp(self):
        ''''''
        data = [2,7,4,9,-1,0,23,-9,55]
        self.my_stack = SqStack(data = data)
    
    def test_size(self):
        pass