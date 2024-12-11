#!/usr/bin/env python3
"""This module provides a function to plot
a histogram of student scores for a project.
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    Plots a histogram of student scores for a project.

    The x-axis is labeled 'Grades'.
    The y-axis is labeled 'Number of Students'.
    The x-axis has bins every 10 units.
    The title of the plot is 'Project A'.
    The bars are outlined in black.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Create an histogram plot
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')

    # Create title and labels
    plt.title('Project A')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')

    # Setting axis ranges
    plt.xticks(range(0, 101, 10))
    plt.xlim(0, 100)
    plt.ylim(0, 30)

    # Display histogram
    plt.show()
