--196). Delete Duplicate Emails

--Create Tables with data
Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'john@example.com')
insert into Person (id, email) values ('2', 'bob@example.com')
insert into Person (id, email) values ('3', 'john@example.com')

--Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
--Expected output:
--  +----+------------------+
--  | id | email            |
--  +----+------------------+
--  | 1  | john@example.com |
--  | 2  | bob@example.com  |
--  +----+------------------+

--Solution
DELETE P FROM Person P
    INNER JOIN (
        SELECT distinct
            FIRST_VALUE(id) over(partition by email order by id) as first,
            email
        FROM Person) Firsts

    ON P.email = Firsts.email
    WHERE P.email = Firsts.email AND P.id != Firsts.first