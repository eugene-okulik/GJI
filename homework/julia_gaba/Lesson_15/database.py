import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(buffered=True)

# 1. Добавляем студента
cursor.execute('''
    INSERT INTO students(name, second_name, group_id)
    VALUES('Misha', 'Rituzin', NULL)
''')
db.commit()

# Получаем ID студента
cursor.execute("SELECT id FROM students WHERE name = 'Misha' AND second_name = 'Rituzin'")
my_student_id = cursor.fetchone()[0]

# Добавляем группу
cursor.execute('''
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES('Desperate', 'Dec 2024', 'March 2025')
''')
db.commit()

# Получаем ID группы
cursor.execute("SELECT id FROM `groups` WHERE title = 'Desperate'")
my_group_id = cursor.fetchone()[0]

# Обновляем группу студента
cursor.execute(f'''
    UPDATE students SET group_id = {my_group_id} WHERE id = {my_student_id}
''')
db.commit()

# Добавляем книги
books_data = [
    ('Bim White and Black Ears', my_student_id),
    ('The fried red tomato', my_student_id),
    ('Python and Anaconda', my_student_id)
]
cursor.executemany('''
    INSERT INTO books(title, taken_by_student_id)
    VALUES(%s, %s)''',
    books_data)
db.commit()

# Добавляем предметы
subjects_data = [
    ('Thai boxing',),
    ('Running',),
    ('Kiting',)
]

cursor.executemany('''
    INSERT INTO subjets (title)
    VALUES(%s)''',
    subjects_data)
db.commit()

# Получаем ID предметов
cursor.execute("SELECT id FROM subjets WHERE title = 'Thai boxing'")
thai_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM subjets WHERE title = 'Running'")
running_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM subjets WHERE title = 'Kiting'")
kiting_id = cursor.fetchone()[0]

# Добавляем уроки
lessons_data = [
    ('Thai boxing lesson 1', thai_id),
    ('Thai boxing lesson 2', thai_id),
    ('Running lesson 1', running_id),
    ('Running lesson 2', running_id),
    ('Kiting lesson 1', kiting_id),
    ('Kiting lesson 2', kiting_id)
]
cursor.executemany('''
    INSERT INTO lessons(title, subject_id)
    VALUES(%s, %s)''',
    lessons_data)
db.commit()

# Получаем ID уроков
cursor.execute("SELECT id FROM lessons ORDER BY id DESC LIMIT 6")
lesson_ids = [row[0] for row in cursor.fetchall()]

# Добавляем оценки
marks_data = [
    ('5', lesson_ids[0], my_student_id),
    ('5', lesson_ids[1], my_student_id),
    ('5', lesson_ids[2], my_student_id),
    ('5', lesson_ids[3], my_student_id),
    ('5', lesson_ids[4], my_student_id),
    ('5', lesson_ids[5], my_student_id)
]

cursor.executemany('''
    INSERT INTO marks(value, lesson_id, student_id)
    VALUES(%s, %s, %s)''',
    marks_data)
db.commit()

cursor.execute('''
    SELECT value FROM marks
    WHERE student_id = %s''', (my_student_id,))
result_marks = cursor.fetchall()
print(result_marks)

cursor.execute('''
    SELECT title FROM books
    WHERE taken_by_student_id = %s''', (my_student_id,))
result_books = cursor.fetchall()
print(result_books)

cursor.execute('''
    SELECT * FROM students st
    JOIN `groups` g ON st.group_id = g.id
    JOIN books b ON st.id = b.taken_by_student_id
    JOIN marks m ON st.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id  
    JOIN subjets sub ON l.subject_id = sub.id  
    WHERE st.id = %s''', (my_student_id,))
result_join = cursor.fetchall()
print(result_join)

db.close()