import math 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def distance_between(point1: list, point2: list):
    """
    Calculate the Euclidean distance between two points in 3-dimensional space.

    Args:
        point1 (list): The coordinates of the first point as a list of three numbers [x1, y1, z1].
        point2 (list): The coordinates of the second point as a list of three numbers [x2, y2, z2].

    Returns:
        float: The Euclidean distance between the two points.

    Raises:
        TypeError: If point1 or point2 are not lists or if their elements are not numbers.
        ValueError: If point1 or point2 does not contain exactly three elements or if the list is empty.
    """
    # Verificación de tipo de dato lista
    if not isinstance(point1, list) or not isinstance(point2, list):
        raise TypeError("Both point1 and point2 must be of type list")

    # Verificación de que la lista no esté vacía
    if len(point1) == 0 or len(point2) == 0:
        raise ValueError("Points must not be empty")

    # Verificación de dimensión
    if len(point1) != 3 or len(point2) != 3:
        raise ValueError("The points must be in 3 dimensions (exactly 3 elements each)")

    # Verificación de que todos los elementos sean numéricos
    for coord in point1 + point2:
        if not isinstance(coord, (int, float)):
            raise TypeError("All coordinates must be integers or floats")
    
    squared_result = ((point2[0] - point1[0]) ** 2 +
                      (point2[1] - point1[1]) ** 2 +
                      (point2[2] - point1[2]) ** 2)
    
    return math.sqrt(squared_result)


def plot_distance(point1: list, point2: list):
    """
    Plot two points in 3D space and the line connecting them, along with displaying the distance between the points.

    Args:
        point1 (list): The coordinates of the first point as a list of three numbers [x1, y1, z1].
        point2 (list): The coordinates of the second point as a list of three numbers [x2, y2, z2].

    Raises:
        TypeError: If point1 or point2 are not lists or if their elements are not numbers.
        ValueError: If point1 or point2 does not contain exactly three elements or if the list is empty.
    """
    if not isinstance(point1, list) or not isinstance(point2, list):
        raise TypeError("Both point1 and point2 must be of type list")

    if len(point1) == 0 or len(point2) == 0:
        raise ValueError("Points must not be empty")

    if len(point1) != 3 or len(point2) != 3:
        raise ValueError("The points must be in 3 dimensions (exactly 3 elements each)")

    for coord in point1 + point2:
        if not isinstance(coord, (int, float)):
            raise TypeError("All coordinates must be integers or floats")
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    z_values = [point1[2], point2[2]]

    ax.scatter(x_values, y_values, z_values, c='darkred', marker='o')
    ax.plot(x_values, y_values, z_values, color='b')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    distance = distance_between(point1, point2)
    mid_x = (point1[0] + point2[0])
    mid_y = (point1[1] + point2[1]) / 2
    mid_z = (point1[2] + point2[2]) / 2
    ax.text(mid_x, mid_y, mid_z, f'Distancia: {distance:.2f}', color='darkblue')

    plt.show()
