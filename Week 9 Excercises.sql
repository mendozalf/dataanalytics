use v_art;

select fname, lname, title
from artwork 
	join artist
    on artwork.artist_id  = artist.artist_id
    where lname = 'da Vinci';
    
select * from artist;
select * from artwork;

use bike;

select * from category;

select * from product;

select product_name, category_name, brand_name, list_price
from product p
	join category c
    on p.category_id = c.category_id
    join brand b
    on p.brand_id = b.brand_id
where category_name = 'Children Bicycles';

select first_name, last_name, store.store_id
from staff 
	join store
	on staff.store_id = store.store_id
where staff.store_id = 3;

select * from brand;


use v_art;

select title
from artwork a
	join artwork_keyword ak
    on a.artwork_id = ak.artwork_id
    join keyword k
    on ak.keyword_id = k.keyword_id
where keyword = 'water';

use employees;

select first_name, last_name, dept_name, salary, s.from_date
from departments d
	join dept_emp de
    on d.dept_no = de.dept_no
    join employees e
    on e.emp_no = de.emp_no
    join salaries s
    on e.emp_no = s.emp_no
    where s.from_date > '2000-12-31';
    
use world;

select * from city;

select co.name, ci.name
from city ci
	join country co
    on code = countrycode;
    
use bike;

select last_name, product_name, order_date
from customer c
	join cust_order co
    on c.customer_id = co.customer_id
    join cust_order_item coi
    on co.cust_order_id = coi.cust_order_id
    join product p
    on coi.product_id = p.product_id
where last_name = 'Baldwin';