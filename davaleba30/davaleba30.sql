
create table Deposit (DepositID serial primary key not null, DepOwnerName varchar(20), DateOfBirth date,
					  City varchar(20), StreetName varchar(30), DepositAmount numeric(10, 2), Interest numeric(5, 2), 
					  Comission numeric(5, 2), Total numeric(10, 2))
					  
					
insert into deposit(DepOwnerName, DateOfBirth, City, StreetName) values('John', '1993-10-23', 'Tbilisi', 'Nutsubidze str.'), 
('Mary', '1997-11-02', 'Tbilisi', 'Rustaveli str.'), ('David', '2000-12-13', 'Batumi', 'Gorgasali str.')

select * from deposit

insert into deposit(DepOwnerName, DateOfBirth, DepositAmount, Comission, Total) values('Giorgi', '1989-03-14', 2501, 1, 2500),
('Natia', '1998-06-02', 2005, 2, 2003), ('Nino', '1997-03-20', 2300, 2, 2298), ('Eka', '1973-09-19', 950, 1.5, 948.5),
('Nodari', '1960-07-28', 1000, 1.5, 998.5)

select * from deposit where DepositAmount > 1500
select * from deposit where City = 'Tbilisi' and StreetName = 'Rustaveli str.'
select * from deposit where City = 'Batumi' and StreetName = 'Gorgasali str.' and DepositAmount between 1000 and 2000
select * from deposit where DepOwnerName like 'D%'

truncate deposit

drop table deposit