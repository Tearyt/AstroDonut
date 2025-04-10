# AstroDonut
AstroDonut is a Python package for generating synthetic elliptical ring structures—ideal for simulating protoplanetary or circumstellar disks such as HL Tauri. 

## Requirements
- The package should be able to generate elliptcial rings(donuts) to simulate disk structures around young stellar objects (YSOs) to test telescope configurations, plan observations, and develop data reduction pipelines, astronomers need realistic yet flexible synthetic models of these disks.
- The user should be able to define ring parameters such as:
  - Semi-major axis (`a1`)
  - Semi-minor axis (`b1`)
  - Eccentricity (`ecc`)
  - Inclination (`inc`)
  - Output array size (`width`, `height`)
- The model should reflect radial intensity variation, where pixels closer to the center appear brighter, following a Gaussian distribution.
- The package should be able to combine multiple rings and stack them together, to model more complex disk structures.
- The package should offer a preview of the model with the help of `matplotlib`, plotting the model to allow for a quick visual inspection of the model.
- The package should be able to export the model to a FITS format for use with observatory simulators.

  ### Dependecies
- `numpy`: For the numerical calculations for generating the donut.
- `matplotlib`: To plot the preview of the created model.
- `astropy`: Employed to export the model into a FITS file.

## User stories

### Main use cases

Shannon is designing an observing program for the ELT to study planet formation. She wants to test if the telescope can detect gaps and rings in HL Tauri–like systems. Using AstroDonut, she generates a synthetic disk with five elliptical rings of varying radii, eccentricities, and inclinations. She exports the disk to a FITS file and uses ScopeSim to simulate ELT observations under realistic conditions.

Benjamin is writing a data processing pipeline for a simulator that will mimic ELT’s camera response. To test the pipeline, Benjamin needs realistic test data in FITS format. He uses AstroDonut to generate synthetic multi-ring disks, exports them to FITS, and runs them through the simulator pipeline. This helps him to identify edge cases where image artifacts or noise could affect disk detectability.
### Edge use cases

During a parameter sweep, Lando sets `ecc=1.5` by mistake. AstroDonut immediately raises a `ValueError` with a message:
"Eccentricity must be < 1 for physical ellipses."
This helps Lando correct the input without generating unphysical models or debugging cryptic errors.

Andreas wants to simulate whether a 0.01 AU-wide gap in a disk can be resolved by the ELT. They use AstroDonut to generate a single ultra-narrow elliptical ring (with a tiny `b1` value). They then simulate the observation and process it to test if such a narrow feature can be detected.

## Pseudo code examples

import astrodonut as ad

ring1 = ad.generate_donut(
    a1=100, b1=60, ecc=0.2, inc=30, width=500, height=500
)

ring2 = ad.generate_donut(
    a1=150, b1=90, ecc=0.3, inc=30, width=500, height=500
)

combined_rings = ad.combine_donuts([ring1, ring2])

ad.preview(combined_rings)

ad.export_to_fits(combined_rings, 'combined_rings.fits')

