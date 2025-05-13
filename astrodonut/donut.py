import numpy as np
from .utils import validate_parameters, calculate_intensity, transform, create_ring

class Donut:
    """
    Represents a single elliptical donut shape rendered as a 2D NumPy array.

    This class encapsulates parameters like the size, eccentricity, inclination,
    and thickness of the donut, and generates a ring-shaped image using those values.
    """

    def __init__(self, a1, b1, ecc, inc, ring_ratio, width, height):
        """
        Initialize the Donut with geometric and rendering parameters.

        Parameters
        ----------
        a1 : float
            Semi-major axis of the outer ellipse.
        b1 : float
            Semi-minor axis of the outer ellipse.
        ecc : float
            Eccentricity of the ellipse (between 0 and 1).
        inc : float
            Inclination angle in degrees (for rotation).
        ring_ratio : float
            Ratio of inner to outer radius (defines thickness of the donut).
        width : int
            Width of the output 2D model array.
        height : int
            Height of the output 2D model array.

        Raises
        ------
        ValueError
            If the parameters are not within acceptable ranges (e.g. invalid eccentricity).
        """
        self.a1 = a1
        self.b1 = b1
        self.ecc = ecc
        self.inc = inc
        self.ring_ratio = ring_ratio
        self.width = width
        self.height = height
        self.model = None

        validate_parameters(a1, b1, ecc)

    def ring(self):
        """
        Generate the 2D donut ring based on the initialized parameters.

        Returns
        -------
        numpy.ndarray
            A 2D NumPy array of shape (height, width) representing the donut intensity model.
        """
        self.model = create_ring(
            self.a1, self.b1, self.ecc, self.inc, self.ring_ratio, self.width, self.height
        )
        return self.model