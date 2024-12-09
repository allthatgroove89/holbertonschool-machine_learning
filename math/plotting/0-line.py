#!/usr/bin/env python3
"""
This module contains a function to plot a
line graph of cubic values using matplotlib.
"""


import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plots a line graph of cubic values from 0 to 10.
    """
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(range(len(y)), y, '-r')  # '-r' specifies a solid red lie

    # Set x-axis range
    plt.xlim(0, 10)

    # Display the plot
    plt.show()
