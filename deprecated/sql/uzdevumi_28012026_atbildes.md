# SQL atbildes — uzdevumi_28012026.md

## 1) Kategoriju “cenu profils”

```sql
SELECT
  c.CategoryName AS CategoryName,
  COUNT(p.ProductID) AS ProductCount,
  MIN(p.Price) AS MinPrice,
  MAX(p.Price) AS MaxPrice
FROM Categories c
JOIN Products p ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryID, c.CategoryName
ORDER BY ProductCount DESC;
```

## 2) Produktu “pārdošanas profils” (SUM + AVG)

```sql
SELECT
  p.ProductName AS ProductName,
  SUM(od.Quantity) AS TotalQuantitySold,
  AVG(od.Quantity) AS AvgQuantityPerOrderLine
FROM Products p
JOIN OrderDetails od ON od.ProductID = p.ProductID
GROUP BY p.ProductID, p.ProductName
ORDER BY TotalQuantitySold DESC;
```

## 3) Piegādātāju statistika par produktu cenām (COUNT + AVG)

```sql
SELECT
  s.SupplierName AS SupplierName,
  COUNT(p.ProductID) AS ProductCount,
  AVG(p.Price) AS AvgPrice
FROM Suppliers s
JOIN Products p ON p.SupplierID = s.SupplierID
GROUP BY s.SupplierID, s.SupplierName
ORDER BY AvgPrice DESC;
```

## 4) Pasūtījumi pa valsti un piegādātāju

```sql
SELECT
  cu.Country AS Country,
  sh.ShipperName AS ShipperName,
  COUNT(o.OrderID) AS OrdersCount
FROM Orders o
JOIN Customers cu ON cu.CustomerID = o.CustomerID
JOIN Shippers sh ON sh.ShipperID = o.ShipperID
GROUP BY cu.Country, sh.ShipperID, sh.ShipperName
ORDER BY Country ASC, OrdersCount DESC;
```

## 5) Pārdotās vienības pa kategoriju un piegādātāju

```sql
SELECT
  c.CategoryName AS CategoryName,
  s.SupplierName AS SupplierName,
  SUM(od.Quantity) AS UnitsSold
FROM OrderDetails od
JOIN Products p ON p.ProductID = od.ProductID
JOIN Categories c ON c.CategoryID = p.CategoryID
JOIN Suppliers s ON s.SupplierID = p.SupplierID
GROUP BY c.CategoryID, c.CategoryName, s.SupplierID, s.SupplierName
ORDER BY UnitsSold DESC;
```

## 6A) Kategorijas, kur kopā pārdotas vismaz 200 vienības

```sql
SELECT
  c.CategoryName AS CategoryName,
  SUM(od.Quantity) AS UnitsSold
FROM OrderDetails od
JOIN Products p ON p.ProductID = od.ProductID
JOIN Categories c ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, c.CategoryName
HAVING SUM(od.Quantity) >= 200
ORDER BY UnitsSold DESC;
```

## 6B) Piegādātāji, kuriem ir vismaz 5 produkti

```sql
SELECT
  s.SupplierName AS SupplierName,
  COUNT(p.ProductID) AS ProductCount
FROM Suppliers s
JOIN Products p ON p.SupplierID = s.SupplierID
GROUP BY s.SupplierID, s.SupplierName
HAVING COUNT(p.ProductID) >= 5
ORDER BY ProductCount DESC;
```
