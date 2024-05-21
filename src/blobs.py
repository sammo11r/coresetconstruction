from kmedian import *
from sklearn.datasets import make_blobs

# Generate the first blobs dataset
# Number of centers
num_centers = 16

# Generate blobs around the specified centers
X, y = make_blobs(n_samples=100000, centers=num_centers, cluster_std=1, random_state=42)

# Combine X and Y coordinates into an array
points = np.column_stack((X[:, 0], X[:, 1]))

# Save the pointset
np.savetxt('blobs_points_1.txt', points)
points = np.array(points)


# Generate the second blobs dataset
# Generate grid coordinates for the centers
x_centers = np.linspace(0, 20000, int(np.sqrt(num_centers)))
y_centers = np.linspace(0, 20000, int(np.sqrt(num_centers)))
x_mesh, y_mesh = np.meshgrid(x_centers, y_centers)
centers = np.vstack([x_mesh.ravel(), y_mesh.ravel()]).T

# Generate blobs around the specified centers
X, y = make_blobs(n_samples=10000000, centers=centers, cluster_std=750, random_state=42)

# Combine X and Y coordinates into an array
points = np.column_stack((X[:, 0], X[:, 1]))

# Save the pointset
np.savetxt('blobs_points_2.txt', points)

points = np.array(points)
points = np.array(points)

# Initialize variables
dimension = 2
k_array = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
k = 20
epsilon = 0.25
epsilon_array = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

max_coordinate = float('-inf')
min_coordinate = float('inf')

# Run the experiments
approximation_list, running_time_list = approximation_ratio_k(k_array, dimension, epsilon, np.array(points),
                                                              min_coordinate, max_coordinate)
print("Approximations - k: ", approximation_list)
print("Running Times - k: ", running_time_list)

approximation_list, running_time_list = approximation_ratio_eps(k, dimension, epsilon_array, np.array(points),
                                                              min_coordinate, max_coordinate)
print("Approximations - eps: ", approximation_list)
print("Running Times - eps: ", running_time_list)
