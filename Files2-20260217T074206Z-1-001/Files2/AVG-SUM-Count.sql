--arzoontarin va geroontar mahsool
SELECT MIN (UnitPrice) AS MINUNITPRICE , MAX(UnitPrice) AS MAXUNITPRICE
FROM Products

--Kamtarin va Bishtarin takhfif
SELECT MIN (Discount) AS MINDISCOUNT, MAX(Discount) AS MAXDISCOUNT
FROM [Order Details]


--bishtarin va kamtarin gheymate mahsool dar har daste bandi
SELECT CategoryID , MIN (UnitPrice) AS MINUNITPRICE , MAX(UnitPrice) AS MAXUNITPRICE
FROM Products
GROUP BY CategoryID
ORDER BY CategoryID

--ghadminitarin va jadidtarin sefaresh har moshtari

SELECT CustomerID , MIN (OrderDate) AS OLDEST ,  MAX (OrderDate) AS NEWEST
FROM Orders
GROUP BY CustomerID
ORDER BY CustomerID

-- AVG SUM COUNT
-- TEDAD KOLE MOSHTARIHA
SELECT Count(CustomerID) CountCustomers
FROM Customers


--miangin gheymate mahsoolat
SELECT AVG (UnitPrice) AS AVGPRice
FROM Products


--SUM
--mojodie kole anbar mahsoolat cheghadre

SELECT SUM (UnitsInStock) AS SUMUnits
FROM Products