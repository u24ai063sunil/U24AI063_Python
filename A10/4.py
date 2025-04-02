import numpy as np

def cartesian_to_polar(points):
    """Convert Cartesian coordinates to polar."""
    r = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
    theta = np.arctan2(points[:, 1], points[:, 0])
    return np.column_stack((r, theta))

N = 10
points = np.random.rand(N, 2) * 10
polar_points = cartesian_to_polar(points)

print("Cartesian Points:\n", points)
print("Polar Coordinates:\n", polar_points)
