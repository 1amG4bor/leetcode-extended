--176). Second Highest Salary
--  Problem description> https://leetcode.com/problems/second-highest-salary/description/

--Create Tables with data
Create table If Not Exists Employee (id int, salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')
-- Test2
insert into Employee (id, salary) values ('1', '100')
-- Test3
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '100')
-- Test4
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')

--Write a solution to find the second highest salary from the Employee table.
--  If there is no second highest salary, return null.
--Expected output (Test1):
--  +---------------------+
--  | SecondHighestSalary |
--  +---------------------+
--  | 200                 |
--  +---------------------+
-- Expected output for Test2:   null
-- Expected output for Test3:   null
-- Expected output for Test4:   100

--Solution
SELECT NTH_VALUE(salary, 2) OVER() AS SecondHighestSalary
    FROM (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC) inner_query
    LIMIT 1