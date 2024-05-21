import math

from CoresetConstruction import *
from visualize import *


def preprocessing(points: np.ndarray, dimensions: int, delta: float, OPT: float, epsilon: float) -> tuple:
    """
    Implementation of the algorithm "Pre-processing"
    :param points: all points in the dataset
    :param dimensions: the dimensionality of the space
    :param delta: helper value used to calculate the threshold of heavy cells
    :param OPT: the optimal solution to the entire pointset
    :param epsilon: the approximation factor
    :returns: set of sampled points S and subdivision of the space subdivision
    """
    subdivision = coreset_construction(points, dimensions, delta, OPT)

    S = []
    weights = []
    dvc = 2 * dimensions

    # for each cell, either add all points or sample beta points
    for cell in subdivision:
        c = 2
        vcthreshold = (c / epsilon ** 2) * (dvc * math.log(dvc / epsilon, 2))
        beta = min(len(cell.points), vcthreshold)

        # If the cell contains less than or equal to beta points, add all points
        if len(cell.points) <= beta:
            for point in cell.points:
                S.append(point)
                weights.append(1)

        # Else sample beta points
        else:
            sampled_indices = np.random.choice(len(cell.points), size=int(math.ceil(beta)), replace=False)
            sampled_points = [cell.points[i] for i in sampled_indices]
            for point in sampled_points:
                S.append(point)
                weights.append(math.ceil(len(cell.points) / beta))

    return S, subdivision, weights
