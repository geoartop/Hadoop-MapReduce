__author__ = 'Theodoros Malikourtis & Georgios Artopoulos'

import numpy as np

# Define the three cluster centers
centers = np.array([[0, 1], [4, 5], [7, 8]])

# Define the number of points per cluster
n_points = 350000

# Define the standard deviation of the distance from the centers
std = 1

# Define the degree of skewness
skew = 0.1

# Generate the points around the centers with skewness
points = np.concatenate([
    np.random.normal(center, std, size=(n_points, 2)) + skew * np.random.normal(size=(n_points, 2))
    for center in centers
])

# Save the points to a text file
np.savetxt('data.txt', points, delimiter=',')
