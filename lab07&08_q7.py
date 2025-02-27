import math

class Vector2D:
    """Represents a 2D vector or point."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        """Calculates the magnitude (length) of the vector."""
        return math.sqrt(self.x**2 + self.y**2)

    def rotation(self):
        """Calculates the rotation (angle) with respect to the positive x-axis in radians."""
        return math.atan2(self.y, self.x)

    def __str__(self):
        return f"({self.x}, {self.y})"

def distance_2d(v1, v2):
    """Calculates the distance between two 2D vectors."""
    return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)

def dot_product_2d(v1, v2):
    """Calculates the dot product of two 2D vectors."""
    return v1.x * v2.x + v1.y * v2.y

def cross_product_2d(v1, v2):
    """Calculates the cross product of two 2D vectors (returns a scalar)."""
    return v1.x * v2.y - v1.y * v2.x

class Vector3D(Vector2D):
    """Represents a 3D vector or point, inheriting from Vector2D."""

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        """Calculates the magnitude (length) of the 3D vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def distance_3d(v1, v2):
    """Calculates the distance between two 3D vectors."""
    return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2 + (v1.z - v2.z)**2)

def dot_product_3d(v1, v2):
    """Calculates the dot product of two 3D vectors."""
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

def cross_product_3d(v1, v2):
    """Calculates the cross product of two 3D vectors (returns a 3D vector)."""
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Vector3D(x, y, z)

# Example usage:
v1_2d = Vector2D(3, 4)
v2_2d = Vector2D(1, 2)

print(f"2D Vector 1: {v1_2d}")
print(f"2D Vector 2: {v2_2d}")
print(f"Magnitude of v1_2d: {v1_2d.magnitude()}")
print(f"Rotation of v1_2d: {v1_2d.rotation()} radians")
print(f"Distance between v1_2d and v2_2d: {distance_2d(v1_2d, v2_2d)}")
print(f"Dot product of v1_2d and v2_2d: {dot_product_2d(v1_2d, v2_2d)}")
print(f"Cross product of v1_2d and v2_2d: {cross_product_2d(v1_2d, v2_2d)}")

v1_3d = Vector3D(1, 2, 3)
v2_3d = Vector3D(4, 5, 6)

print(f"\n3D Vector 1: {v1_3d}")
print(f"3D Vector 2: {v2_3d}")
print(f"Magnitude of v1_3d: {v1_3d.magnitude()}")
print(f"Distance between v1_3d and v2_3d: {distance_3d(v1_3d, v2_3d)}")
print(f"Dot product of v1_3d and v2_3d: {dot_product_3d(v1_3d, v2_3d)}")
print(f"Cross product of v1_3d and v2_3d: {cross_product_3d(v1_3d, v2_3d)}")
