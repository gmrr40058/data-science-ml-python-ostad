-- Select all from grandfather table
SELECT * FROM grandfather;

-- Select all from father table
SELECT * FROM father;

-- Select specific columns from grandfather_siblings
SELECT name AS relative_name, gender AS relationship, spouse_name, wealth
FROM grandfather_siblings;

-- Select specific columns from father_gifts
SELECT gift_description AS gift_type, estimated_value AS gift_value, year AS gift_year
FROM father_gifts;


-- Grandfather's siblings who are brothers
SELECT name AS relative_name, wealth
FROM grandfather_siblings
WHERE gender = 'Male';

-- Gifts valued more than 500
SELECT gift_description AS gift_type, estimated_value AS gift_value, year AS gift_year
FROM father_gifts
WHERE estimated_value > 500;

-- Grandfather who is alive
SELECT name, birth_date
FROM grandfather
WHERE alive = TRUE;

-- Order grandfather's siblings by wealth descending
SELECT name AS relative_name, wealth
FROM grandfather_siblings
ORDER BY wealth DESC;

-- List gifts ordered by value
SELECT gift_description AS gift_type, estimated_value AS gift_value
FROM father_gifts
ORDER BY estimated_value DESC;

-- Total gift value received per year
SELECT year AS gift_year, SUM(estimated_value) AS total_gift_value
FROM father_gifts
GROUP BY year;

-- Average wealth by gender (interpreted as relationship)
SELECT gender AS relationship, AVG(wealth) AS avg_wealth
FROM grandfather_siblings
GROUP BY gender;

-- Average wealth by gender where it's less than 1000
SELECT gender AS relationship, AVG(wealth) AS avg_wealth
FROM grandfather_siblings
GROUP BY gender
HAVING avg_wealth < 10000000;

-- Years where total gift value exceeded 1000
SELECT year AS gift_year, SUM(estimated_value) AS total_gift_value
FROM father_gifts
GROUP BY year
HAVING total_gift_value > 1000;


-- Limit to first 5 gifts
SELECT gift_description AS gift_type, estimated_value AS gift_value
FROM father_gifts
LIMIT 5;

-- Count of brothers among grandfather's siblings
SELECT COUNT(*) AS total_brothers
FROM grandfather_siblings
WHERE gender = 'Male';

-- Distinct gift types received
SELECT DISTINCT gift_description AS gift_type
FROM father_gifts;

-- Distinct genders (relationships) among grandfather's siblings
SELECT DISTINCT gender AS relationship
FROM grandfather_siblings;

-- Join father and father_gifts to show gifts received by father
SELECT father.name, father_gifts.gift_description AS gift_type, father_gifts.estimated_value AS gift_value
FROM father
LEFT JOIN father_gifts
ON father.id = father_gifts.father_id;

-- Join grandfather and grandfather_siblings to show all his relatives
SELECT grandfather.name AS grandfather_name, grandfather_siblings.name AS relative_name, grandfather_siblings.gender AS relationship
FROM grandfather
LEFT JOIN grandfather_siblings
ON grandfather.id = grandfather_siblings.grandparent_id;


-- List all sisters who are married (assuming spouse_name is not null)
SELECT name AS relative_name
FROM grandfather_siblings
WHERE gender = 'Female' AND spouse_name IS NOT NULL;

-- Show father's wealth (only latest data available in one row)
SELECT name, wealth
FROM father;

-- Count how many different gift types were received
SELECT COUNT(DISTINCT gift_description) AS unique_gift_types
FROM father_gifts;



