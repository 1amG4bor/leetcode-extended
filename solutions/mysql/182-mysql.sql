--182). Duplicate Emails
--  Problem description: https://leetcode.com/problems/duplicate-emails/description/

--Create Tables with data
Create table If Not Exists Person (id int, email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'a@b.com')
insert into Person (id, email) values ('2', 'c@d.com')
insert into Person (id, email) values ('3', 'a@b.com')

--Write a solution to report all the duplicate emails.
--  Note that it's guaranteed that the email field is not NULL.
--Expected output:
--  +---------+
--  | Email   |
--  +---------+
--  | a@b.com |
--  +---------+

--Solution
SELECT email FROM Person GROUP BY email HAVING COUNT(*) > 1;