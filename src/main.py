from PreProcessing import *
from RangedCoresetConstruction import *


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
k = 2 # Number of centers
d = 2 # Dimensionality of the space
epsilon = 0.1
n = 1000 # number of points
OPT = 100 # Optimal solution to the entire pointset
max_coordinate = 10  # Example maximum coordinate value

# Generate the points
# points = generate_discrete_points(n, d, 0, 100)
# Save points to a file
# np.savetxt('points.txt', points)

# Later, load the points from the file
points = np.loadtxt('points.txt')
# print("generated")
delta = (1 / (4 * k * math.sqrt(d) * (math.log(len(points) + 1, 2)))) * (epsilon / (14 * math.sqrt(d)))**d

# Run the preprocessing algorithm
S, subdivision = preprocessing(points, d, delta, OPT, epsilon)

# Define the range
R = [[5, 5], [10, 10]]

# Compute the coreset
Qr = RangeCoresetConstruction(subdivision, S, R)

for point in Qr:
    print(point)
