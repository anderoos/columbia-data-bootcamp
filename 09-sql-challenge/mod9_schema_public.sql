-- Data Engineering
-- DROP TABLE if exists
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;

--Creating titles table
CREATE TABLE titles (
	title_id VARCHAR PRIMARY KEY NOT NULL,
	title VARCHAR NOT NULL);
	
-- Create table departments
CREATE TABLE departments (
 	dept_no VARCHAR PRIMARY KEY NOT NULL,
 	dept_name VARCHAR NOT NULL);
	
-- Create table employees
CREATE TABLE employees (
	emp_no INT PRIMARY KEY NOT NULL,
	emp_title_id VARCHAR,
	birth_date DATE,
	first_name TEXT,
	last_name TEXT,
	sex TEXT,
	hire_date DATE,
	FOREIGN KEY (emp_title_id) REFERENCES titles (title_id));

--Create table dept_emp
CREATE TABLE dept_emp (
	emp_no INT NOT NULL,
	dept_no VARCHAR NOT NULL,
    PRIMARY KEY (emp_no, dept_no),
    FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
    FOREIGN KEY (dept_no) REFERENCES departments(dept_no));

-- Create table dept_managers
CREATE TABLE dept_manager (
	dept_no VARCHAR NOT NULL,
	emp_no INT NOT NULL,
    PRIMARY KEY (dept_no, emp_no),
    FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
    FOREIGN KEY (emp_no) REFERENCES employees(emp_no));
	
-- Creating salaries table
CREATE TABLE salaries (
	emp_no INT PRIMARY KEY NOT NULL,
	salary INT NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees (emp_no));
	
-- PREVIEW
-- SELECT * FROM departments
-- SELECT * FROM dept_emp
-- SELECT * FROM dept_manager
-- SELECT * FROM employees
-- SELECT * FROM salaries
-- SELECT * FROM titles

