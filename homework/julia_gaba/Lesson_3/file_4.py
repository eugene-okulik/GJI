# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
import math


def triangle_properties(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    area = (a * b) / 2

    return hypotenuse, area


hypotenuse, area = triangle_properties(3, 4)
print(f"Гипотенуза: {hypotenuse}")
print(f"Площадь: {area}")
