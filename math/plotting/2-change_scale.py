#!/usr/bin/env python3
"""
This module contains a function to plot the exponential
decay of C-14 over time using matplotlib.
"""


import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """
    Generates and plots a line graph showing the
    exponential decay of C-14 over time.
    The data is calculated using the exponential decay formula.
    """
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))

    # Create a line graph plot
    plt.plot(x, y)

    # Add title and labels
    plt.title('Exponential Decay of C-14')
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')

    # Logarithmic scale for Y-axis
    plt.yscale('log')

    # Adjust X-axis range
    plt.xlim(0, 28650)

    # Display graph
    plt.show()
