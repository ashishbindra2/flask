from datetime import date
from app import db, Employee

db.drop_all()
db.create_all()

e1 = Employee(firstname='John',
              lastname='Doe',
              email='jd@example.com',
              age=32,
              hire_date=date(2012, 3, 3),
              active=True
              )

e2 = Employee(firstname='Mary',
              lastname='Doe',
              email='md@example.com',
              age=38,
              hire_date=date(2016, 6, 7),
              active=True
              )

e3 = Employee(firstname='Jane',
              lastname='Tanaka',
              email='jt@example.com',
              age=32,
              hire_date=date(2015, 9, 12),
              active=False
              )

e4 = Employee(firstname='Alex',
              lastname='Brown',
              email='ab@example.com',
              age=29,
              hire_date=date(2019, 1, 3),
              active=True
              )

e5 = Employee(firstname='James',
              lastname='White',
              email='jw@example.com',
              age=24,
              hire_date=date(2021, 2, 4),
              active=True
              )

e6 = Employee(firstname='Harold',
              lastname='Ishida',
              email='hi@example.com',
              age=52,
              hire_date=date(2002, 3, 6),
              active=False
              )

e7 = Employee(firstname='Scarlett',
              lastname='Winter',
              email='sw@example.com',
              age=22,
              hire_date=date(2021, 4, 7),
              active=True
              )

e8 = Employee(firstname='Emily',
              lastname='Vill',
              email='ev@example.com',
              age=27,
              hire_date=date(2019, 6, 9),
              active=True
              )

e9 = Employee(firstname='Mary',
              lastname='Park',
              email='mp@example.com',
              age=30,
              hire_date=date(2021, 8, 11),
              active=True
              )

db.session.add_all([e1, e2, e3, e4, e5, e6, e7, e8, e9])

db.session.commit()


# Retrieving the First Record

# Similarly, you can use the first() method to get the first record:

#     first_employee = Employee.query.first()
#     print(first_employee)

# Retrieving a Record by ID

# In most database tables, records are identified with a unique ID. Flask-SQLAlchemy allows you to fetch a record using its ID with the get() method:

employee5 = Employee.query.get(5)
employee3 = Employee.query.get(3)
print(f'{employee5} | ID: {employee5.id}')
print(f'{employee3} | ID: {employee3.id}')

# Retrieving a Record or Multiple Records by a Column Value

# To get a record using the value of one of its columns, use the filter_by() method. For example, to get a record using its ID value, similar to the get() method:

employee = Employee.query.filter_by(id=1).first()
print(employee)



