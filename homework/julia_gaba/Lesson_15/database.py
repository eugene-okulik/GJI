import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# 1. Добавляем студента
cursor.execute('''
    INSERT INTO students (name, second_name)
    VALUES (%s, %s)''', ('Elizabet', 'White'))
my_student = cursor.lastrowid
db.commit()

# 2. Добавляем книги и вешаем книги на студента
books_data = [
    ('Думай медленно, решай быстро', my_student),
    ('Грокаем алгоритмы 2', my_student),
    ('Наш любимый Python', my_student)
]

cursor.executemany('''
    INSERT INTO books (title, taken_by_student_id)
    VALUES(%s, %s)''', books_data)
db.commit()

# 3. Добавляем группу и определяем туда моего студента
cursor.execute('''
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES (%s, %s, %s)''', ('Desperate Housewives', 'Dec 2024', 'April 2025'))
my_group = cursor.lastrowid
db.commit()

cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s", (my_group, my_student))
db.commit()

# 4. Добавляем предметы
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

# 5. Добавляем по 2 урока к каждому предмету
lessons_data = [
    ('Вокал lesson 1', sub1),
    ('Вокал lesson 2', sub1),
    ('Барабаны lesson 1', sub2),
    ('Барабаны lesson 2', sub2),
    ('Гитара lesson 1', sub3),
    ('Гитара lesson 2', sub3)
]

cursor.execute('''
    INSERT INTO lessons (title, subject_id)
    VALUES(%s, %s)''', lessons_data[0])
les1 = cursor.lastrowid

cursor.execute('''
    INSERT INTO lessons (title, subject_id)
    VALUES(%s, %s)''', lessons_data[1])
les2 = cursor.lastrowid

cursor.execute('''
    INSERT INTO lessons (title, subject_id)
    VALUES(%s, %s)''', lessons_data[2])
les3 = cursor.lastrowid

cursor.execute('''
    INSERT INTO lessons (title, subject_id)
    VALUES(%s, %s)''', lessons_data[3])
les4 = cursor.lastrowid

cursor.execute('''
    INSERT INTO lessons (title, subject_id)
    VALUES(%s, %s)''', lessons_data[4])
les5 = cursor.lastrowid

cursor.execute('''
    INSERT INTO lessons (title, subject_id)
    VALUES(%s, %s)''', lessons_data[5])
les6 = cursor.lastrowid
db.commit()

# 6. Добавляем оценки по каждому уроку
marks_data = [
    ('5', les1, my_student),
    ('5', les2, my_student),
    ('4', les3, my_student),
    ('5', les4, my_student),
    ('5', les5, my_student),
    ('5', les6, my_student)
]

cursor.executemany('''
    INSERT INTO marks(value, lesson_id, student_id)
    VALUES(%s, %s, %s)''', marks_data)
db.commit()

# Все оценки студента
cursor.execute('''
    SELECT value FROM marks
    WHERE student_id = %s''', (my_student,))
result_marks = cursor.fetchall()
print(result_marks)

# Все книги, которые находятся у студента
cursor.execute('''
    SELECT title FROM books
    WHERE taken_by_student_id = %s''', (my_student,))
result_books = cursor.fetchall()
print(result_books)

# Всё, что есть в базе о моем студенте
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
