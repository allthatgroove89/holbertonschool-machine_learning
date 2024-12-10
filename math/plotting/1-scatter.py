#!/usr/bin/env python3
"""
This module contains a function to plot a scatter plot
of men's height vs weight using matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """
    Generates and plots a scatter plot of men's height vs weight.
    The data is generated from a bivariate normal distribution.
    """
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))

    # Create scatter plot and color
    plt.scatter(x, y, color='magenta')

    # Adding title and labels
    plt.title("Men's Height vs Weight")
    plt.xlabel('Height(in)')
    plt.ylabel('Weight(lbs)')

    # Display the plot
    plt.show()
