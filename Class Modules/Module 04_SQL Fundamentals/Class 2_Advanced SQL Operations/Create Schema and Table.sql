-- Create a new schema for family data
DROP SCHEMA IF EXISTS family_db;
CREATE SCHEMA family_db;
USE family_db;

-- Table for grandfather and his siblings
CREATE TABLE grandfather (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE,
    age INT,
    email VARCHAR(100),
    alive BOOLEAN,
    number_of_brothers INT,
    number_of_sisters INT,
    wealth DECIMAL(12,2),
    death_date DATE
);

-- Table for siblings of grandfather
CREATE TABLE grandfather_siblings (
    id INT PRIMARY KEY not null,
    grandparent_id INT,
    name VARCHAR(100),
    gender ENUM('Male', 'Female'),
    spouse_name VARCHAR(100),
    number_of_children INT,
    wealth DECIMAL(12,2),
    birth_date DATE,
    age INT,
    email VARCHAR(100),
    alive BOOLEAN,
    death_date DATE,
    FOREIGN KEY (grandparent_id) REFERENCES grandfather(id)
);

-- Table for father data
CREATE TABLE father (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE,
    age INT,
    number_of_brothers INT,
    number_of_sisters INT,
    wealth DECIMAL(12,2),
    email VARCHAR(100),
    alive BOOLEAN
);

-- Table for father's gift history
CREATE TABLE father_gifts (
    id INT PRIMARY KEY,
    father_id INT,
    year YEAR,
    gift_description VARCHAR(255),
    from_relative_name VARCHAR(100),
    estimated_value DECIMAL(10,2),
    FOREIGN KEY (father_id) REFERENCES father(id)
);

-- Insert data for grandfather
INSERT INTO grandfather VALUES
(1, 'Abdul Karim', '1930-02-15', 94, 'abdul.karim@example.com', FALSE, 7, 3, 1500000.00, '2024-03-01');

-- Insert data for grandfather's siblings
INSERT INTO grandfather_siblings VALUES
(101, 1, 'Habibur Rahman', 'Male', 'Ayesha Begum', 5, 200000.00, '1932-06-10', 92, 'habib.rahman@example.com', TRUE, NULL),
(102, 1, 'Jabed Ali', 'Male', 'Rokeya Khatun', 4, 180000.00, '1934-08-21', 90, 'jabed.ali@example.com', TRUE, NULL),
(103, 1, 'Nazma Khatun', 'Female', 'Salam Miah', 6, 170000.00, '1936-03-15', 88, 'nazma.khatun@example.com', FALSE, '2020-11-20'),
(104, 1, 'Farida Begum', 'Female', 'Kamal Uddin', 3, 160000.00, '1938-12-01', 86, 'farida.begum@example.com', TRUE, NULL),
(105, 1, 'Sultan Mahmud', 'Male', 'Jannat Ara', 7, 250000.00, '1940-07-11', 84, 'sultan.mahmud@example.com', TRUE, NULL),
(106, 1, 'Anisur Rahman', 'Male', 'Sufia Khatun', 2, 130000.00, '1942-01-20', 82, 'anisur.rahman@example.com', FALSE, '2022-05-09'),
(107, 1, 'Shamsun Nahar', 'Female', 'Mujibur Rahman', 4, 140000.00, '1944-10-18', 80, 'shamsun.nahar@example.com', TRUE, NULL),
(108, 1, 'Tariqul Islam', 'Male', 'Rani Akter', 5, 190000.00, '1946-09-30', 78, 'tariqul.islam@example.com', TRUE, NULL),
(109, 1, 'Rezaul Karim', 'Male', 'Sultana Jahan', 3, 210000.00, '1948-04-05', 76, 'rezaul.karim@example.com', TRUE, NULL),
(110, 1, 'Hasina Akter', 'Female', 'Abul Kalam', 6, 175000.00, '1950-11-11', 74, 'hasina.akter@example.com', TRUE, NULL);

-- Insert data for father
INSERT INTO father VALUES
(1, 'Mizanur Rahman', '1965-01-25', 60, 4, 2, 1200000.00, 'mizan.rahman@example.com', TRUE);

-- Insert father's gift history
INSERT INTO father_gifts VALUES
(1, 1, 2010, 'Gold Watch', 'Uncle Habib', 25000.00),
(2, 1, 2015, 'Land in village', 'Uncle Jabed', 350000.00),
(3, 1, 2018, 'Cash gift for house construction', 'Aunt Farida', 50000.00),
(4, 1, 2022, 'Laptop', 'Brother Sultan', 100000.00);
