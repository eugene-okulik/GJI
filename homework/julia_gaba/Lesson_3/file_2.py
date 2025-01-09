# Даны числа x и y. Получить x − y / 1 + xy

def calculate(x, y):
    return (x - y) / (1 + x * y)


print(calculate(3, 1))
