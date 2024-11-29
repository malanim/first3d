# light.py
import math
class Light:
    def __init__(self, position, intensity):
        self.position = position  # Позиция источника света (x, y, z)
        self.intensity = intensity  # Интенсивность света

class Sun(Light):
    def __init__(self, direction, intensity):
        super().__init__(position=(0, 0, 0), intensity=intensity)
        self.direction = direction  # Направление света (вектор)

class LightManager:
    def __init__(self):
        self.lights = []

    def add_light(self, light):
        self.lights.append(light)

    def get_light_intensity(self, normal):
        total_intensity = 0
        for light in self.lights:
            # Вычисляем интенсивность от каждого источника света
            light_direction = (
                normal[0] - light.position[0],
                normal[1] - light.position[1],
                normal[2] - light.position[2]
            )
            light_direction_length = math.sqrt(sum(d ** 2 for d in light_direction))
            if light_direction_length > 0:
                intensity = max(0, light.intensity * (light_direction[2] / light_direction_length))
                total_intensity += intensity
        return total_intensity