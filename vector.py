import math

def rotate_vector(vector, angle_x, angle_y):
    x, y, z = vector
    # Rotate around the X axis
    y, z = y * math.cos(angle_x) - z * math.sin(angle_x), y * math.sin(angle_x) + z * math.cos(angle_x)
    # Rotate around the Y axis
    x, z = x * math.cos(angle_y) + z * math.sin(angle_y), -x * math.sin(angle_y) + z * math.cos(angle_y)
    return (x, y, z)