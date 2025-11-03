import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Student (
    RollNo INTEGER PRIMARY KEY,
    Name TEXT,
    Marks INTEGER,
    Aadhar TEXT UNIQUE,
    Address TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Course (
    RollNo INTEGER,
    Course TEXT,
    Course_Duration TEXT,
    FOREIGN KEY (RollNo) REFERENCES Student(RollNo)
)
''')

cursor.executemany('''
INSERT OR IGNORE INTO Student (RollNo, Name, Marks, Aadhar, Address)
VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Rohit', 45, '123456789012', 'Delhi'),
    (2, 'Rajesh', 29, '123456789013', 'Mumbai'),
    (3, 'Aman', 55, '123456789014', 'Pune'),
    (4, 'Rahul', 20, '123456789015', 'Kolkata'),
    (5, 'Ravi', 70, '123456789016', 'Chennai')
])

cursor.executemany('''
INSERT OR IGNORE INTO Course (RollNo, Course, Course_Duration)
VALUES (?, ?, ?)
''', [
    (1, 'BCA', '3 years'),
    (2, 'BBA', '3 years'),
    (3, 'BCA', '3 years'),
    (4, 'BCom', '3 years'),
    (5, 'BCA', '3 years')
])

conn.commit()

cursor.execute('SELECT AVG(Marks) FROM Student')
average_marks = cursor.fetchone()[0]
print(f"Average marks: {average_marks}")

cursor.execute('SELECT Name FROM Student ORDER BY Name ASC')
names = cursor.fetchall()
print("Names in ascending order:")
for name in names:
    print(name[0])

cursor.execute('SELECT RollNo, Name FROM Student WHERE Marks < 30')
students_below_30 = cursor.fetchall()
print("Students scoring below 30:")
for student in students_below_30:
    print(f"RollNo: {student[0]}, Name: {student[1]}")

cursor.execute("SELECT RollNo, Name FROM Student WHERE Name LIKE 'R%'")
students_with_r = cursor.fetchall()
print("Students whose names start with 'R':")
for student in students_with_r:
    print(f"RollNo: {student[0]}, Name: {student[1]}")

cursor.execute("SELECT RollNo FROM Course WHERE Course = 'BCA'")
bca_students = cursor.fetchall()
print("Students pursuing BCA:")
for student in bca_students:
    print(f"RollNo: {student[0]}")

conn.close()
