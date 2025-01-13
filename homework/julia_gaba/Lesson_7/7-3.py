
stroki = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


def find_and_culc(stroka):
    for item in stroka.split():
        if item.isdigit():
            num = int(item)
            new_stroka = stroka.replace(str(num), str(int(num + 10)))
            return (new_stroka)


for stroka in stroki:
    print(find_and_culc(stroka))
