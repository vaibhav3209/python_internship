-- question1>)
-- TOTAL AMOUNT SPENT BY CUSTOMER
		select s.customer_id,sum(price) as "Total amount spent" from dannys_diner.sales s
		join dannys_diner.menu using (product_id)
		group by s.customer_id;

-- question 2.. NO. OF DAYS CUSTOMER VISITED
		select s.customer_id,COUNT(s.order_date) as "Days visited" 
		from dannys_diner.sales s
		group by s.customer_id;

-- question3 ..
-- first product ordered

--  select * from 
--  -- sales
--  -- where
-- --  customer_id in 
--  (
--  select distinct customer_id
--  from sales) as v;
 
 -- question4....
		select product_id 
        from sales 
        where product_id = (
			select max()
 
 -- question 10..
 -- assumption,,,,assuming a memeber customer,,,
 -- date <janunary 31,,,,$1 pe 20 points for 1st week ,,,baad mein 10 points
 
			select customer_id,sum(points)
			from(
			 select s.customer_id,s.product_id,s.order_date,mb.join_date,
					( case
					when order_date between join_date and date_add(join_date ,INTERVAL 7 day)
					then (price*20) 
					else (price*10)
					end 
					) as "points"
			 from sales s
			 join menu m using (product_id)
			 join members mb using (customer_id)            -- to see if a customer is member
			order by customer_id
			) as c
			where order_date < "2021-01-31"
			group by customer_id
			order by customer_id;

-- this is original joined table could crreate a view
			select * 
			from sales s
			 join menu m using (product_id)
			 join members mb using (customer_id)            -- to see if a customer is member
			order by customer_id