from model import session, Departments, Employees

joined_query = session.query(Employees, Departments).join(Departments, Employees.departmentid == Departments.departmentid)

for employee, department in joined_query:
    print(employee.employeeid, employee.fullname, department.departmentname, employee.hiredate)


# joined_query = session.query(Employees.departmentid, Employees.fullname, Departments.departmentname, Employees.hiredate).join(Departments).all()
#
# for employee in joined_query:
#     print(employee)
