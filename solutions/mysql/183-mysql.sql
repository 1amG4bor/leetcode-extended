--183). Customers Who Never Order
--  Problem description: https://leetcode.com/problems/customers-who-never-order/description/

--Create Tables with data
Create table If Not Exists Customers (id int, name varchar(255))
Create table If Not Exists Orders (id int, customerId int)
Truncate table Customers
insert into Customers (id, name) values ('1', 'Joe')
insert into Customers (id, name) values ('2', 'Henry')
insert into Customers (id, name) values ('3', 'Sam')
insert into Customers (id, name) values ('4', 'Max')
Truncate table Orders
insert into Orders (id, customerId) values ('1', '3')
insert into Orders (id, customerId) values ('2', '1')

--Write a solution to find all customers who never order anything.
--Expected output:
--  +-----------+
--  | Customers |
--  +-----------+
--  | Henry     |
--  | Max       |
--  +-----------+

--Solution
SELECT C.name as Customers FROM Customers C LEFT JOIN Orders O ON C.id = O.customerId WHERE O.id IS NULL