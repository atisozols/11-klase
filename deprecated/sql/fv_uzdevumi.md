# SQL uzdevumi (pamati līdz INNER JOIN + “order line view”) — jauna variācija

## 1) Klienti ar konkrētu burtu nosaukumā + sakārtošana
Mārketingam vajag klientus, kuru nosaukumā ir burts **“a”** (vai cits burts pēc izvēles). Izvada: klienta nosaukums, kontaktpersona, pilsēta, valsts. Sakārto pēc valsts, tad pēc klienta nosaukuma A–Z.

## 2) Piegādātāju (Suppliers) un viņu produktu saraksts
Iepirkumu nodaļa grib redzēt, kādus produktus piegādā katrs piegādātājs. Izvada: piegādātāja nosaukums, piegādātāja valsts, produkta nosaukums, produkta cena. Izmanto INNER JOIN Suppliers–Products. Sakārto pēc piegādātāja nosaukuma, tad pēc cenas no dārgākā uz lētāko.

## 3) Produkti ar kategoriju un piegādātāju vienā skatā (3 JOIN)
Noliktavai vajag vienu tabulu, kur redzams: produkta nosaukums, kategorijas nosaukums, piegādātāja nosaukums, cena. Izmanto Products + Categories + Suppliers. Sakārto pēc kategorijas, tad pēc produkta nosaukuma.

## 4) Pasūtījumi vienā pilsētā (Orders + Customers)
Atbalsta komandai jāatrod visi pasūtījumi, kas veikti klientiem no konkrētas **pilsētas** (izvēlies pilsētu, kas eksistē). Izvada: pasūtījuma ID, pasūtījuma datums, klienta nosaukums, pilsēta. Sakārto pēc datuma no jaunākā uz vecāko.

## 5) Pasūtījumi, ko apstrādājis konkrēts darbinieks (Orders + Employees)
Vadītājs grib pārbaudīt vienu darbinieku. Atrodi visus pasūtījumus, ko apstrādājis konkrēts darbinieks (filtrs pēc uzvārda vai EmployeeID). Izvada: pasūtījuma ID, pasūtījuma datums, darbinieka vārds, darbinieka uzvārds. Sakārto pēc datuma no jaunākā uz vecāko.

## 6) Pasūtījuma rindas ar mērvienību (OrderDetails + Products + Orders)
Klients prasa precīzu informāciju par precēm pasūtījumā, ieskaitot mērvienību. Izvada: pasūtījuma ID, pasūtījuma datums, produkta nosaukums, mērvienība (Unit), daudzums. Izmanto Orders + OrderDetails + Products. Sakārto pēc pasūtījuma ID, tad produkta nosaukuma.

---

# Uzdevumi ar pilno “Order Line View” (4 uzdevumi ar pilno JOIN ķēdi)

**Pilnajam “order line view” obligāti jāiekļauj vismaz:**
- pasūtījuma ID, pasūtījuma datums  
- klienta nosaukums (+ pilsēta vai valsts kā papildu lauks)  
- darbinieka vārds + uzvārds  
- piegādātāja (Shipper) nosaukums  
- produkta nosaukums, kategorijas nosaukums  
- daudzums (Quantity), cena (Price)

(Izmanto: Orders + Customers + Employees + Shippers + OrderDetails + Products + Categories)

## 7) Pilnais “Order Line View” ar papildu filtru uz cenu
Izveido pilno “order line view”, bet parādi tikai tās rindas, kur produkta cena ir **virs noteiktas robežas** (piem., Price > 50). Sakārto pēc cenas dilstoši, pēc tam pēc datuma.

## 8) Pilnais “Order Line View” konkrētai valstij + sakārtošana
Izveido pilno “order line view” tikai klientiem no konkrētas **valsts** (izvēlies valsti, kas eksistē). Izvada arī klienta valsti. Sakārto pēc pasūtījuma datuma no jaunākā uz vecāko, tad pēc klienta nosaukuma.

## 9) Pilnais “Order Line View” konkrētam piegādātājam + kolonnas izvēle
Izveido pilno “order line view” tikai pasūtījumiem, kas nosūtīti ar konkrētu **Shipper** (izvēlies). Izvada: pasūtījuma ID, datums, shipper nosaukums, klienta nosaukums, produkta nosaukums, daudzums, cena. Sakārto pēc pasūtījuma ID, tad pēc produkta nosaukuma.

## 10) Pilnais “Order Line View” konkrētai kategorijai + filtrs uz daudzumu
Izveido pilno “order line view” tikai vienai kategorijai (piem., “Seafood” vai “Beverages”), un papildus parādi tikai tās rindas, kur daudzums ir **>= 10** (vai cita robeža). Sakārto pēc daudzuma dilstoši, pēc tam pēc datuma no jaunākā uz vecāko.
