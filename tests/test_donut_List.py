import unittest
from astrodonut.donut import Donut
from astrodonut.donut_List import DonutList

class TestDonutList(unittest.TestCase):

    def test_combine_donuts(self):
        d1 = Donut(100, 60, 0.1, 20, 0.8, 200, 200)
        d2 = Donut(120, 80, 0.2, 20, 0.8, 200, 200)
        d1.ring()
        d2.ring()
        
        dl = DonutList([d1, d2])
        combined = dl.get_combined()
        
        self.assertEqual(combined.shape, (200, 200))
        self.assertTrue((combined > 0).any())

if __name__ == '__main__':
    unittest.main()
