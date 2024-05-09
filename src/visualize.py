import matplotlib.pyplot as plt
import numpy as np


def plot_light_cells(cells: list, min_coordinate: float, max_coordinate: float) -> None:
    """
    Method used to plot the subdivision of the space into light cells

    :param cells: a list containing all the cells in the subdivision
    :param min_coordinate: a real number representing the minimum coordinate of any point in the point set
    :param max_coordinate: a real number representing the maximum coordinate of any point in the point set
    :returns None:
    """
    fig, ax = plt.subplots()

    for cell in cells:
        rect = plt.Rectangle((cell.center[0] - cell.size / 2, cell.center[1] - cell.size / 2), cell.size, cell.size,
                             fill=False, color='blue')
        ax.add_patch(rect)

        # Display amount of points within the cell at its center
        amount = len(cell.points)
        text_size = min(10, max(8, cell.size / 3))  # Adjust text size based on cell size
        ax.text(cell.center[0], cell.center[1], str(amount), fontsize=text_size,
                horizontalalignment='center', verticalalignment='center')

    # Set the limits of the plot
    ax.set_xlim(min_coordinate, max_coordinate)
    ax.set_ylim(min_coordinate, max_coordinate)

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Cell Subdivision')
    plt.show()


def visualize_points(points: np.ndarray, title: str) -> None:
    """
    Visualize a set of points using Matplotlib.

    :param points: A list of points, where each point is a list [x, y]
    :param title: The title of the plot
    :returns None:
    """
    # Extract x and y coordinates from points
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, s=1)  # s parameter controls the marker size

    # Set plot title and labels
    plt.title(title)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    # Show plot
    plt.show()


def visualize_points_with_centroids(points: list, centroids: list) -> None:
    """
    Visualize a set of points and centroids.

    :param points: A list of points, where each point is a list [x, y]
    :param centroids: A list of centroids, where each centroid is a list [x, y]
    :returns None:
    """

    # Convert points and centroids to numpy arrays
    points = np.array(points)
    centroids = np.array(centroids)

    # Visualize points
    plt.figure(figsize=(8, 6))
    plt.scatter(points[:, 0], points[:, 1], s=1, c='blue', label='Points')  # s parameter controls marker size

    # Plot centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='red', s=100, label='Centroids')

    # Set plot title and labels
    plt.title('Visualization of Points with Centroids')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()

    # Show plot
    plt.show()
