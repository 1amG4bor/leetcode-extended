--586). Customer Placing the Largest Number of Orders

--Create Tables with data
Create table If Not Exists orders (order_number int, customer_number int)
Truncate table orders
insert into orders (order_number, customer_number) values ('1', '1')
insert into orders (order_number, customer_number) values ('2', '2')
insert into orders (order_number, customer_number) values ('3', '3')
insert into orders (order_number, customer_number) values ('4', '3')


--Write a solution to
--Expected output:
--  +-----------------+
--  | customer_number |
--  +-----------------+
--  | 3               |
--  +-----------------+

--Solution
SELECT customer_number FROM Orders
    GROUP BY customer_number
    ORDER BY count(*) DESC
    LIMIT 1