import numpy as np

def validate_parameters(a1, b1, ecc):
    """
    Validates the input parameters for a donut shape.

    Parameters
    ----------
    a1 : float
        Semi-major axis of the outer ellipse.
    b1 : float
        Semi-minor axis of the outer ellipse.
    ecc : float
        Eccentricity of the ellipse. Must be between 0 (circular) and 1 (parabolic).

    Raises
    ------
    ValueError
        If eccentricity is not in the range [0, 1), or if axes are non-positive.
    """
        
    if ecc >= 1 or ecc < 0:
        raise ValueError("Eccentricity must be between 0 and 1.")
    if a1 <= 0 or b1 <= 0:
        raise ValueError("Axes must be positive values.")
    
def calculate_intensity(dist, width):
    """
    Calculates the intensity value based on distance from the center.

    Parameters
    ----------
    dist : float
        Distance from the center of the ellipse.
    width : int
        Total width of the donut image (used for scaling intensity).

    Returns
    -------
    float
        Intensity value at the given distance.
    """
    return 50 + 200 * np.exp(-dist**2 / (2 * (0.1 * width)**2))

def transform(x, y, x0, y0, cos_inc, sin_inc):
    """
    Applies a rotation and translation transformation to the coordinates.

    Parameters
    ----------
    x, y : float
        Original coordinates.
    x0, y0 : float
        Center coordinates (to translate to origin).
    cos_inc : float
        Cosine of the inclination angle (rotation).
    sin_inc : float
        Sine of the inclination angle (rotation).

    Returns
    -------
    tuple of float
        Transformed (x, y) coordinates.
    """
    norm_x = x - x0
    norm_y = y - y0
    transformed_x = norm_x * cos_inc - norm_y * sin_inc
    transformed_y = norm_x * sin_inc + norm_y * cos_inc
    return transformed_x, transformed_y

def create_ring(a1, b1, ecc, inc, ring_ratio, width, height):
    """
    Creates a 2D numpy array representing a ring (donut) shape with elliptical geometry.

    Parameters
    ----------
    a1 : float
        Semi-major axis of the outer ellipse.
    b1 : float
        Semi-minor axis of the outer ellipse.
    ecc : float
        Eccentricity of the ellipse.
    inc : float
        Inclination angle in degrees (rotation).
    ring_ratio : float
        Ratio of inner to outer ellipse (controls thickness of the ring).
    width : int
        Width of the resulting image.
    height : int
        Height of the resulting image.

    Returns
    -------
    numpy.ndarray
        2D array of shape (height, width) containing intensity values of the donut ring.
    """
    array = np.zeros((height, width), dtype=np.float32)

    x0 = width // 2
    y0 = height // 2

    inc_rad = np.radians(inc)
    cos_inc = np.cos(-inc_rad)
    sin_inc = np.sin(-inc_rad)

    # Outer ellipse
    for y in range(height):
        for x in range(width):
            tx, ty = transform(x, y, x0, y0, cos_inc, sin_inc)
            if (tx**2 / (a1**2 * (1 - ecc**2)) + ty**2 / (b1**2)) <= 1:
                dist = np.sqrt((x - x0) ** 2 + (y - y0) ** 2)
                intensity = calculate_intensity(dist, width)
                array[y, x] = intensity

    # Inner ellipse
    a2 = a1 * ring_ratio
    b2 = b1 * ring_ratio
    
    for y in range(height):
        for x in range(width):
            tx_i, ty_i = transform(x, y, x0, y0, cos_inc, sin_inc)
            if tx_i**2 / (a2**2 * (1 - ecc**2)) + ty_i**2 / (b2**2) <= 1:
                array[y, x] = 0

    return array