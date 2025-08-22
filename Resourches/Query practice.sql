select * from grandfather;

select * from father;

select name as Relative_Name, gender as relationship, spouse_name, wealth
from grandfather_siblings;

-- grandparents brother list
select name as relative_name, wealth
from grandfather_siblings
where gender="Male";


-- gifts more than 500
select gift_description, estimated_value, year
from father_gifts
where estimated_value<30000;

-- who is alive
select name, birth_date
from grandfather_siblings
where alive=True;


-- Who is richer
select name, wealth
from grandfather_siblings
order by wealth desc;


-- average wealth by gender where it's less than 170000
select gender, avg(wealth) as avg_wealth
from grandfather_siblings
group by gender
having avg_wealth < 200000;

-- total brother
select count(*) as total_brother
from grandfather_siblings
where gender="Male";


-- list all sisters who are married
select name
from grandfather_siblings
where gender="Female" and spouse_name is null;


select count(distinct gift_description) as unique_gift_types
from father_gifts;
