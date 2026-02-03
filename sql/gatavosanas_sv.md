# 10 SQL treniņuzdevumi (gatavošanās pārbaudes darbam) — sarežģītība aug straujāk
**Tēmas:** SELECT, WHERE, ORDER BY, INNER JOIN, “order line view”, un beigās GROUP BY.  

---

## 1) LIKE + precīzs nosacījums (nevis “satur”)
Atrodi klientus, kuru **CustomerName sākas ar “A”**.  
Izvada: CustomerName, ContactName, City, Country.  
Sakārto pēc Country, tad CustomerName A–Z.

---

## 2) LIKE + 2 nosacījumi (AND)
Atrodi klientus, kuru **CustomerName satur “a”** un **Country ir “UK”** (vai cita valsts, kas eksistē).  
Izvada: CustomerName, Country, City.  
Sakārto pēc City, tad CustomerName.

---

## 3) 2 JOIN: produkti ar kategoriju + filtrs pēc cenas
Parādi produktus kopā ar kategoriju: ProductName, CategoryName, Price.  
Filtrs: Price **>= 30** (vai cits slieksnis).  
Izmanto Products + Categories (INNER JOIN).  
Sakārto pēc Price dilstoši, tad ProductName.

---

## 4) 2 JOIN: pasūtījumi + piegādātājs (Shippers) + filtrs pēc piegādātāja
Parādi: OrderID, OrderDate, ShipperName.  
Filtrs: ShipperName ir konkrēts (izvēlies jebkuru esošu piegādātāju).  
Sakārto pēc OrderDate DESC.

*(Mērķis: pareizā saite Orders ↔ Shippers, un filtrs pēc teksta vērtības.)*

---

## 5) 3 JOIN: pasūtījumi konkrētai pilsētai + piegādātājs
Parādi visus pasūtījumus klientiem no konkrētas **pilsētas** (piem., London/Berlin utt.):  
OrderID, OrderDate, CustomerName, City, ShipperName.  
Izmanto Orders + Customers + Shippers.  
Sakārto pēc OrderDate DESC, tad CustomerName.

---

## 6) 4 JOIN: pasūtījuma rindas ar kategoriju (OrderDetails “pavairo” rindas)
Parādi pasūtījuma rindas ar kategoriju:  
OrderID, OrderDate, ProductName, CategoryName, Quantity.  
Izmanto Orders + OrderDetails + Products + Categories.  
Sakārto pēc OrderID, tad CategoryName, tad ProductName.

---

## 7) Pilnais “Order Line View”
Izveido pilno “order line view” ar kolonnām:
- OrderID, OrderDate  
- CustomerName, Country  
- Employee FirstName + LastName  
- ShipperName  
- ProductName, CategoryName  
- Quantity, Price  

Izmanto: Orders + Customers + Employees + Shippers + OrderDetails + Products + Categories.  
Sakārto pēc OrderDate DESC, tad OrderID, tad ProductName.  

---

## 8) GROUP BY: pasūtījumu skaits pa piegādātājiem (Shippers)
Parādi katram piegādātājam:
- ShipperName
- pasūtījumu skaitu (COUNT Orders)

Izmanto Orders + Shippers.  
Sakārto pēc pasūtījumu skaita dilstoši.

---

## 9) GROUP BY: produktu “pārdošanas apjoms” (SUM) pa produktiem
Parādi katram produktam:
- ProductName
- kopējo pārdoto daudzumu (SUM OrderDetails.Quantity)

Izmanto OrderDetails + Products.  
Sakārto pēc SUM(Quantity) dilstoši.

*(Mērķis: saprast, ka pārdošanas apjoms nāk no OrderDetails.)*

---

## 10) GROUP BY ar 2 laukiem: pārdotās vienības pa valsti un kategoriju
Parādi katrai kombinācijai:
- Country (no Customers)
- CategoryName (no Categories)
- kopā pārdotās vienības (SUM OrderDetails.Quantity)

Izmanto: Customers → Orders → OrderDetails → Products → Categories.  
GROUP BY: Country, CategoryName.  
Sakārto pēc Country A–Z un pēc pārdotajām vienībām dilstoši.
