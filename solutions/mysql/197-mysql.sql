--197). Rising Temperature

--Create Tables with data
Create table If Not Exists Weather (id int, recordDate date, temperature int)
Truncate table Weather
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10')
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25')
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20')
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30')

--Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
--Expected output:
--  +----+
--  | id |
--  +----+
--  | 2  |
--  | 4  |
--  +----+

--Solution
SELECT id AS Id FROM (
    SELECT id,
        temperature,
        DATE_ADD(recordDate, INTERVAL -1 DAY) AS prev_day,
        LAG(recordDate) OVER(ORDER BY recordDate) as prev_temp_day,
        LAG(temperature) OVER(ORDER BY recordDate) as prev_temp
    FROM Weather) W
    WHERE W.prev_day = W.prev_temp_day AND W.temperature > W.prev_temp