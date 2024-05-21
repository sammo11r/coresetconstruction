import numpy as np


def RangeCoresetConstruction(weights: list, S: list, R: list) -> tuple:
    """
    Method used to compute the coreset for the range R
    :param weights: the weights of the points
    :param S: a set of points S
    :param R: the query rectangle R
    :return: an array Qr representing the coreset for P ∩ R
    """
    Qr = []
    Qr_weights = []

    # Check if R is a triangle
    if len(R) == 3:
        for i, point in enumerate(S):
            if point_in_triangle(point, R):
                Qr.append(point)
                Qr_weights.append(weights[i])

    # R is a rectangle
    else:
        for i, point in enumerate(S):
            if R[0][0] <= point[0] <= R[1][0] and R[0][1] <= point[1] <= R[1][1]:
                Qr.append(point)
                Qr_weights.append(weights[i])

    return np.array(Qr), np.array(Qr_weights)


def point_in_triangle(point, R) -> bool:
    """
    Check if a point is inside of a triangle
    :param point: the point to be checked
    :param R: the triangle to be checked
    :return: a boolean representing if the point is inside of the triangle
    """
    # Get the vertices of the triangle
    v1, v2, v3 = R[0], R[1], R[2]
    x, y = point

    # Compute barycentric coordinates
    denominator = ((v2[1] - v3[1]) * (v1[0] - v3[0]) + (v3[0] - v2[0]) * (v1[1] - v3[1]))
    alpha = ((v2[1] - v3[1]) * (x - v3[0]) + (v3[0] - v2[0]) * (y - v3[1])) / denominator
    beta = ((v3[1] - v1[1]) * (x - v3[0]) + (v1[0] - v3[0]) * (y - v3[1])) / denominator
    gamma = 1 - alpha - beta

    # Check if the point is inside the triangle
    return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1
