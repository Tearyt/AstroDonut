.. AstroDonut documentation master file, created by
   sphinx-quickstart on Tue May 13 10:27:45 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

AstroDonut Documentation
========================

**Date**: May 14, 2025 **Version**:0.1.0

**Github**: https://github.com/Tearyt/AstroDonut

AstroDonut is a Python package for generating synthetic elliptical ring structures, ideal for simulating protoplanetary or circumstellar disks such as HL Tauri.

Explore the core components below:

.. toctree::
   :hidden:

   donut
   donut_List
   donut_exporter
   utils

.. raw:: html

   <style>
     .grid-container {
       display: grid;
       grid-template-columns: repeat(2, 1fr);
       gap: 1.5rem;
       margin-top: 2rem;
     }
     .card {
       padding: 1.2rem;
       border-radius: 0.75rem;
       border: 1px solid var(--color-foreground-border);
       background-color: var(--color-background-secondary);
       color: var(--color-foreground-primary);
       text-decoration: none;
       transition: box-shadow 0.3s ease;
     }
     .card:hover {
       box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
     }
     .card h3 {
       margin-top: 0;
       margin-bottom: 0.5rem;
       font-size: 1.25rem;
     }
     .card p {
       margin: 0;
       font-size: 0.95rem;
     }
   </style>

   <div class="grid-container">

     <a class="card" href="donut_exporter.html">
       <h3>Donut Exporter</h3>
       <p>Handles exporting donuts to file formats.</p>
     </a>

     <a class="card" href="donut_List.html">
       <h3>Donut List</h3>
       <p>Manages collections of donut objects.</p>
     </a>

     <a class="card" href="donut.html">
       <h3>Donut</h3>
       <p>Generates the ring-shaped donut geometries.</p>
     </a>

     <a class="card" href="utils.html">
       <h3>Utils</h3>
       <p>Math and geometry helper functions.</p>
     </a>

   </div>
