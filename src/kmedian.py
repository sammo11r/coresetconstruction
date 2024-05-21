import time

from haversine import haversine_vector, Unit
from PreProcessing import *
from RangedCoresetConstruction import *
from visualize import *


def kmedian_cost(points: np.array, weights: list, k: int, max_iter=250, dist='euclidean') -> int:
    """
    Function used to calculate the optimal cost of a k-median solution

    :param points: the data points which need to be clustered
    :param weights: the weights of the points to be clustered
    :param k: the amount of clusters we need in our solution
    :param max_iter: the maximum amount of iterations of the algorithm, default set to 250
    :param dist: the distance formula used to calculate the k median cost, default is set to the Euclidean distance
    :returns an integer: representing the optimal cost of a k-median solution
    """
    centroids = points[np.random.choice(points.shape[0], k, replace=False)]

    for _ in range(max_iter):
        # Assign each data point to the closest centroid
        distances = np.zeros((points.shape[0], k))
        if dist == 'euclidean':
            for i in range(k):
                distances[:, i] = np.sqrt(np.sum(((points - centroids[i]) ** 2) * weights, axis=1))
        else:
            for i in range(k):
                centroid = centroids[i]
                distances[:, i] = haversine_vector((centroid[0], centroid[1]), (points[:, 0], points[:, 1]),
                                                   Unit.KILOMETERS)

        labels = np.argmin(distances, axis=1)
        points = np.array(points)

        # Update centroids to the medians of their respective clusters
        new_centroids = np.array([np.median(points[labels == i], axis=0) for i in range(k)])

        # Check for convergence
        if np.all(centroids == new_centroids):
            print("Converge")
            break

        centroids = new_centroids

    # Compute cost of the clustering solution
    cost = np.sum(np.min(distances, axis=1))

    return cost


def approximation_ratio_k(k_array, dimension, epsilon, points, min_coordinate, max_coordinate) -> tuple:
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
        # Compute the total cost
        total_cost = kmedian_cost(points, np.ones_like(points), k)

        # Compute delta
        delta = (1 / (4 * k * math.sqrt(dimension) * (math.log(len(points) + 1, 2)))) * \
                (epsilon / (14 * math.sqrt(dimension))) ** dimension

        start_time = time.time()

        # Run the preprocessing algorithm
        S, subdivision, weights = preprocessing(points, dimension, delta, total_cost, epsilon)
        weights = np.array(weights)
        weights = weights.reshape(len(weights), 1)

        # Define the range
        R = [[min_coordinate, min_coordinate], [max_coordinate, max_coordinate]]

        # Compute the coreset
        Qr, Qr_weights = RangeCoresetConstruction(weights, S, R)
        Qr_weights = Qr_weights.reshape(len(Qr_weights), 1)

        # Calculate the running time
        end_time = time.time()
        running_time = end_time - start_time

        # Calculate the coreset cost
        coreset_cost = kmedian_cost(Qr, Qr_weights, k)

        # Update the lists accordingly
        approximation_list.append([coreset_cost, total_cost, coreset_cost / total_cost])
        running_time_list.append(running_time)

        print("approximation values: ", coreset_cost, total_cost, coreset_cost / total_cost)
        print("Running time: ", running_time)

    return approximation_list, running_time_list


def approximation_ratio_eps(k, dimension, epsilon_array, points, min_coordinate, max_coordinate) -> tuple:
    """
    Function used to calculate the approximation ratio as a function of k

    :param k: the amount of clusters we consider
    :param dimension: the dimension of the input space
    :param epsilon_array: an array containing the approximation factors
    :param points: the point set
    :returns list: containing tuples of the form (coreset-cost, total-cost, approximation-ratio)
    """
    approximation_list = []
    running_time_list = []

    for epsilon in epsilon_array:
        # Compute the total cost
        total_cost = kmedian_cost(points, np.ones_like(points), k)

        # Compute delta
        delta = (1 / (4 * k * math.sqrt(dimension) * (math.log(len(points) + 1, 2)))) * \
                (epsilon / (14 * math.sqrt(dimension))) ** dimension

        start_time = time.time()

        # Run the preprocessing algorithm
        S, subdivision, weights = preprocessing(points, dimension, delta, total_cost, epsilon)
        weights = np.array(weights)
        weights = weights.reshape(len(weights), 1)

        # Define the range
        R = [[min_coordinate, min_coordinate], [max_coordinate, max_coordinate]]

        # Compute the coreset
        Qr, Qr_weights = RangeCoresetConstruction(weights, S, R)
        Qr_weights = Qr_weights.reshape(len(Qr_weights), 1)

        # Calculate the running time
        end_time = time.time()
        running_time = end_time - start_time

        # Compute the coreset cost
        coreset_cost = kmedian_cost(Qr, Qr_weights, k)

        # Update the lists accordingly
        approximation_list.append([coreset_cost, total_cost, coreset_cost / total_cost])
        running_time_list.append(running_time)

        print("approximation values: ", coreset_cost, total_cost, coreset_cost / total_cost)
        print("Running time: ", running_time)

    return approximation_list, running_time_list


def calc_range(S: any, weights: any, R: list, k: int) -> tuple:
    """
    Function used to calculate the cost of a range on a set of points
    :param S: the set of points on which to calculate the range
    :param weights: the corresponding set of weights
    :param R: the range
    :param k: the amount of clusters to consider
    :return: a tuple containing the points in the range, their weights and their labels
    """

    # Compute the coreset
    Qr, Qr_weights = RangeCoresetConstruction(weights, S, R)
    Qr_weights = Qr_weights.reshape(len(Qr_weights), 1)

    # Cluster the coreset points using k-median algorithm
    centroids = Qr[np.random.choice(Qr.shape[0], k, replace=False)]
    for _ in range(250):  # maximum iterations
        distances = np.zeros((Qr.shape[0], k))
        for i in range(k):
            distances[:, i] = np.sqrt(np.sum(((Qr - centroids[i]) ** 2) * Qr_weights, axis=1))

        labels = np.argmin(distances, axis=1)
        new_centroids = np.array([np.median(Qr[labels == i], axis=0) for i in range(k)])

        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return Qr, Qr_weights, labels
