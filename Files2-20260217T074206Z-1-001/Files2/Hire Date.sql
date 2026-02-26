--karmandani ra k tarikhe estekhdame sale balaye 1994 darand ra gozaresh dahid
SELECT (FirstName + ' ' + LastName) AS FullName , year(HireDate) AS TarikheEstekhdam
FROM Employees
WHERE year(HireDate) >= 1994