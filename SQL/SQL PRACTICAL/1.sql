--1.1 
SELECT client_name
FROM Client Info Table
LEFT JOIN Company Table
ON Client Info Table.client_id = Company Table.client_id


--1.2
FULL OUTER JOIN

--1.3

--1.3.1
SELECT employee_name,manager_id
FROM tbl_employees_and_managers
WHERE manager_id is not NULL

--1.3.2
