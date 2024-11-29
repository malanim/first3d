# renderer.py
import os
from light import Light
import math

class Renderer:
    def render(self, projected):
        raise NotImplementedError("Subclasses should implement this!")

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_line(self, output, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            if 0 <= x1 < len(output[0]) and 0 <= y1 < len(output):
                output[y1][x1] = '#'
            if x1 == x2 and y1 == y2:
                break
            err2 = err * 2
            if err2 > -dy:
                err -= dy
                x1 += sx
            if err2 < dx:
                err += dx
                y1 += sy

    def draw_cube(self, projected):
        self.clear_console()
        output = [[' ' for _ in range(80)] for _ in range(40)]  # Увеличено разрешение до 80x40

        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Задняя грань
            (4, 5), (5, 6), (6, 7), (7, 4),  # Передняя грань
            (0, 4), (1, 5), (2, 6), (3, 7)   # Соединения между гранями
        ]
        
        for edge in edges:
            start, end = edge
            x1, y1 = projected[start]
            x2, y2 = projected[end]
            self.draw_line(output, int(40 + x1 * 20), int(20 - y1 * 20), int(40 + x2 * 20), int(20 - y2 * 20))

        for x, y in projected:
            x = int(40 + x * 20)
            y = int(20 - y * 20)
            if 0 <= x < len(output[0]) and 0 <= y < len(output):
                output[y][x] = '#'
        
        for line in output:
            print(''.join(line))

class BasicRenderer(Renderer):
    def render(self, projected):
        self.draw_cube(projected)  # Использует метод draw_cube из Renderer

class GradientLightingRenderer(Renderer):
    def __init__(self, light_manager):
        self.light_manager = light_manager
        self.gradient_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']  # Символы от темного к светлому

    def render(self, projected):
        self.clear_console()
        output = [[' ' for _ in range(80)] for _ in range(40)]

        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Задняя грань
            (4, 5), (5, 6), (6, 7), (7, 4),  # Передняя грань
            (0, 4), (1, 5), (2, 6), (3, 7)   # Соединения между гранями
        ]

        # Определяем нормали граней
        normals = [
            (0, 0, -1),  # Задняя грань
            (0, 0, 1),   # Передняя грань
            (-1, 0, 0),  # Левая грань
            (1, 0, 0),   # Правая грань
            (0, -1, 0),  # Нижняя грань
            (0, 1, 0)    # Верхняя грань
        ]

        for i, edge in enumerate(edges):
            start, end = edge
            x1, y1 = projected[start]
            x2, y2 = projected[end]
            normal = normals[i // 4]  # Определяем нормаль для текущей грани

            # Используем LightManager для получения общей интенсивности света
            intensity = self.light_manager.get_light_intensity(normal)

            # Определяем индекс символа в зависимости от интенсивности света
            char_index = min(int(intensity * (len(self.gradient_chars) - 1)), len(self.gradient_chars) - 1)
            char = self.gradient_chars[char_index]

            self.draw_line(output, int(40 + x1 * 20), int(20 - y1 * 20), int(40 + x2 * 20), int(20 - y2 * 20), char)

        for x, y in projected:
            x = int(40 + x * 20)
            y = int(20 - y * 20)
            if 0 <= x < len(output[0]) and 0 <= y < len(output):
                output[y][x] = char

        for line in output:
            print(''.join(line))

    def draw_line(self, output, x1, y1, x2, y2, char):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            if 0 <= x1 < len(output[0]) and 0 <= y1 < len(output):
                output[y1][x1] = char
            if x1 == x2 and y1 == y2:
                break
            err2 = err * 2
            if err2 > -dy:
                err -= dy
                x1 += sx
            if err2 < dx:
                err += dx
                y1 += sy