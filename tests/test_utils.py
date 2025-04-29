import unittest
import numpy as np
from astrodonut.utils import transform, validate_parameters, create_ring  # Corrected import

class TestUtils(unittest.TestCase):

    def test_transform(self):
        x, y = 5, 10
        x0, y0 = 2, 2
        cos_inc = 1
        sin_inc = 0
        tx, ty = transform(x, y, x0, y0, cos_inc, sin_inc)
        self.assertEqual(tx, 3)
        self.assertEqual(ty, 8)

    def test_validate_parameters_valid(self):
        try:
            validate_parameters(100, 60, 0.5) 
        except ValueError:
            self.fail("validate_parameters() raised ValueError unexpectedly!")

    def test_validate_parameters_invalid(self):
        with self.assertRaises(ValueError):
            validate_parameters(100, 60, 1.2)

    def test_create_ring_output_shape(self):
        ring = create_ring(100, 60, 0.2, 30, 0.8, 200, 200)
        self.assertEqual(ring.shape, (200, 200))

    def test_create_ring_nonzero(self):
        ring = create_ring(100, 60, 0.2, 30, 0.8, 200, 200)
        self.assertTrue(np.max(ring) > 0)

if __name__ == '__main__':
    unittest.main()
