import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

def distance_2d(v1, v2):
    return math.sqrt((v2.x - v1.x)**2 + (v2.y - v1.y)**2)

def dot_product_2d(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

def cross_product_2d(v1, v2):
    return v1.x * v2.y - v1.y * v2.x

# 3D Vector using inheritance

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

def distance_3d(v1, v2):
    return math.sqrt((v2.x - v1.x)**2 + (v2.y - v1.y)**2 + (v2.z - v1.z)**2)

def dot_product_3d(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

def cross_product_3d(v1, v2):
    return Vector3D(v1.y * v2.z - v1.z * v2.y,
                    v1.z * v2.x - v1.x * v2.z,
                    v1.x * v2.y - v1.y * v2.x)


v1_2d = Vector2D(3, 4)
v2_2d = Vector2D(1, 2)

print(f"Magnitude of v1 (2D): {v1_2d.magnitude()}")
print(f"Rotation of v1 (2D): {v1_2d.rotation()}")
print(f"Distance between v1 and v2 (2D): {distance_2d(v1_2d, v2_2d)}")
print(f"Dot product of v1 and v2 (2D): {dot_product_2d(v1_2d, v2_2d)}")
print(f"Cross product of v1 and v2 (2D): {cross_product_2d(v1_2d, v2_2d)}")

v1_3d = Vector3D(1, 2, 3)
v2_3d = Vector3D(4, 5, 6)

print(f"\nMagnitude of v1 (3D): {v1_3d.magnitude()}")
print(f"Distance between v1 and v2 (3D): {distance_3d(v1_3d, v2_3d)}")
print(f"Dot product of v1 and v2 (3D): {dot_product_3d(v1_3d, v2_3d)}")
print(f"Cross product of v1 and v2 (3D): {cross_product_3d(v1_3d, v2_3d)}")
