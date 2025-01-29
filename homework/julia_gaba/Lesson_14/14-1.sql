INSERT INTO students (name, second_name, group_id)
VALUES ('Masha', 'Retuzina', NULL)

INSERT INTO books (title, taken_by_student_id)
VALUES ('The fried green tomato', 3940), ('White and Black Bim', 3940), ('Python and Black Mamba', 3940)

INSERT INTO `groups` (title, start_date, end_date)
VALUES ('Swiss knife', 'dec 2024', 'march 2025')

UPDATE students SET group_id = 2493 WHERE id = 3940

INSERT INTO subjets (title)
VALUES ('Cooking'), ('Driving'), ('Surfing')

INSERT INTO lessons (title, subject_id)
VALUES 
('Cooking lesson 1', 3807), ('Cooking lesson 2', 3807), 
('Driving lesson 1', 3808), ('Driving lesson 2', 3808),
('Surfing lesson 1', 3809), ('Surfing lesson 2', 3809)

INSERT INTO marks (value, lesson_id, student_id)
VALUES 
('5', 7416, 3940), ('5', 7417, 3940),
('5', 7418, 3940), ('5', 7419, 3940),
('5', 7420, 3940), ('5', 7421, 3940)

SELECT value FROM marks
WHERE student_id = 3940

SELECT title FROM books
WHERE taken_by_student_id = 3940 

SELECT * FROM students st 
JOIN `groups` g ON st.group_id = g.id
JOIN books b ON st.id = b.taken_by_student_id
JOIN subjets sub ON sub.id = l.subject_id
JOIN lessons l ON l.subject_id = sub.id
JOIN marks m ON st.id = m.student_id