# v_art database
use v_art;
# 1. When you visit the Virtual Art Gallery and you search by Period/Style
# and you choose Impressionism, you get two resulting images ("Woman in the Garden" and "Irises").
# What query would be used in the code here to allow the user to see these images? No join is needed. 

select artfile from artwork
where period = 'Impressionism';

# 2. When you visit the Virtual Art Gallery, search by Subject and type in the word flower, you get three images.
# What query would have allowed the user to get those results (remember, the keyword might have been 'flowers' but they typed 'flower') .

select artfile
from artwork
	join artwork_keyword
    on artwork.artwork_id = artwork_keyword.artwork_id
    join keyword
    on artwork_keyword.keyword_id = keyword.keyword_id
    where keyword = 'flowers';

# 3. List all the artists from the artist table, but only the related artwork
# from the artwork table. We need the first name, last name, and artwork title. 

select fname, lname, title
from artist
	join artwork
    on artist.artist_id = artwork.artist_id;
    
# Magazine Database:
select * from subscription;
# 4. List all subscriptions with the magazine name, last name, first name, and sort alphabetically by magazine name. 
use magazine;
select magazineName, subscriberLastName, subscriberFirstName
from magazine
	join subscription
    on magazine.magazineKey = subscription.magazinekey
    join subscriber
    on subscription.subscriberkey = subscriber.subscriberkey
    order by magazineName;
    
# 5.  List all the magazines that Samantha Sanders subscribes to. 
select magazineName
from magazine
	join subscription
    on magazine.magazineKey = subscription.magazinekey
    join subscriber
    on subscription.subscriberkey = subscriber.subscriberkey
    where subscriberFirstName = 'Samantha';
    
# Employee Database:
# 6. List the first five employees from the Customer Service Department.
# Put them in alphabetical order by last name.
use employees;
select first_name, last_name
from employees
	join dept_emp
    on employees.emp_no = dept_emp.emp_no
    join departments
    on dept_emp.dept_no = departments.dept_no
    where dept_name = 'Customer Service'
    order by last_name
    limit 5;
    
# 7. Find out the current salary and department of Berni Genin.
# You can use the ORDER BY and LIMIT to get just the most recent salary.
select first_name, last_name, dept_name, salary
from employees
	join dept_emp
    on employees.emp_no = dept_emp.emp_no
    join salaries 
    on dept_emp.emp_no = salaries.emp_no
    join departments
    on dept_emp.dept_no = departments.dept_no
    where last_name = 'Genin' and first_name = 'Berni'
    order by salary desc
    limit 1;


