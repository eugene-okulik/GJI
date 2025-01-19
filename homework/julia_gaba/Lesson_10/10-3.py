def operation_decorator(func):
    def wrapper(first, second, operation=None):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'

        return func(first, second, operation)
    return wrapper


@operation_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

result = calc(first_number, second_number)
print(result)
