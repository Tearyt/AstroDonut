from astrodonut.donut import Donut
from astrodonut.donut_List import DonutList
from matplotlib import pyplot as plt
from astrodonut.donut_exporter import DonutExporter

# Create individual donuts
d1 = Donut(56, 40, 0.3, 40, 0.97, 200, 200)
d2 = Donut(44, 31, 0.3, 40, 0.8, 200, 200)
d3 = Donut(20, 15, 0.3, 40, 0.45, 200, 200)

# Generate rings
d1.ring()
d2.ring()
d3.ring()

# Combine them in a DonutList
dl = DonutList([d1, d2, d3])
combined_model = dl.get_combined()

# Plot the combined donut disk
plt.imshow(combined_model, origin='lower', cmap='hot')
plt.title("Combined Donut Disk")
plt.colorbar(label="Intensity")
plt.show()

# Save the combined donut to a FITS file
exporter = DonutExporter(dl)
exporter.save_to_fits("combined_donut.fits", overwrite=True)

