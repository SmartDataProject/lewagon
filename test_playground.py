import unittest
import math
from playground import cal_perimeter
class TestPlayground(unittest.TestCase):
   def test_playground_0(self):
       self.assertEqual(cal_perimeter(0), 0)

   def test_playground_1(self):
       self.assertEqual(cal_perimeter(1), 2*math.pi)
  
if __name__ == '__main__':
    unittest.main()