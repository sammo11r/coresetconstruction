import numpy as np
import math

from PreProcessing import *

def generate_random_points(dimension, num_points, max_coordinate):
    """
    Generate random points in the specified dimension with coordinates in the range {1, ..., max_coordinate}.

    :param dimension: The dimensionality of the space.
    :param num_points: The number of points to generate.
    :param max_coordinate: The maximum coordinate value.
    :return: An array of shape (num_points, dimension) containing the generated points.
    """
    points = np.random.randint(1, max_coordinate + 1, size=(num_points, dimension))
    return points


# Initialize variables
k = 2 # Number of centers
d = 2 # Dimensionality of the space
epsilon = 0.1
n = 100 # number of points
OPT = 10 # Optimal solution to the entire pointset
max_coordinate = 10  # Example maximum coordinate value

# Generate the points
points = generate_random_points(d, n, max_coordinate)
delta = (1 / (4 * k * math.sqrt(d) * (math.log(len(points) + 1, 2)))) * (epsilon / (14 * math.sqrt(d)))**d

print("Generated points:")
print(points)

preprocessing(points, d, delta, OPT, epsilon)