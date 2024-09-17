from app import db, Student
student_john = Student(firstname='john', lastname='doe',
                       email='jd@example.com', age=23,
                       bio='Biology student')
print(student_john.id)# student_john.firstname
# student_john.bio
db.session.add(student_john)
db.session.commit()
print(student_john.id) # 1



student_john.email = 'john_doe@example.com'
db.session.add(student_john)
db.session.commit()


sammy = Student(firstname='Sammy',
               lastname='Shark',
               email='sammyshark@example.com',
               age=20,
               bio='Marine biology student')

carl = Student(firstname='Carl',
               lastname='White',
               email='carlwhite@example.com',
               age=22,
               bio='Marine geology student')

db.session.add(sammy)
db.session.add(carl)
db.session.commit()

Student.query.all()