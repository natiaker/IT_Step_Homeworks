create table customers(
	CustomerID serial primary key not null,
	FullName varchar(40),
	Email varchar(40),
	Phone varchar(15)	
);

create table sales(
	SaleID serial primary key not null,
	CustomerID int,
	ProductName varchar(25),
	Quantity float,
	UnitPrice float,
	SaleDate timestamp
);

alter table sales add constraint customerIdFKey foreign key (CustomerID) references customers (CustomerID)

insert into customers(FullName, Email, Phone) values 
('David Hill', 'david.hill@gmail.com', '781-461-5815'),
('Mary Scott', 'mary.scott@gmail.com', '972-654-1743'),
('Amy Johnson', 'amy.johnson@gmail.com', '310-505-2691'),
('Susan Clarke', 'susan.clarke@gmail.com', '832-238-3455'),
('Eric Martin', 'eric.martin@gmail.com', '607-272-6799'),
('Barbara Cooper', 'barbara.cooper@gmail.com', '360-809-4415');

insert into sales(CustomerID, ProductName, Quantity, UnitPrice) values
(1, 'Apple', 50, 3.5),
(2, 'Banana', 25, 5),
(3, 'Orange', 40, 4.50),
(2, 'Kiwi', 40, 4.50),
(8, 'grapes', 50, 8.09),
(6, 'Banana', 20, 12.30);

create or replace function set_sale_date()
returns trigger AS $$
	begin
		NEW.SaleDate = NOW();
		return NEW;
	end;
	$$ language plpgsql;
	
	
create trigger set_sale_date_trigger
before insert on sales
for each row
execute function set_sale_date();

select sum(Quantity*UnitPrice) as TotalRevenue from sales;
select avg(Quantity) as AvarageSales from sales;

select FullName, ProductName, Quantity, UnitPrice from sales
left join customers on sales.CustomerID = customers.CustomerID;

select FullName, ProductName, Quantity, UnitPrice from sales 
right join customers on sales.CustomerID = customers.CustomerID where sales.customerID is null;

select ProductName, sum(Quantity) as TotalQuantuty from sales
group by ProductName;

select FullName, SUM(Quantity * UnitPrice) AS TotalSales
from customers
inner join sales on customers.CustomerID = sales.CustomerID
group by FullName;
