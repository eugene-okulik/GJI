def finish_me(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
        print('finished')
        return result
    return wrapper


@finish_me
def get_sq(width, height):
    return width * height


get_sq(8, 11)
