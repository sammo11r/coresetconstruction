from kmedian import *


def generate_discrete_points(num_points: int, dimension: int, min_val: int, max_val: int):
    """
    Generate a set of unique discrete points in the specified dimension within the given range.

    :param num_points: The number of points to generate.
    :param dimension: The dimensionality of the space in which the points will be generated.
    :param min_val: The minimum value for each coordinate of the points.
    :param max_val: The maximum value for each coordinate of the points.

    :returns: An array containing the generated discrete points, where each row represents a point.
    """
    points_set = set()
    while len(points_set) < num_points:
        point = tuple(np.random.randint(min_val, max_val + 1, size=dimension))
        points_set.add(point)
    points = np.array(list(points_set))
    return points


# Initialize variables
k_array = [10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 100]
dimension = 2
epsilon = 0.25

max_coordinate = float('-inf')
min_coordinate = float('inf')

# Define an empty list to store points
points = []

# Open the dataset file and read each line
with open("../datasets/twitter.txt", "r") as file:
    for line_number, line in enumerate(file):
        # Split the line into timestamp, x, and y components
        timestamp, x, y = line.strip().split()

        # Convert x and y to float and create a point [x, y]
        point = [float(x), float(y)]

        # Update max_coordinate if necessary
        max_coordinate = max(max_coordinate, float(x), float(y))
        min_coordinate = min(min_coordinate, float(x), float(y))

        # Append the point to the list of points
        points.append(point)

points = np.array(points)

# Save points to a file
np.savetxt('points.txt', points)

# Later, load the points from the file
points = np.loadtxt('points.txt')

approximation_list = approximation_ratio_k(k_array, dimension, epsilon, points, min_coordinate, max_coordinate)
print(approximation_list)
