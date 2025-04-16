import numpy as np

def validate_parameters(a1, b1, ecc):
    if ecc >= 1 or ecc < 0:
        raise ValueError("Eccentricity must be between 0 and 1.")
    if a1 <= 0 or b1 <= 0:
        raise ValueError("Axes must be positive values.")
    
def calculate_intensity(dist, width):
    return 50 + 200 * np.exp(-dist**2 / (2 * (0.1 * width)**2))


