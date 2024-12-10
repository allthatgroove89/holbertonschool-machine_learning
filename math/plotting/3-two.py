#!/usr/bin/env python3
"""
This module contains a function to plot the exponential
decay of C-14 and Ra-226 over time using matplotlib.
"""


import numpy as np
import matplotlib.pyplot as plt


def two():
    """
    Generates and plots line graphs showing the
    exponential decay of C-14 and Ra-226 over time.
    The data is calculated using the exponential decay formula.
    """
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    # Create a plot as a line graphs
    plt.plot(x, y1, 'r--', label='C-14')
    plt.plot(x, y2, 'g-', label='Ra-226')

    # Adding titles and labels
    plt.title('Exponential Decay of Radioactive Elements')
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')

    # Setting axis ranges
    plt.xlim(0, 20000)
    plt.ylim(0, 1)

    # Adding legend
    plt.legend(loc='upper right')

    # Display the graph
    plt.show()
