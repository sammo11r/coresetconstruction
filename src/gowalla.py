import numpy as np
from kmedian import *

# Initialize variables
dimension = 2
k_array = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
k = 20
epsilon = 0.25
epsilon_array = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

# Load the points
max_coordinate = float('-inf')
min_coordinate = float('inf')
points = []

# Open the dataset file and read each line
with open("../datasets/Gowalla/Gowalla_totalCheckins.txt", "r") as file:
    for line_number, line in enumerate(file):
        # Split the line into its components
        user, check_in_time, long, lat, location = line.strip().split()

        # Convert x and y to float
        x_float, y_float = float(lat), float(long)

        # Remove invalid points
        if abs(x_float) > 180 or abs(y_float) > 180:
            continue

        # Create a point
        point = [x_float, y_float]

        # Append the point to the list
        points.append(point)

points = np.array(points)

# Update max_coordinate and min_coordinate if necessary
max_coordinate = max(max_coordinate, *map(max, points))
min_coordinate = min(min_coordinate, *map(min, points))

# Extract x and y coordinates
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

# Save points to a file
np.savetxt('points.txt', points)

# Later, load the points from the file
points = np.loadtxt('points.txt')

# Run the experiments
approximation_list, running_time_list = approximation_ratio_k(k_array, dimension, epsilon, np.array(points),
                                                              min_coordinate, max_coordinate)
print("Approximations - k: ", approximation_list)
print("Running Times - k: ", running_time_list)

approximation_list, running_time_list = approximation_ratio_eps(k, dimension, epsilon_array, np.array(points),
                                                              min_coordinate, max_coordinate)
print("Approximations - eps: ", approximation_list)
print("Running Times - eps: ", running_time_list)
