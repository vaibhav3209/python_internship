-- question1 : how many users?
	select count(distinct user_id)           -- unique nikalna padega as primary key nhi hai user_id
	from users; 

-- question2 : how many cookies does each user have on average
	select user_id,count(cookie_id)             -- yha par distinct na lagega as PRIMARY KEY HAI 
	from users 
	group by user_id;

--  question3 :unique num, of visits by all users per month
	select month(event_time)as month_num,count(distinct visit_id) as "visits"
	from events 
	group by month_num  ;                           -- alias ko yha likh sakte...???

--  question4 :no. of eveents for each event type
	select event_type,count(event_type)
	from events
	group by event_type;

-- question 5:percentage of visits which have a purchase event???
-- alag har event ka percentage calca
select 
(

	(
		select count(visit_id) as "visits of purchase event" 
		from events e
		join event_identifier ev using (event_type)
		 where event_name = "Add to Cart"        -- use this for single event
        
	) 
	/               -- divide kardo 
(select count(visit_id) from events)*(100)
	) as "percentage";
    
    
    
-- method2 for question 5 :easy  and also work for 	
-- AND
 -- QUESTION 6 -- add to cart required
		select ev.event_type,ev.event_name,per.percent_event from (
			select e.event_type ,(count(visit_id)/(select count(visit_id) as total_visits from events))*100 as percent_event
			from events e 
			group by event_type 
		) as per
		right join event_identifier ev using (event_type);
-- ......................................................


-- question 7 : mosst viewwd pages
select ev.page_id,ph.page_name,count(ev.visit_id) as max_visits
from events ev

join page_hierarchy ph using (page_id)

group by ev.page_id,ph.page_name

having max_visits = (
select  max(page_visits)
from (
			select e.page_id,count(e.visit_id) as page_visits 
			from events e 
			group by e.page_id
	) as x
					);
                    

-- question8 :  view and add to cart for each product category

-- use this refernece table below
		select page_id,page_name,product_category,event_type, event_name
		from events 
		join event_identifier ev using (event_type)
		join page_hierarchy ph using (page_id)
		order by page_id,event_type;
  
  
  -- SOLUTION 
	select product_category,event_name,count(event_name) 
	from events 
	join event_identifier ev using (event_type)
		join page_hierarchy ph using (page_id)
	group by product_category , event_name
    
-- .................................