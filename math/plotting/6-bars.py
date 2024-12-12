#!/usr/bin/env python3
"""
Module: 6-bars

This module provides a function to plot a stacked bar graph of student grades.

Functions:
    bars(): Plots a stacked bar graph of different
    types of fruits for each student.

Example:
    To use this module, simply call the bars function:

    from 6-bars import bars
    bars()
"""


import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    Plots a stacked bar graph of different types of fruits for each student.

    The x-axis is labeled with student names.
    Each bar represents the number of different types of fruits.
    The bars are stacked to show the total number of fruits for each student.
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))
    names = ['Farrah', 'Fred', 'Felicia']

    # Set the names of the fruits and their corresponding colors
    fruits = [('apples', 'red'), ('bananas', 'yellow'),
              ('oranges', '#ff8000'), ('peaches', '#ffe5b4')]

    # Initialize the bottom of the bars (needed for stacking the bars)
    bottom = np.zeros(len(names))

    # Loop over each type of fruit
    for fruit_name, color in fruits:
        # Create a bar for the current type of fruit
        # The height of the bar is the number of this type of fruit
        # The bottom of the bar is the top of the previous bar
        # (or 0 for the first bar)
        plt.bar(names, fruit[fruits.index((fruit_name, color))],
                bottom=bottom, color=color, width=0.5)

        # Update the bottom for the next bar
        bottom += fruit[fruits.index((fruit_name, color))]

    # Add a legend to the plot
    plt.legend([fruit_name for fruit_name, color in fruits])

    # Label the y-axis and set its range and tick marks
    plt.ylabel('Quantity of Fruit')
    plt.yticks(np.arange(0, 81, 10))

    # Set the title of the plot
    plt.title('Number of Fruit per Person')

    # Display the plot
    plt.show()
