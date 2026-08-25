-- ============================================================
-- 02. BLOKS — DATUBĀZES UN SQL
-- ============================================================
-- Vaicājumus izmēģini šeit:
--   https://www.w3schools.com/sql/trysql.asp
-- Savu datubāzi veido ar DB Browser for SQLite.
--
-- Abi rīki ir atļauti centralizētajā eksāmenā.
--
-- Komentārs  -- ?  nozīmē: vispirms uzmini rezultātu, tikai tad palaid.
-- ============================================================


-- ============================================================
-- 1. KĀPĒC DATUBĀZE                                  [11-017]
-- ============================================================
-- CSV datnē 100 000 ierakstu meklēšana pēc vārda nozīmē izlasīt
-- visu datni no sākuma līdz beigām. Datubāze to izdara uzreiz,
-- jo tā zina, kur meklēt (indeksi).
--
-- Datne:      programma pati lasa, meklē, kārto un pārbauda.
-- Datubāze:   tu pasaki, KO gribi; datubāze pati zina, KĀ to atrast.
--
-- Datnē arī nav neviena, kas neļautu ierakstīt muļķības. Datubāzē ir.


-- ============================================================
-- 2. TABULA UN DATU TIPI                             [11-018]
-- ============================================================
-- Tabula = rindas (ieraksti) un kolonnas (lauki).
--
--   id  | nosaukums | cena
--   ----+-----------+------
--   1   | Piens     | 1.09
--   2   | Maize     | 2.45
--
-- Biežākie tipi:
--   INTEGER   veseli skaitļi, arī id
--   TEXT      teksts
--   REAL      decimāldaļas (cena!)
--   DATE      datums
--
-- Cenai NEKAD nelieto INTEGER — 1.09 kļūtu par 1.
--
-- PRIMĀRĀ ATSLĒGA (PRIMARY KEY) ir lauks, kas viennozīmīgi identificē
-- ierakstu. Divi skolēni var būt ar vienādu vārdu; ar vienādu id — ne.


-- ============================================================
-- 3. SELECT UN WHERE                                 [11-019]
-- ============================================================
SELECT * FROM Products;

SELECT ProductName, Price FROM Products;

SELECT ProductName, Price
FROM Products
WHERE Price > 50;

SELECT CustomerName, City
FROM Customers
WHERE Country = 'Germany';

-- SELECT *  ir ērts, bet paņem visas kolonnas, arī tās, kas nav vajadzīgas.
-- Reālā sistēmā tas nozīmē lieku darbu un lieku datu pārraidi.


-- ============================================================
-- 4. KĀRTOŠANA UN IEROBEŽOŠANA                       [11-020]
-- ============================================================
SELECT ProductName, Price
FROM Products
ORDER BY Price DESC;

SELECT ProductName, Price
FROM Products
ORDER BY Price DESC
LIMIT 5;

-- Vairāki lauki: vispirms pēc valsts, tad pēc pilsētas
SELECT CustomerName, Country, City
FROM Customers
ORDER BY Country ASC, City ASC;

-- Katra vērtība vienu reizi
SELECT DISTINCT Country FROM Customers;


-- ============================================================
-- 5. SALIKTI NOSACĪJUMI                              [11-021]
-- ============================================================
SELECT ProductName, Price
FROM Products
WHERE Price BETWEEN 20 AND 40;

SELECT CustomerName, Country
FROM Customers
WHERE Country IN ('Germany', 'France');

-- LIKE šabloni:
--   'A%'    sākas ar A
--   '%a'    beidzas ar a
--   '%ark%' satur ark
--   '_a%'   otrais burts ir a
SELECT CustomerName
FROM Customers
WHERE CustomerName LIKE 'A%';

-- Tukša vērtība ir NULL. Uzmanību: = NULL nekad nav patiess!
SELECT CustomerName FROM Customers WHERE PostalCode IS NULL;
-- SELECT CustomerName FROM Customers WHERE PostalCode = NULL;   -- ?


-- ============================================================
-- 6. AGREGĀTFUNKCIJAS                                [11-022]
-- ============================================================
SELECT COUNT(*) AS produktu_skaits FROM Products;

SELECT AVG(Price) AS videja_cena FROM Products;

SELECT MIN(Price) AS letakais, MAX(Price) AS dargakais FROM Products;

SELECT COUNT(*) AS klienti
FROM Customers
WHERE Country = 'Germany';

-- AS dod rezultāta kolonnai saprotamu nosaukumu.
--
-- COUNT(*)      skaita visas rindas
-- COUNT(lauks)  skaita rindas, kurās lauks NAV NULL


-- ============================================================
-- 7. GROUP BY UN HAVING                              [11-023]
-- ============================================================
-- Viena skaitļa vietā — pa vienam skaitlim katrai grupai.
SELECT CategoryID, COUNT(*) AS skaits
FROM Products
GROUP BY CategoryID;

SELECT Country, COUNT(*) AS klienti
FROM Customers
GROUP BY Country
ORDER BY klienti DESC;

-- HAVING filtrē GRUPAS, WHERE filtrē IERAKSTUS.
--   WHERE  darbojas PIRMS grupēšanas
--   HAVING darbojas PĒC grupēšanas
SELECT Country, COUNT(*) AS klienti
FROM Customers
GROUP BY Country
HAVING COUNT(*) > 5;

-- Šis ir kļūda — nevar filtrēt grupas ar WHERE:
-- SELECT Country, COUNT(*) FROM Customers WHERE COUNT(*) > 5 GROUP BY Country;


-- ============================================================
-- 8. RELĀCIJAS                                       [11-024]
-- ============================================================
-- Pasūtījumā neglabā klienta vārdu un adresi, bet gan klienta id.
-- Ja klients maina adresi, tā jāmaina VIENĀ vietā, nevis 500.
--
-- ĀRĒJĀ ATSLĒGA (FOREIGN KEY) ir lauks, kas norāda uz citas tabulas
-- primāro atslēgu.
--
--   Orders.CustomerID  ->  Customers.CustomerID
--
-- Saistību veidi:
--   1:1   vienam ierakstam atbilst tieši viens (reti)
--   1:N   vienam klientam daudz pasūtījumu (visbiežāk)
--   N:M   daudz pasūtījumu satur daudz produktu -> vajag STARPTABULU
--
-- w3schools datubāzē N:M ir OrderDetails: tā savieno Orders un Products.


-- ============================================================
-- 9. INNER JOIN                                      [11-025]
-- ============================================================
-- Savieno divas tabulas pa saistīto lauku.
SELECT Products.ProductName, Categories.CategoryName
FROM Products
INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;

-- Aizstājvārdi (alias) saīsina pierakstu:
SELECT p.ProductName, s.SupplierName, s.Country
FROM Products AS p
INNER JOIN Suppliers AS s ON p.SupplierID = s.SupplierID;

-- Trīs tabulas:
SELECT p.ProductName, c.CategoryName, s.SupplierName
FROM Products AS p
INNER JOIN Categories AS c ON p.CategoryID = c.CategoryID
INNER JOIN Suppliers AS s ON p.SupplierID = s.SupplierID;

-- Ja aizmirst ON, datubāze savieno KATRU rindu ar KATRU rindu.
-- 77 produkti un 8 kategorijas dod 616 rindas.


-- ============================================================
-- 10. LEFT JOIN                                      [11-026]
-- ============================================================
-- INNER JOIN atmet tos, kam nav pāra. LEFT JOIN patur visus no
-- kreisās tabulas, bet trūkstošo aizpilda ar NULL.
SELECT c.CustomerName, COUNT(o.OrderID) AS pasutijumi
FROM Customers AS c
LEFT JOIN Orders AS o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName
ORDER BY pasutijumi DESC;

-- Klienti bez pasūtījumiem — tikai ar LEFT JOIN tos vispār var ieraudzīt:
SELECT c.CustomerName
FROM Customers AS c
LEFT JOIN Orders AS o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;


-- ============================================================
-- 11. DATUBĀZES PLĀNOŠANA                            [11-027]
-- ============================================================
-- Trīs soļi:
--   1) atrodi LIETAS, par kurām jāglabā dati -> tabulas
--   2) atrodi katras lietas ĪPAŠĪBAS         -> lauki
--   3) atrodi, kā lietas SAISTĀS             -> ārējās atslēgas
--
-- Piemērs: sporta klubs
--   biedri(id, vards, uzvards, epasts)
--   treninu_veidi(id, nosaukums, ilgums)
--   pieteikumi(id, biedrs_id, trenina_id, datums)
--
-- Zelta likums: ja vienu un to pašu informāciju raksti divās vietās,
-- shēma ir nepareiza. Piemēram, trenera vārds katrā treniņa ierakstā.


-- ============================================================
-- 12. CREATE TABLE                                   [11-028]
-- ============================================================
CREATE TABLE skoleni (
    id INTEGER PRIMARY KEY,
    vards TEXT NOT NULL,
    klase TEXT NOT NULL,
    epasts TEXT UNIQUE
);

CREATE TABLE pulcini (
    id INTEGER PRIMARY KEY,
    nosaukums TEXT NOT NULL,
    diena TEXT
);

-- Starptabula N:M saistībai
CREATE TABLE dalibnieki (
    id INTEGER PRIMARY KEY,
    skolens_id INTEGER REFERENCES skoleni(id),
    pulcins_id INTEGER REFERENCES pulcini(id)
);

-- Tabulu un lauku nosaukumus raksta bez garumzīmēm un atstarpēm.


-- ============================================================
-- 13. INSERT, UPDATE, DELETE                         [11-029]
-- ============================================================
INSERT INTO skoleni (vards, klase, epasts)
VALUES ('Anna Kalnina', '11.a', 'anna@skola.lv');

UPDATE skoleni
SET klase = '12.a'
WHERE id = 1;

DELETE FROM skoleni
WHERE id = 1;

-- ĻOTI SVARĪGI: bez WHERE šīs komandas attiecas uz VISIEM ierakstiem.
--   UPDATE skoleni SET klase = '12.a';     -- visi kļūst par 12.a
--   DELETE FROM skoleni;                   -- tabula tukša
-- Atsaukt nevar. Pirms UPDATE vai DELETE vispirms uzraksti to pašu
-- nosacījumu ar SELECT un pārbaudi, ko tas atlasa.


-- ============================================================
-- 14. DATU INTEGRITĀTE                               [11-030]
-- ============================================================
-- Ierobežojumi neļauj datubāzē nonākt muļķībām:
--
--   NOT NULL           lauks nedrīkst būt tukšs
--   UNIQUE             vērtība nedrīkst atkārtoties
--   PRIMARY KEY        NOT NULL + UNIQUE
--   REFERENCES         vērtībai jāeksistē otrā tabulā
--   CHECK              paša definēts nosacījums

CREATE TABLE preces (
    id INTEGER PRIMARY KEY,
    nosaukums TEXT NOT NULL,
    cena REAL CHECK (cena >= 0),
    kategorija_id INTEGER REFERENCES kategorijas(id)
);

-- Kur validēt? Visur:
--   pārlūkā   — lai lietotājam uzreiz pateiktu, ka kaut kas nav kārtībā
--   serverī   — jo pārlūku var apiet
--   datubāzē  — jo arī serverī var būt kļūda
