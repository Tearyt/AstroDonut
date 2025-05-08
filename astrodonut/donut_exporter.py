from astropy.io import fits
import numpy as np

class DonutExporter:
    def __init__(self, source):
        if hasattr(source, 'model'):
            self.data = source.model
        elif hasattr(source, 'get_combined'):
            self.data = source.get_combined()
        else:
            raise TypeError("Invalid donut or donut list provided.")
    
    def save_to_fits(self, filename, overwrite=True):
        
        hdu = fits.PrimaryHDU(self.data)
        hdul = fits.HDUList([hdu])
        hdul.writeto(filename, overwrite=True)
        print(f"FITS file saved successfully to '{filename}'.")
