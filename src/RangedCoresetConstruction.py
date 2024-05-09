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

    for i, point in enumerate(S):
        if R[0][0] <= point[0] <= R[1][0] and R[0][1] <= point[1] <= R[1][1]:
            Qr.append(point)
            Qr_weights.append(weights[i])

    return np.array(Qr), np.array(Qr_weights)


def intersects(cell, R):
    """
    Check if a cell intersects with the query rectangle R
    """
    # Unpack coordinates for better readability
    min_x_cell, min_y_cell = cell.center - cell.size / 2
    max_x_cell, max_y_cell = cell.center + cell.size / 2
    min_x_rect, min_y_rect = R[0]
    max_x_rect, max_y_rect = R[1]

    # Check for intersection along each dimension
    if max_x_cell < min_x_rect or min_x_cell > max_x_rect or \
            max_y_cell < min_y_rect or min_y_cell > max_y_rect:
        return False
    return True


def intersects_points(point, R):
    """
    Check if a point intersects with the query rectangle R
    """
    # Unpack coordinates of the point and rectangle
    x_point, y_point = point
    (min_x_rect, min_y_rect), (max_x_rect, max_y_rect) = R

    # Check if the point is within the rectangle
    return min_x_rect <= x_point <= max_x_rect and min_y_rect <= y_point <= max_y_rect


def contains(cell, R):
    """
    Check if a cell is completely contained within the query rectangle R
    """
    # Check if the min and max coordinates of the cell are within the min and max coordinates of
    # the rectangle along each dimension
    min_x_cell, min_y_cell = cell.center - cell.size / 2
    max_x_cell, max_y_cell = cell.center + cell.size / 2
    min_x_rect, min_y_rect = R[0]
    max_x_rect, max_y_rect = R[1]

    return min_x_rect <= min_x_cell and max_x_cell <= max_x_rect and \
           min_y_rect <= min_y_cell and max_y_cell <= max_y_rect
