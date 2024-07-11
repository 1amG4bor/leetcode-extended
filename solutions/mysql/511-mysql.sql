--511). Game Play Analysis I.

--Create Tables with data
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
Truncate table Activity
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5')
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6')
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5')

--Write a solution to find the first login date for each player.
--Expected output:
--  +-----------+-------------+
--  | player_id | first_login |
--  +-----------+-------------+
--  | 1         | 2016-03-01  |
--  | 2         | 2017-06-25  |
--  | 3         | 2016-03-02  |
--  +-----------+-------------+

--Solution
SELECT  player_id, MIN(event_date) as first_login FROM Activity
    GROUP BY player_id ORDER BY event_date