import datetime

my_time = "Jan 15, 2023 - 12:05:33"

python_time = datetime.datetime.strptime(
    my_time, "%b %d, %Y - %H:%M:%S")


print(python_time.month)

human_date = python_time.strftime("%d.%m.%Y, %H:%M")
print(human_date)


temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


hot_temps = list(filter(lambda i: i > 28, temperatures))

print(hot_temps)

print(max(hot_temps))
print(min(hot_temps))
print(round(sum(hot_temps) / len(hot_temps)))
