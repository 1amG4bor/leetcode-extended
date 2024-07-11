--181. Combine two tables
--  Problem description: https://leetcode.com/problems/combine-two-tables/description/

--Create Tables with data
Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int)
Truncate table Employee
insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3')
insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4')
insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', 'None')
insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', 'None')

--Write a solution to find the employees who earn more than their managers.
--Expected output:
--  +----------+
--  | Employee |
--  +----------+
--  | Joe      |
--  +----------+

--Solution
SELECT E1.name AS "Employee" FROM Employee E1 LEFT JOIN Employee E2 ON E2.id = E1.managerId WHERE E1.salary > E2.salary