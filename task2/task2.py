import math
import sys

def read_circle(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        first_line = lines[0].strip().split()

        if len(first_line) == 3:  # Все значения на одной строке
            x0, y0, r = map(float, first_line)
        elif len(first_line) == 2 and len(lines) >= 2:  # Координаты на первой строке, радиус на второй
            x0, y0 = map(float, first_line)
            r = float(lines[1].strip())
        else:
            raise ValueError("Файл с окружностью должен содержать координаты центра и радиус в корректном формате.")

    return x0, y0, r

def read_points(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            x, y = line.split()
            points.append((float(x), float(y)))
    return points

def check_position(x, y, x0, y0, r):
    distance = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
    if math.isclose(distance, r):
        return 0
    elif distance < r:
        return 1
    else:
        return 2

circle_file = sys.argv[1]
points_file = sys.argv[2]

try:
    x0, y0, r = read_circle(circle_file)
    points = read_points(points_file)

    for x, y in points:
        result = check_position(x, y, x0, y0, r)
        print(result)
except Exception as e:
    print(f"Ошибка: {e}")
