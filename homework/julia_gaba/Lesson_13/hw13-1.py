import os
import datetime

base_path = os.path.dirname(__file__)
print(base_path)

homework_path = os.path.dirname(os.path.dirname(base_path))
print(homework_path)

eugene_file_path = os.path.join(
    homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_file_path)


def read_file():
    with open(eugene_file_path, 'r') as eugene_file:
        for line in eugene_file.readlines():
            yield line


with open('hw13-1.py', 'a') as julis_file:
    for data_line in read_file():

        start = data_line.find('.') + 1
        end = data_line.find('- ')
        date_str = data_line[start:end].strip()

        print(date_str)

        date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        if "на неделю позже" in data_line:
            new_date = date + datetime.timedelta(weeks=1)
            julis_file.write(str(new_date))
            print(str(new_date))

        if "день недели" in data_line:
            weekday = date.strftime('%A')
            julis_file.write(str(weekday))
            print(str(weekday))

        if "сколько дней назад" in data_line:
            days_ago = (datetime.datetime.now() - date).days
            julis_file.write(str(days_ago))
            print(str(days_ago))
