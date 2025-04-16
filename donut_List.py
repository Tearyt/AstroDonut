import numpy as np

class DonutList:
    def __init__(self, shape):
        self.height, self.width = shape
        self.combined = np.zeros((self.height, self.width), dtype=np.float32)

    def add_donut(self, donut):
        if donut.shape != (self.height, self.width):
            raise ValueError("Donut shape does not match the list shape.")
        self.combined += donut
    
    def get_combined(self):
        return self.combined
    
    def normalize(self):
        max_value = np.max(self.combined)
        if max_value > 0:
            self.combined /= max_value
        return self.combined
        
