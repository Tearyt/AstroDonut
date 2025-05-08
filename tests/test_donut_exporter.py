import unittest
import os
from astropy.io import fits
from astrodonut.donut import Donut
from astrodonut.donut_List import DonutList
from astrodonut.donut_exporter import DonutExporter

class TestDonutExporter(unittest.TestCase):
    
    def setUp(self):
        # Create a sample donut and donut list for testing
        self.donut = Donut(50, 50, 0.3, 20, 0.9, 200, 200)
        self.donut.ring()
        self.donut_list = DonutList([self.donut])
        self.exporter = DonutExporter(self.donut_list)

    def test_export_donut_to_fits(self):
        # Test saving the donut to a FITS file
        filename = "test_donut.fits"
        self.exporter.save_to_fits(filename, overwrite=True)

        # Check if the file was created and is readable
        with fits.open(filename) as hdul:
            self.assertEqual(len(hdul), 1)
            self.assertEqual(hdul[0].data.shape, (200, 200))
            self.assertTrue((hdul[0].data == self.donut_list.get_combined()).all())

    def tearDown(self):
        # Clean up the created FITS file after the test
        if os.path.exists("test_donut.fits"):
            os.remove("test_donut.fits")

if __name__ == '__main__':
    unittest.main()