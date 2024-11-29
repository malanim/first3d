# main.py
import time
from camera import Camera
from object import Cube
from input_handler import get_key
from renderer import BasicRenderer, GradientLightingRenderer
from light import LightManager, Sun, Light

def main():
    angle_x, angle_y = 0, 0
    camera_distance = 2.5
    cube_size = 1.0
    camera = Camera(distance=camera_distance)
    cube = Cube()

    light_manager = LightManager()
    light_manager.add_light(Sun(direction=(1, -1, 1), intensity=1))
    # light_manager.add_light(Sun(direction=(-1, -1, 1), intensity=0.5))  # Пример второго источника света

    # Инициализация рендерера
    current_renderer = BasicRenderer()  # Начинаем с базового рендерера

    while True:
        # Изменяем размер куба
        cube.vertices = [[x * cube_size for x in vertex] for vertex in cube.vertices]
        cube_vertices = cube.rotate(angle_x, angle_y)
        projected = camera.project(cube_vertices)

        # Рендеринг с использованием текущего рендерера
        current_renderer.render(projected)

        angle_x += 0.025
        angle_y += 0.025

        # Обработка ввода пользователя
        command = get_key()
        if command == 'q':  # Выход из программы при нажатии 'q'
            break
        elif command == '1':  # Переключение на базовый рендерер
            current_renderer = BasicRenderer()
        elif command == '2':  # Переключение на новый рендерер
            current_renderer = GradientLightingRenderer(light_manager)
        elif command == 'w':  # Увеличение размера куба
            cube_size += 0.1
        elif command == 's':  # Уменьшение размера куба
            cube_size = max(0.1, cube_size - 0.1)  # Минимальный размер куба - 0.1
        elif command == 'a':  # Увеличение расстояния камеры
            camera_distance += 0.1
            camera.distance = camera_distance
        elif command == 'd':  # Уменьшение расстояния камеры
            camera_distance = max(0.1, camera_distance - 0.1)  # Минимальное расстояние камеры - 0.1

        # time.sleep(0.01)

if __name__ == "__main__":
    main()