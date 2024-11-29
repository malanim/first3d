# light.py
class Light:
    def __init__(self, position, intensity):
        self.position = position  # Позиция источника света (x, y, z)
        self.intensity = intensity  # Интенсивность света

class Sun:
    def __init__(self, direction, intensity):
        self.direction = direction  # Направление света (вектор)
        self.intensity = intensity  # Интенсивность света