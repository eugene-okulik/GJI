def fibonacci(limit=110_000):
    f1 = 0
    f2 = 1
    count = 1
    while count < limit:
        yield f2
        f2 += f1
        count += 1


count = 1
for number in fibonacci(110_000):
    if count == 5:
        print(number)
        break
    count += 1

count = 1
for number in fibonacci(110_000):
    if count == 200:
        print(number)
        break
    count += 1

count = 1
for number in fibonacci(110_000):
    if count == 1000:
        print(number)
        break
    count += 1

count = 1
for number in fibonacci(110_000):
    if count == 100_000:
        print(number)
        break
    count += 1

# я что-то напутала, помогите плиз!
