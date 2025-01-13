
# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
try:
    name, last_name, city, phone, country = person
except ValueError:
    print("Error: Added new elements in the list!")


# Задание 2

result_list = [
    "результат операции: 42",
    "результат операции: 514",
    "результат операции: 9"
]

for result in result_list:
    result_idx = result.index(':')
    result_num = int(result[result_idx + 2:])

    print(result_num)

# result_list = [
#     "результат операции: 42",
#     "результат операции: 514",
#     "результат операции: 9"
# ]

# for result in result_list:
#     parts = result.split()
#     # print(parts)
#     # вижу, что все part являются <class 'str'>  далее преобразую 'число' в int

#     for part in parts:
#         if part.isdigit():
#             result_num = int(part)
#             print(result_num)


# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)
subjects_str = ', '.join(subjects)

match_students = f"Students {students_str} study these subjects: {subjects_str}"

print(match_students)
