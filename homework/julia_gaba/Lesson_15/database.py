import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)


# Добавляем студента
cursor.execute('''
    INSERT INTO students (name, second_name)
    VALUES (%s, %s)''', ('Bett', 'Right'))
my_student = cursor.lastrowid
db.commit()
print(my_student)

# Получаем моего студента
cursor.execute("SELECT * FROM students WHERE id = %s", (my_student,))
print(cursor.fetchone())

# Добавляем группу
cursor.execute('''
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES (%s, %s, %s)''',('Desperate Housewives', 'Dec 2024', 'Dec 2025'))
my_group = cursor.lastrowid
db.commit()
print(my_group)

# Получаем группу
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (my_group,))
print(cursor.fetchone())

# Обновляем группу студента
cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s", (my_group, my_student))
db.commit()

# Добавляем книги
books_data = [
    ('Думай медленно, решай быстро', my_student),
    ('Грокаем алгоритмы 2', my_student),
    ('Наш любимый Python', my_student)
]
cursor.executemany('''
    INSERT INTO books (title, taken_by_student_id)
    VALUES(%s, %s)''',
                   books_data)
db.commit()


# Добавляем предметы
subjects_data = [
    ('Вокал',),
    ('Барабаны',),
    ('Гитара',)
]

cursor.execute('''
    INSERT INTO subjets (title)
    VALUES(%s)''', subjects_data[0])
sub1 = cursor.lastrowid

cursor.execute('''
    INSERT INTO subjets (title)
    VALUES(%s)''', subjects_data[1])
sub2 = cursor.lastrowid

cursor.execute('''
    INSERT INTO subjets (title)
    VALUES(%s)''', subjects_data[2])
sub3 = cursor.lastrowid

db.commit()

# Получаем ID предметов
cursor.execute("SELECT id FROM subjets "
               "WHERE id = %s", (sub1,))
print(cursor.fetchone())
cursor.execute("SELECT id FROM subjets "
               "WHERE id = %s", (sub2,))
print(cursor.fetchone())
cursor.execute("SELECT id FROM subjets "
               "WHERE id = %s", (sub3,))
print(cursor.fetchone())


# Добавляем уроки
lessons_data = [
    ('Вокал lesson 1', sub1),
    ('Вокал lesson 2', sub1),
    ('Барабаны lesson 1', sub2),
    ('Барабаны lesson 2', sub2),
    ('Гитара lesson 1', sub3),
    ('Гитара lesson 2', sub3)
]
cursor.executemany('''
    INSERT INTO lessons (title, subject_id)
    VALUES(%s, %s)''',
                   lessons_data)
db.commit()
lessons_first_id = cursor.lastrowid

lessons_ids = list(range(lessons_first_id,
                         lessons_first_id + len(lessons_data)))
print(lessons_ids)


# Получаем ID уроков
cursor.execute("SELECT * FROM lessons WHERE id BETWEEN %s AND %s",
               (lessons_ids[0], lessons_ids[5]))

print(cursor.fetchall())


# Добавляем оценки
marks_data = [
    ('5', lesson_id, my_student)
    for lesson_id in lessons_ids
]

cursor.executemany('''
    INSERT INTO marks(value, lesson_id, student_id)
    VALUES(%s, %s, %s)''', marks_data)
db.commit()

cursor.execute('''
    SELECT value FROM marks
    WHERE student_id = %s''', (my_student,))
result_marks = cursor.fetchall()
print(result_marks)

cursor.execute('''
    SELECT title FROM books
    WHERE taken_by_student_id = %s''', (my_student,))
result_books = cursor.fetchall()
print(result_books)

cursor.execute('''
    SELECT * FROM students st
    JOIN `groups` g ON st.group_id = g.id
    JOIN books b ON st.id = b.taken_by_student_id
    JOIN marks m ON st.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjets sub ON l.subject_id = sub.id
    WHERE st.id = %s''', (my_student,))
result_join = cursor.fetchall()
print(result_join)

db.close()
