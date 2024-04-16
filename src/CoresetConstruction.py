import numpy as np

def coreset_construction(points: np.ndarray, dimension, delta, OPT):
    """
    Main function - used to calculate the subdivision of the space into light cells
    :param points: the pointset on which the subdivision will be computed
    :param dimension: the dimensionality of the space
    :param delta: helper value used to calculate the threshold of a heavy cell
    :param OPT: the optimal solution to the entire pointset
    """
    subdivision = []

    return subdivision