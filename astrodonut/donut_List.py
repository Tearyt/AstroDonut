import numpy as np
from .donut import Donut

class DonutList:
    """
    Manages a collection of Donut objects and combines them into a single 2D model.

    This class allows adding multiple donut models together, normalizing the result,
    and retrieving the combined image.

    """
    def __init__(self, donuts):
        """
        Initialize the DonutList with a list of Donut objects.

        Parameters
        ----------
        donuts : list of Donut
            A list of Donut instances to be combined.

        Raises
        ------
        ValueError
            If the list is empty or if the shapes of the donut models do not match.
        """
        if not donuts:
            raise ValueError("The list of donuts cannot be empty.")
        
        self.donuts = donuts
        self.height, self.width = self.donuts[0].model.shape

        for donut in self.donuts:
            if donut.model.shape != (self.height, self.width):
                raise ValueError("All donuts must have the same shape.")
        
        self.combined = np.zeros((self.height, self.width), dtype=np.float32)

        self.combine()
    
    def combine(self):
        """
        Combine all Donut models in the list into one by summing their intensity arrays.
        """
        for donut in self.donuts:
            self.combined += donut.model

    def add_donut(self, donut):
        """
        Add a new Donut model to the combined image.

        Parameters
        ----------
        donut : Donut
            A new Donut instance to be added.

        Raises
        ------
        ValueError
            If the shape of the donut model does not match the combined image.
        """
        if donut.shape != (self.height, self.width):
            raise ValueError("Donut shape does not match the list shape.")
        self.combined += donut.model
    
    def get_combined(self):
        """
        Retrieve the combined image of all Donuts.

        Returns
        -------
        numpy.ndarray
            The combined 2D intensity model.
        """
        return self.combined
    
    def normalize(self):
        """
        Normalize the combined image so that its maximum value is 1.
        """
        max_val = np.max(self.combined)
        if max_val > 0:
            self.combined /= max_val
        
