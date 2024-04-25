import psycopg2

HOST = 'localhost'
PORT = 5432
DATABASE = 'company'
USER = 'postgres'
PASSWORD = 'nat2nat'

conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)

cursor = conn.cursor()

create_departments_table = """
    CREATE TABLE IF NOT EXISTS departments(
    departmentid SERIAL PRIMARY KEY,
    departmentname varchar(30)
    )"""

create_employees_table = """
    CREATE TABLE IF NOT EXISTS employees(
    employeeid SERIAL PRIMARY KEY,
    fullname varchar(40),
    hiredate timestamp(0) default current_timestamp,
    departmentid integer references departments(departmentid)
    ) """

cursor.execute(create_departments_table)
cursor.execute(create_employees_table)

insert_departments = "INSERT INTO departments (departmentname) VALUES ('Sales'), ('Marketing'), ('Finance'), ('IT')"
insert_employees = ("INSERT INTO employees (fullname, departmentid) VALUES ('John Doe', 1), ('Jane Smith', 1), "
                    "('Michael Johnson', 2), ('Emily Wilson', 3), ('Robert Smith', 4), ('Jackson Davis', 3)")

cursor.execute(insert_departments)
cursor.execute(insert_employees)

select_query = "SELECT employeeid, fullname, departmentname, hiredate FROM departments inner join employees on departments.departmentid = employees.departmentid"
cursor.execute(select_query)
result = cursor.fetchall()

for employee in result:
    print(employee)

conn.commit()

cursor.close()
conn.close()
