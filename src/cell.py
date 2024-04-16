import numpy as np

class Cell:
    """
    Class representing a cell in the subdivision of the space, either light or heavy.

    Attributes:
        center (numpy.ndarray): The coordinates of the center of the cell.
        size (float): The size of the cell.
        is_heavy (bool): Indicates whether the cell is classified as heavy.
        subcells (list): A list of subcells if the cell is divided into smaller cells.
        points (list): A list of points contained within the cell.
        parent (Cell or None): The parent cell, if any, that contains the current cell.
    """
    def __init__(self, center, size, parent=None):
        self.center = np.array(center)
        self.size = size
        self.is_heavy = False
        self.subcells = []
        self.points = []
        self.parent = parent

    def calc_points(self, points: np.ndarray) -> int:
        """
        Helper function used to calculate the amount of points in a cell
        :param points: All points in the dataset
        :return: amount of points in the cell
        """
        return 0

    def is_point_inside(self, point) -> bool:
        """
        Check if a given point is inside the boundaries of the cell.
        :param point: The point to check.
        :return: True if the point is inside the cell, False otherwise.
        """
        return True