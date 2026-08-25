# SQL atbildes — uzdevumi_27012026.md

## 1) Pasūtījumu skaits darbiniekiem

```sql
SELECT
  Employees.FirstName,
  Employees.LastName,
  COUNT(Orders.OrderID) AS OrdersCount
FROM Employees
INNER JOIN Orders ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY Employees.EmployeeID, Employees.FirstName, Employees.LastName
ORDER BY OrdersCount DESC;
```

## 2) Produktu skaits piegādātājiem (Suppliers)

```sql
SELECT
  Suppliers.SupplierName,
  COUNT(*) AS ProductCount
FROM Suppliers
INNER JOIN Products ON Products.SupplierID = Suppliers.SupplierID
GROUP BY Suppliers.SupplierID, Suppliers.SupplierName
ORDER BY ProductCount DESC;
```

## 3) Minimālā produkta cena kategorijās

```sql
SELECT
  Categories.CategoryName,
  MIN(Products.Price) AS MinPrice
FROM Categories
INNER JOIN Products ON Products.CategoryID = Categories.CategoryID
GROUP BY Categories.CategoryID, Categories.CategoryName
ORDER BY MinPrice ASC;
```

## 4) Vidējais pasūtītais daudzums (Quantity)

```sql
SELECT
  Products.ProductName,
  AVG(OrderDetails.Quantity) AS AvgQuantity
FROM Products
INNER JOIN OrderDetails ON OrderDetails.ProductID = Products.ProductID
GROUP BY Products.ProductID, Products.ProductName
ORDER BY AvgQuantity DESC;
```
