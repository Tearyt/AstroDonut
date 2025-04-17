from donut import Donut
from donut_List import DonutList
from matplotlib import pyplot as plt

# Create individual donuts
d1 = Donut(56, 40, 0.3, 40, 0.97, 200, 200)
d2 = Donut(44, 31, 0.3, 40, 0.8, 200, 200)
d3 = Donut(20, 15, 0.3, 40, 0.45, 200, 200)

# Generate rings
d1.ring()
d2.ring()
d3.ring()

# Combine them in a DonutList
dl = DonutList([d1, d2, d3])  # ← list of Donut objects, not a shape
combined_model = dl.get_combined()

# Plot the combined donut disk
plt.imshow(combined_model, origin='lower', cmap='hot')
plt.title("Combined Donut Disk")
plt.colorbar(label="Intensity")
plt.show()

