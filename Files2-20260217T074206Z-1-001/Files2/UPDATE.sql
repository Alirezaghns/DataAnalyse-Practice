--INSERT 
--UPDATE
--DELETE

--UPDATE Northwind..Employees
--SET FirstName = 'Ahmad'
--, LastName = 'Rezaee'
--WHERE  EmployeeID = 6


--NAME AND LASTNAME AHmad Rezaee b SARA ALIPOUR Taghir namad

SELECT *
FROM Northwind..Employees
WHERE FirstName = 'Ahmad'
AND LastName = 'Rezaee'
AND EmployeeID = 6


UPDATE Northwind..Employees
SET FirstName = 'Sara'
,LastName = 'Alipour'
WHERE FirstName = 'Ahmad'
AND LastName = 'Rezaee'
AND EmployeeID = 6
