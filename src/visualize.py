import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import geopandas as gpd


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

    # Set the limits of the plot
    ax.set_xlim(min_coordinate, max_coordinate)
    ax.set_ylim(min_coordinate, max_coordinate)

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Lambda')
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


def visualize_world_map(x_values: list, y_values: list, title='') -> None:
    """
    Visualize points with the world map as a backdrop
    :param x_values: the x values of each point
    :param y_values: the y values of each point
    :param title: the title of the plot
    :return: None
    """
    # Load world map data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Plot the world map
    world.plot(ax=plt.gca(), color='lightgray')

    # Create a scatter plot using seaborn
    sns.scatterplot(x=x_values, y=y_values, s=1, color='blue', edgecolor='none')
    plt.xlabel('longitude')
    plt.ylabel('Latitude')
    plt.title(title)
    plt.grid(False)
    plt.show()


def visualize_clusters(points, labels, centroids, title='') -> None:
    """
    Function used to visualize clusters.
    :param points: Data points.
    :param labels: Cluster labels for each data point.
    :param centroids: Centroids of the clusters.
    :param title: Title of the plot.
    :returns: None
    """
    # Load world map data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Plot the world map
    world.plot(ax=plt.gca(), color='lightgray')

    # Create a scatter plot for each cluster
    for cluster_label in np.unique(labels):
        cluster_points = points[labels == cluster_label]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {cluster_label + 1}')

    # Overlay scatterplot for centroids
    sns.scatterplot(x=centroids[:, 0], y=centroids[:, 1], color='black', alpha=0)
    sns.scatterplot(x=centroids[:, 0], y=centroids[:, 1], marker='x', color='black', label='Centroids')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(title)
    plt.grid(False)
    plt.legend()
    plt.show()
