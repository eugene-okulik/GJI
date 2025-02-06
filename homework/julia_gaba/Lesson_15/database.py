import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)


# Добавляем студента. Закомитить после правильного выполнения!
# cursor.execute('''
#     INSERT INTO students (name, second_name)
#     VALUES (%s, %s)''', ('Lena', 'Popova'))
# my_student_id = cursor.lastrowid
# db.commit()
# print(my_student_id)

# Получаем моего студента (4264 Lena Popova)
cursor.execute("SELECT * FROM students WHERE id = %s", (4264,))

print(cursor.fetchone())


# Добавляем группу. Закомитить после правильного выполнения!
# cursor.execute('''
#     INSERT INTO `groups` (title, start_date, end_date)
#     VALUES (%s, %s, %s)''',('Desperate Housewives', 'Dec 2024', 'Dec 2025'))
# my_group_id = cursor.lastrowid
# db.commit()
# print(my_group_id)


# Получаем группу (2686 Desperate Housewives)
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (2686,))

print(cursor.fetchone())

# # Обновляем группу студента
cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s", (2686, 4264))
db.commit()


# # Добавляем книги. Закомитить после правильного выполнения!
# books_data = [
#     ('Бедный богатый папа', 4264),
#     ('Атомные привычки', 4264),
#     ('Мой любимый Python', 4264)
# ]
# cursor.executemany('''
#     INSERT INTO books (title, taken_by_student_id)
#     VALUES(%s, %s)''',
#                    books_data),
# db.commit()


# # Добавляем предметы. Закомитить после правильного выполнения!
# subjects_data = [
#     ('Вокал',),
#     ('Барабаны',),
#     ('Гитара',)
# ]
#
# cursor.executemany('''
#     INSERT INTO subjets (title)
#     VALUES(%s)''',
#                    subjects_data)
# db.commit()

# # Получаем ID предметов (4289, 4290, 4291)
cursor.execute("SELECT * FROM subjets ORDER BY id DESC LIMIT 3")

print(cursor.fetchall())


# # Добавляем уроки. Закомитить после правильного выполнения!
lessons_data = [
    ('Вокал lesson 1', 4289),
    ('Вокал lesson 2', 4289),
    ('Барабаны lesson 1', 4290),
    ('Барабаны lesson 2', 4290),
    ('Гитара lesson 1', 4291),
    ('Гитара lesson 2', 4291)
]
cursor.executemany('''
    INSERT INTO lessons (title, subject_id)
    VALUES(%s, %s)''',
                   lessons_data)
db.commit()
lessons_first_id = cursor.lastrowid

lessons_ids = list(range(lessons_first_id, lessons_first_id + len(lessons_data)))
print(lessons_ids)


# Получаем ID уроков (7994-7999) Закомитить тоже
cursor.execute(f"SELECT * FROM lessons WHERE id BETWEEN %s AND %s", (lessons_ids[0], lessons_ids[5]))

print(cursor.fetchall())


# Добавляем оценки. Закомитить после правильного выполнения!
# marks_data = [
#     ('5', lesson_id, 4264)
#     for lesson_id in lessons_ids
# ]
#
# cursor.executemany('''
#     INSERT INTO marks(value, lesson_id, student_id)
#     VALUES(%s, %s, %s)''', marks_data)
# db.commit()

cursor.execute('''
    SELECT value FROM marks
    WHERE student_id = %s''', (4264,))
result_marks = cursor.fetchall()
print(result_marks)

cursor.execute('''
    SELECT title FROM books
    WHERE taken_by_student_id = %s''', (4264,))
result_books = cursor.fetchall()
print(result_books)

cursor.execute('''
    SELECT * FROM students st
    JOIN `groups` g ON st.group_id = g.id
    JOIN books b ON st.id = b.taken_by_student_id
    JOIN marks m ON st.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjets sub ON l.subject_id = sub.id
    WHERE st.id = %s''', (4264,))
result_join = cursor.fetchall()
print(result_join)

db.close()
