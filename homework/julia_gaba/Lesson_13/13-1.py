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


with open('hw13-1.txt', 'w') as julis_file:
    for data_line in read_file():
        start = data_line.find('.') + 1
        end = data_line.find('- ')
        date_str = data_line[start:end].strip()

        print(str(date_str))

        date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        if "на неделю позже" in data_line:
            new_date = date + datetime.timedelta(weeks=1)
            formatted_date = (
                f"{new_date.year}-{new_date.month}-{new_date.day} "
                f"{new_date.strftime('%-H:%M:%S.%f')}".rstrip('0').rstrip('.'))

            julis_file.write(formatted_date + "\n")
            formatted_date_str = str(formatted_date)
            print(formatted_date_str)

        if "день недели" in data_line:
            weekday = date.strftime('%A')
            julis_file.write(weekday + "\n")
            print(weekday)

        if "сколько дней назад" in data_line:
            days_ago = (datetime.datetime.now() - date).days
            julis_file.write(str(days_ago) + "\n")
            print(days_ago)
