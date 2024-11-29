import time
from camera import Camera
from object import Cube
from input_handler import get_key
from draw import draw_cube
from light import Light, Sun

def main():
    angle_x, angle_y = 0, 0
    camera_distance = 2.5
    cube_size = 1.0  # Размер куба
    camera = Camera(distance=camera_distance)
    cube = Cube()
    # Создание источников света
    # point_light = Light(position=(0, 0, 1), intensity=1.0)
    sun = Sun(direction=(1, -1, -1), intensity=0.5)

    while True:
        # Здесь можно изменить размер куба, если вы добавите соответствующий метод в класс Cube
        cube.vertices = [[x * cube_size for x in vertex] for vertex in cube.vertices]

        cube_vertices = cube.rotate(angle_x, angle_y)
        projected = camera.project(cube_vertices)
        draw_cube(projected)

        angle_x += 0.025
        angle_y += 0.025

        # Обработка ввода пользователя
        command = get_key()
        if command == 'q':  # Выход из программы при нажатии 'q'
            break
        elif command == 'w':  # Увеличение размера куба
            cube_size += 0.1
        elif command == 's':  # Уменьшение размера куба
            cube_size = max(0.1, cube_size - 0.1)  # Минимальный размер куба - 0.1
        elif command == 'a':  # Увеличение расстояния камеры
            camera_distance += 0.1
            camera.distance = camera_distance
        elif command == 'd':  # Уменьшение расстояния камеры
            camera_distance = max(0.1, camera_distance - 0.1)  # Минимальное расстояние камеры - 0.1

        time.sleep(0.05)

if __name__ == "__main__":
    main()