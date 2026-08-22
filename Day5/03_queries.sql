#Q1. Display all employees
SELECT * FROM employees;

#Q2. Display only name and salary
SELECT name, salary FROM employees;

#Q3. Display employees with salary greater than 60000
SELECT * FROM employees WHERE salary > 60000;

#Q4. Display employees from a specific city
SELECT * FROM employees WHERE city = 'Pune';

#Q5. Display employees in a specific department
SELECT * FROM employees WHERE department = 'Data Science';

#Q7. Display unique departments
SELECT DISTINCT department FROM employees;

#Q8. Sort employees by salary from highest to lowest
SELECT * FROM employees ORDER BY salary DESC;
