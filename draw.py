import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_line(output, x1, y1, x2, y2):
    # Алгоритм Брезенхэма для рисования линии
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