--584). Find Customer Referee

--Create Tables with data
Create table If Not Exists Customer (id int, name varchar(25), referee_id int)
Truncate table Customer
insert into Customer (id, name, referee_id) values ('1', 'Will', 'None')
insert into Customer (id, name, referee_id) values ('2', 'Jane', 'None')
insert into Customer (id, name, referee_id) values ('3', 'Alex', '2')
insert into Customer (id, name, referee_id) values ('4', 'Bill', 'None')
insert into Customer (id, name, referee_id) values ('5', 'Zack', '1')
insert into Customer (id, name, referee_id) values ('6', 'Mark', '2')

--Find the names of the customer that are not referred by the customer with id = 2.
--Expected output:
--  +------+
--  | name |
--  +------+
--  | Will |
--  | Jane |
--  | Bill |
--  | Zack |
--  +------+

--Solution
SELECT name FROM Customer WHERE referee_id IS NULL OR referee_id != 2
