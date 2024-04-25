create table employees(
	employeeID serial primary key not null,
	FirstName varchar(20),
	LastName varchar(30),
	IDNumber varchar(15),
	DepartmentID integer,
	CityID integer,
	BankID integer
)

create table cities(
	CityID serial primary key not null,
	CityName varchar(30)
)

create table departments(
	DepartmentID serial primary key not null,
	DepartmentName varchar(30)
)

create table banks(
	BankID serial primary key not null,
	BankAbbreviation varchar(15),
	BankName varchar(40)
)


alter table employees add constraint UniqueIDNumber unique (IDNumber)
alter table employees add constraint DepartmentIDFKey foreign key (DepartmentID) references departments (DepartmentID)
alter table employees add constraint CityIDFKey foreign key (CityID) references cities (CityID)
alter table employees add constraint BankIDFKey foreign key (BankID) references banks (BankID)


insert into departments (DepartmentName) values ('IT'), ('Finances'), ('Sales'), ('Marketing'), ('HR') 
insert into cities (CityName) values ('Tbilisi'), ('Batumi'), ('Qutaisi'), ('Telavi'), ('Zugdidi')
insert into banks (BankAbbreviation, BankName) values 
('TBC', 'TBC Bank'), 
('BOG', 'Bank Of Georgia'), 
('Halyk', 'Halyk Bank'), 
('MBC', 'Micro Business Capital'), 
('Rico', 'Rico Credit')
insert into employees (FirstName, LastName, IDNumber, DepartmentID, CityID, BankID) values
('John', 'Doe', '12345678', 1, 1, 1),
('Bob', 'Bobson', '87654321', 2, 2, 2),
('James', 'Johnson', '12121212', 3, 3, 3),
('Jason', 'Smith', '32323232', 4, 4, 4),
('Tom', 'Martin', '54321234', 5, 5, 5)


select EmployeeID, FirstName, LastName, IDNumber, DepartmentName, CityName, BankAbbreviation, BankName
from employees
inner join departments on employees.DepartmentID = departments.DepartmentID
inner join cities on employees.CityID = cities.CityID
inner join banks on employees.BankID = banks.BankID


