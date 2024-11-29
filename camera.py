class Camera:
    def __init__(self, distance):
        self.distance = distance

    def project(self, cube):
        projected = []
        for x, y, z in cube:
            z += self.distance
            if z == 0:
                z = 0.01  # Avoid division by zero
            scale = 1 / z
            x, y = x * scale, y * scale
            projected.append((x, y))
        return projected