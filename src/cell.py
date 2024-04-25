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
        if self.parent is not None:
            self.points = [point for point in self.parent.points if
                           self.is_point_inside(point) and point not in self.points]
        else:
            self.points = [point for point in points if self.is_point_inside(point) and point not in self.points]
        return len(self.points)

    def is_point_inside(self, point) -> bool:
        """
        Check if a given point is inside the boundaries of the cell.
        :param point: The point to check.
        :return: True if the point is inside the cell, False otherwise.
        """
        if len(self.center) != len(point):
            raise ValueError("Dimension mismatch: cell center and point must have the same dimensionality")

        for i in range(len(self.center)):
            if not self.center[i] - self.size / 2 <= point[i] < self.center[i] + self.size / 2:
                return False
        return True
