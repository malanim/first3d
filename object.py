from vector import rotate_vector

class Cube:
    def __init__(self):
        self.vertices = [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1]
        ]

    def rotate(self, angle_x, angle_y):
        rotated = [rotate_vector(vertex, angle_x, angle_y) for vertex in self.vertices]
        return rotated