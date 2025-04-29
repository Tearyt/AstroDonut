import unittest
from astrodonut.donut import Donut

class TestDonut(unittest.TestCase):

    def test_donut_model_generation(self):
        donut = Donut(100, 60, 0.2, 30, 0.8, 200, 200)
        model = donut.ring()
        self.assertEqual(model.shape, (200, 200))
        self.assertTrue((model > 0).any())

if __name__ == '__main__':
    unittest.main()
