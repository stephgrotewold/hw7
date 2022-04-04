import unittest
import test_family

from test_family import calculateDepth
from test_family import perfect

class testBinary(unittest.TestCase):
    def calculateDepth(self):
        self.assertRaises(TypeError, calculateDepth,'a','b', test_family.root)
        self.assertEquals(1,test_family.calculateDepth(1,0,test_family.root))
        self.assertEquals(0,test_family.calculateDepth(3,6,test_family.root))
    
    def is_perfect(self):
        self.assertRaises(TypeError, perfect,'a','b', test_family.root)
        self.assertEquals(1,test_family.perfect(1,0,test_family.root))
        self.assertEquals(0,test_family.perfect(3,6,test_family.root))
    
if __name__=='__main__':
    unittest.main()


