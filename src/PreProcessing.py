import math

from CoresetConstruction import *
from visualize import *


def preprocessing(points: np.ndarray, dimensions: int, delta: float, OPT: float, epsilon: float):
    """
    Implementation of the algorithm "Pre-processing"
    :param points: all points in the dataset
    :param dimensions: the dimensionality of the space
    :param delta: helper value used to calculate the threshold of heavy cells
    :param OPT: the optimal solution to the entire pointset
    :param epsilon: the approximation factor
    """
    subdivision = coreset_construction(points, dimensions, delta, OPT)
    # plot_light_cells(subdivision)

    S = []
    dvc = 2 * dimensions

    # for each cell, either add all points or sample beta points
    for cell in subdivision:
        c = 1
        vcthreshold = (c / epsilon ** 2) * (dvc * math.log(dvc / epsilon, 2))
        beta = min(len(cell.points), vcthreshold)

        # If the cell contains less than or equal to beta points, add all points
        if len(cell.points) <= beta:
            S.extend(cell.points)
        # Else sample beta points
        else:
            sampled_indices = np.random.choice(len(cell.points), size=int(beta), replace=False)
            sampled_points = [cell.points[i] for i in sampled_indices]
            S.extend(sampled_points)

    return S, subdivision
