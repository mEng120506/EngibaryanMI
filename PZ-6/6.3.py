#Дано множество А из N точек на плоскости и точка В (точки заданы своими координатами х, у). Найти точку из множества А,
# наиболее близкую к точке В. Расстояние R между точками с координатами (х1, у1) и (х2, у2) вычисляется по формуле:
#R=√(x2-x1)²+(y2-y1)²
#Для хранения данных о каждом наборе точек следует использовать по два списка: первый список для хранения абсцисс,
# второй для хранения ординат.
import math

# координаты точек из множества А
points_x = [1, 2, 4, 5, 7]
points_y = [3, 5, 2, 6, 1]

# координаты точки В
point_b = (3, 4)

min_distance = float('inf')
closest_point = None

for i in range(len(points_x)):
    distance = math.sqrt((points_x[i] - point_b[0])**2 + (points_y[i] - point_b[1])**2)
    if distance < min_distance:
        min_distance = distance
        closest_point = (points_x[i], points_y[i])

print("Ближайшая точка из множества А к точке B:", closest_point)