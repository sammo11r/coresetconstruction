import numpy as np

from cell import Cell


def divide_cell(cell: Cell):
    """
    Helper function used to divide a cell into 2^d equally sized subcells
    :param cell: the parent cell to be divided
    :return: none
    """
    # Divide a heavy cell into 2^d equally sized subcells
    subcell_size = cell.size / 2
    subcell_centers = generate_subcell_centers(cell.center, subcell_size)

    for center in subcell_centers:
        subcell = Cell(center, subcell_size, parent=cell)
        cell.subcells.append(subcell)


def generate_subcell_centers(center: float, subcell_size: float):
    """
    Generate the centers of the subcells in 2 dimensions
    :param center: center of the parent cell
    :param subcell_size: size of the subcells
    :return: list of subcell centers
    """
    offsets = [(1, 1), (-1, 1), (-1, -1), (1, -1)]  # Clockwise order starting from top-right
    subcell_centers = [center + np.array(offset) * subcell_size / 2 for offset in offsets]
    return subcell_centers


def coreset_construction(points: np.ndarray, dimension: int, delta: float, OPT: float):
    """
    Main function - used to calculate the subdivision of the space into light cells
    :param points: the pointset on which the subdivision will be computed
    :param dimension: the dimensionality of the space
    :param delta: helper value used to calculate the threshold of a heavy cell
    :param OPT: the optimal solution to the entire pointset
    """
    # Compute the bounding box of the points
    min_coords, max_coords = np.min(points, axis=0) - 1, np.max(points, axis=0) + 1
    space_size = np.max(max_coords - min_coords)

    # Initialize the root cell covering the bounding box of the points
    root_center = min_coords + space_size / 2
    root_cell = Cell(center=root_center, size=space_size)

    # Recursively subdivide heavy cells into smaller subcells until all cells are light
    stack = [root_cell]
    while stack:
        cell = stack.pop()
        if cell.calc_points(points) >= delta * (OPT / cell.size):
            cell.is_heavy = True
            divide_cell(cell)
            stack.extend(cell.subcells)

    # Collect all light cells
    light_cells = []
    stack = [root_cell]
    while stack:
        cell = stack.pop()
        if not cell.is_heavy:
            light_cells.append(cell)
        else:
            stack.extend(cell.subcells)

    return light_cells
