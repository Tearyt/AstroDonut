from astropy.io import fits
import numpy as np

class DonutExporter:
    """
    A utility class to export a Donut or DonutList object to a FITS file.

    This class accepts either a single Donut or a DonutList and handles
    the formatting and writing of the image data to a FITS file.
    """

    def __init__(self, source):
        """
        Initialize the DonutExporter with a Donut or DonutList.

        Parameters
        ----------
        source : Donut or DonutList
            The source data object containing a 2D image array to export.

        Raises
        ------
        TypeError
            If the source object does not have a recognizable data structure.
        """
        if hasattr(source, 'model'):
            self.data = source.model
        elif hasattr(source, 'get_combined'):
            self.data = source.get_combined()
        else:
            raise TypeError("Invalid donut or donut list provided.")
    
    def save_to_fits(self, filename, overwrite=True):
        """
        Save the image data to a FITS file.

        Parameters
        ----------
        filename : str
            Path to the output FITS file.

        overwrite : bool, optional
            Whether to overwrite an existing file with the same name, by default True.

        Returns
        -------
        None

        Side Effects
        ------------
        Writes a FITS file to the specified location.

        Prints
        ------
        A confirmation message if the file is saved successfully.
        """
        hdu = fits.PrimaryHDU(self.data)
        hdul = fits.HDUList([hdu])
        hdul.writeto(filename, overwrite=True)
        print(f"FITS file saved successfully to '{filename}'.")
