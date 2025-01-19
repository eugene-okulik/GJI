def repeat_me(func):
    def wrapper(text, count=1):
        result = func(text * count)
        print(result)
    return wrapper


@repeat_me
def print_text(text):
    return text


print_text("Пополнение: 20000 RUB.", count=2)
print_text("Пополнение: 15000 RUB.")
