import sys
sys.set_int_max_str_digits(100000)


def fibonacci():
    f1 = 0
    f2 = 1
    while True:
        yield f1
        old_f1, old_f2 = f1, f2
        f1 = old_f1 + old_f2
        f2 = f1


count_list = [5, 200, 1000, 100_000]

results = []
count = 1

for number in fibonacci():
    if count in count_list:
        results.append(number)
        print(number)
        if len(results) == len(count_list):
            break
    count += 1
