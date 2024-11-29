import math
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def rotate_cube(angle_x, angle_y):
    cube = [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]
    
    rotated = []
    for x, y, z in cube:
        # Rotate around the X axis
        y, z = y * math.cos(angle_x) - z * math.sin(angle_x), y * math.sin(angle_x) + z * math.cos(angle_x)
        # Rotate around the Y axis
        x, z = x * math.cos(angle_y) + z * math.sin(angle_y), -x * math.sin(angle_y) + z * math.cos(angle_y)
        rotated.append((x, y, z))
    
    return rotated

def project_cube(cube, camera_distance):
    projected = []
    for x, y, z in cube:
        z += camera_distance  # Отодвигаем камеру назад
        if z == 0:
            z = 0.01  # Avoid division by zero
        scale = 1 / z
        x, y = x * scale, y * scale
        projected.append((x, y))
    return projected

def draw_line(output, x1, y1, x2, y2):
    # Bresenham's line algorithm
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

def draw_cube(projected):
    clear_console()
    output = [[' ' for _ in range(80)] for _ in range(40)]  # Увеличено разрешение до 80x40
    
    # Рисуем линии между вершинами
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Задняя грань
        (4, 5), (5, 6), (6, 7), (7, 4),  # Передняя грань
        (0, 4), (1, 5), (2, 6), (3, 7)   # Соединения между гранями
    ]
    
    for edge in edges:
        start, end = edge
        x1, y1 = projected[start]
        x2, y2 = projected[end]
        draw_line(output, int(40 + x1 * 20), int(20 - y1 * 20), int(40 + x2 * 20), int(20 - y2 * 20))

    # Рисуем вершины
    for x, y in projected:
        x = int(40 + x * 20)
        y = int(20 - y * 20)
        if 0 <= x < len(output[0]) and 0 <= y < len(output):
            output[y][x] = '#'
    
    for line in output:
        print(''.join(line))

def main():
    angle_x, angle_y = 0, 0
    camera_distance = 2.5  # Расстояние от камеры до куба
    while True:
        cube = rotate_cube(angle_x, angle_y)
        projected = project_cube(cube, camera_distance)
        draw_cube(projected)
        angle_x += 0.025
        angle_y += 0.025
        time.sleep(0.05)

if __name__ == "__main__":
    main()