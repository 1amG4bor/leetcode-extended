--577). Employee Bonus

--Create Tables with data
Create table If Not Exists Employee (empId int, name varchar(255), supervisor int, salary int)
Create table If Not Exists Bonus (empId int, bonus int)
Truncate table Employee
insert into Employee (empId, name, supervisor, salary) values ('3', 'Brad', 'None', '4000')
insert into Employee (empId, name, supervisor, salary) values ('1', 'John', '3', '1000')
insert into Employee (empId, name, supervisor, salary) values ('2', 'Dan', '3', '2000')
insert into Employee (empId, name, supervisor, salary) values ('4', 'Thomas', '3', '4000')
Truncate table Bonus
insert into Bonus (empId, bonus) values ('2', '500')
insert into Bonus (empId, bonus) values ('4', '2000')

--Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.
--Expected output:
--  +------+-------+
--  | name | bonus |
--  +------+-------+
--  | Brad | null  |
--  | John | null  |
--  | Dan  | 500   |
--  +------+-------+

--Solution
SELECT name, bonus FROM Employee E
    LEFT JOIN Bonus B ON E.empId = B.empId
    WHERE bonus is NULL OR bonus < 1000