# Nanogap Estimate
Characterization of electron tunneling in gold electromigrated nanogaps. A simple curve fitting of device I-V traces to determine reduced effective barrier heights and device widths from current voltage measurements of electromigrated gold nanogaps at cryogenic temperatures. A tunneling model characterizes nanogaps irrespective of the true potential profile between electrodes, thus defining a metric for device performance. This metric may be used to compare nanogap device performance.

# Usage
Nanogap Estimate takes as its argument a .csv file of current-voltage measurements. Three examples (a2-d2.csv, a2-d5.csv, and a2-d6.csv) are provided for proper formatting. Nanogap Estimate plots and fits the data to the Simmons model for tunneling currents. Reduced effective barrier height, gap width, and effective resistance at 100 mV are then printed to the console to one standard deviation of accuracy.
