import numpy as np
from utils import validate_parameters, calculate_intensity, transform, create_ring

class Donut:
    def __init__(self, a1, b1, ecc, inc, width, height):
        self.a1 = a1
        self.b1 = b1
        self.ecc = ecc
        self.inc = inc
        self.width = width
        self.height = height
        self.model = None

        validate_parameters(a1, b1, ecc)

    def ring():
        self.model = create_ring(a1, b1, ecc, inc, width, height)
        return self.model