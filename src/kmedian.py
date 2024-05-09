import time

from PreProcessing import *
from RangedCoresetConstruction import *
from visualize import *


def kmedian_cost(points, weights, k, max_iter=250) -> int:
    """
    Function used to calculate the optimal cost of a k-median solution

    :param points: the data points which need to be clustered
    :param weights: the weights of the points to be clustered
    :param k: the amount of clusters we need in our solution
    :param max_iter: the maximum amount of iterations of the algorithm, default set to 250
    :returns an integer: representing the optimal cost of a k-median solution
    """
    centroids = points[np.random.choice(points.shape[0], k, replace=False)]

    for _ in range(max_iter):
        # Assign each data point to the closest centroid
        distances = np.zeros((points.shape[0], k))
        for i in range(k):
            distances[:, i] = np.sqrt(np.sum(((points - centroids[i]) ** 2) * weights, axis=1))
        labels = np.argmin(distances, axis=1)

        points = np.array(points)
        # Update centroids to the medians of their respective clusters
        new_centroids = np.array([np.median(points[labels == i], axis=0) for i in range(k)])

        # Check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    # Compute cost of the clustering solution
    cost = np.sum(np.min(distances, axis=1))

    return cost


def approximation_ratio_k(k_array, dimension, epsilon, points, min_coordinate, max_coordinate) -> list:
    """
    Function used to calculate the approximation ratio as a function of k

    :param k_array: array containing all the values for k
    :param dimension: the dimension of the input space
    :param epsilon: the approximation factor
    :param points: the point set
    :param min_coordinate: the minimal coordinate of the input space
    :param max_coordinate: the maximal coordinate of the input space
    :returns list: containing tuples of the form (coreset-cost, total-cost, approximation-ratio)
    """

    approximation_list = []
    running_time_list = []
    for k in k_array:
        total_cost = kmedian_cost(points, np.ones_like(points), k)
        print("Total cost of the clustering solution:", total_cost)

        delta = (1 / (4 * k * math.sqrt(dimension) * (math.log(len(points) + 1, 2)))) * \
                (epsilon / (14 * math.sqrt(dimension))) ** dimension

        # Define the range
        R = [[min_coordinate, max_coordinate], [min_coordinate, max_coordinate]]

        start_time = time.time()

        # Run the preprocessing algorithm
        S, subdivision, weights = preprocessing(points, 2, delta, total_cost, epsilon)

        # Compute the coreset
        Qr, Qr_weights = RangeCoresetConstruction(weights, S, R)
        Qr_weights = Qr_weights.reshape(len(Qr_weights), 1)

        # Calculate the running time, and the coreset cost
        end_time = time.time()
        running_time = start_time - end_time
        coreset_cost = kmedian_cost(Qr, Qr_weights, k)

        # Update the lists accordingly
        approximation_list.append([coreset_cost, total_cost, coreset_cost / total_cost])
        running_time_list.append(running_time)

    return approximation_list
