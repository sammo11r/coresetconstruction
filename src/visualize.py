import matplotlib.pyplot as plt


def plot_light_cells(cells):
    """
    Method used to plot the subdivision of the space into light cells
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
    ax.set_xlim(-1, 110)
    ax.set_ylim(-1, 110)

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Cell Subdivision')
    plt.show()
