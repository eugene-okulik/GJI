
# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name)     # для проверки


# Задание 2

answer_1 = "результат операции: 42"
result_1 = (answer_1[20:])
print(int(result_1) + 10)


answer_2 = "результат операции: 514"
result_2 = (answer_2[20:])
print(int(result_2) + 10)

answer_3 = "результат операции: 9"
result_3 = (answer_3[20:])
print(int(result_3) + 10)

# Не поняла зачем это нужно решать используя index, но вот так получилось, чуть больше кода.
other_1 = "результат операции: 42"
idx_var_1 = other_1.index(':')
num_1 = int(other_1[idx_var_1 + 1:])
print(num_1 + 10)

other_2 = "результат операции: 514"
idx_var_2 = other_2.index(':')
num_2 = int(other_2[idx_var_2 + 1:])
print(num_2 + 10)

other_3 = "результат операции: 9"
idx_var_3 = other_3.index(':')
num_3 = int(other_3[idx_var_3 + 1:])
print(num_3 + 10)


# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
iva, pet, sid = students

subjects = ['math', 'biology', 'geography']
mat, bio, geo = subjects

print(
    f"Students {iva}, {pet}, {sid} study these subjects: {mat}, {bio}, {geo}")
