-- ============================================================
-- 02. BLOKS — DATUBĀZES UN SQL
-- ============================================================
-- Strādājam ar datubāzi skola.db. Atver to ar DB Browser for SQLite.
-- Tas ir tas pats rīks, kas atļauts centralizētajā eksāmenā, un tam
-- nav vajadzīgs nekāds serveris — datubāze ir viens fails.
--
-- Ja datubāze sabojājas, to var izveidot no jauna:
--   python3 bin/izveido_db.py 02-datubazes/skola.db
--
-- Komentārs  -- ?  nozīmē: vispirms uzmini rezultātu, tikai tad palaid.
-- ============================================================


-- ============================================================
-- 1. KĀPĒC DATUBĀZE                                  [11-017]
-- ============================================================
-- CSV datnē 100 000 ierakstu meklēšana pēc vārda nozīmē izlasīt visu
-- datni no sākuma līdz beigām. Datubāze zina, kur meklēt.
--
-- Datne:      programma pati lasa, meklē, kārto un pārbauda.
-- Datubāze:   tu pasaki, KO gribi; datubāze zina, KĀ to atrast.
--
-- Datnē arī nav neviena, kas neļautu ierakstīt muļķības. Datubāzē ir.


-- ============================================================
-- 2. MŪSU DATUBĀZE                                   [11-018]
-- ============================================================
-- skolotaji   (id, vards, uzvards, epasts)
-- klases      (id, nosaukums, audzinatajs_id -> skolotaji.id)
-- skoleni     (id, vards, uzvards, klase_id -> klases.id, epasts, dzimsanas_gads)
-- prieksmeti  (id, nosaukums, skolotajs_id -> skolotaji.id)
-- atzimes     (id, skolens_id -> skoleni.id, prieksmets_id -> prieksmeti.id,
--              atzime, datums)
-- pulcini     (id, nosaukums, skolotajs_id, diena, vietu_skaits)
-- dalibnieki  (id, skolens_id -> skoleni.id, pulcins_id -> pulcini.id, pieteikts)
--
-- Biežākie datu tipi:
--   INTEGER   veseli skaitļi, arī id
--   TEXT      teksts un datumi formātā 'GGGG-MM-DD'
--   REAL      decimāldaļas (cena!)
--
-- Cenai NEKAD nelieto INTEGER — 1.09 kļūtu par 1.
--
-- PRIMĀRĀ ATSLĒGA viennozīmīgi identificē ierakstu. Divi skolēni var būt
-- ar vienādu vārdu un uzvārdu; ar vienādu id — ne.


-- ============================================================
-- 3. SELECT UN WHERE                                 [11-019]
-- ============================================================
SELECT * FROM skoleni;

SELECT vards, uzvards FROM skoleni;

SELECT vards, uzvards, dzimsanas_gads
FROM skoleni
WHERE dzimsanas_gads < 2009;

SELECT nosaukums FROM prieksmeti WHERE skolotajs_id = 3;

-- SELECT * ir ērts, bet paņem visas kolonnas, arī nevajadzīgās.
-- Reālā sistēmā tas nozīmē lieku darbu un lieku datu pārraidi.


-- ============================================================
-- 4. KĀRTOŠANA UN IEROBEŽOŠANA                       [11-020]
-- ============================================================
SELECT vards, uzvards FROM skoleni ORDER BY uzvards ASC;

SELECT vards, uzvards, dzimsanas_gads
FROM skoleni
ORDER BY dzimsanas_gads DESC, uzvards ASC;

SELECT atzime, datums FROM atzimes ORDER BY datums DESC LIMIT 10;

-- Katra vērtība vienu reizi
SELECT DISTINCT dzimsanas_gads FROM skoleni ORDER BY dzimsanas_gads;


-- ============================================================
-- 5. SALIKTI NOSACĪJUMI                              [11-021]
-- ============================================================
SELECT vards, uzvards FROM skoleni WHERE dzimsanas_gads BETWEEN 2008 AND 2010;

SELECT nosaukums FROM pulcini WHERE diena IN ('otrdiena', 'trešdiena');

-- LIKE šabloni:
--   'A%'    sākas ar A
--   '%a'    beidzas ar a
--   '%ozol%' satur ozol
--   '_a%'   otrais burts ir a
SELECT vards, uzvards FROM skoleni WHERE uzvards LIKE 'K%';

SELECT vards, uzvards FROM skoleni WHERE vards LIKE '_n%';

-- Tukša vērtība ir NULL. Uzmanību: = NULL nekad nav patiess!
SELECT vards, uzvards FROM skoleni WHERE epasts IS NULL;
-- SELECT vards FROM skoleni WHERE epasts = NULL;      -- ?


-- ============================================================
-- 6. AGREGĀTFUNKCIJAS                                [11-022]
-- ============================================================
SELECT COUNT(*) AS skolenu_skaits FROM skoleni;

SELECT ROUND(AVG(atzime), 2) AS videja FROM atzimes;

SELECT MIN(atzime) AS zemaka, MAX(atzime) AS augstaka FROM atzimes;

SELECT COUNT(*) AS bez_epasta FROM skoleni WHERE epasts IS NULL;

-- AS dod rezultāta kolonnai saprotamu nosaukumu.
--
-- COUNT(*)       skaita visas rindas
-- COUNT(epasts)  skaita rindas, kurās epasts NAV NULL   -- ?


-- ============================================================
-- 7. GROUP BY UN HAVING                              [11-023]
-- ============================================================
-- Viena skaitļa vietā — pa vienam skaitlim katrai grupai.
SELECT klase_id, COUNT(*) AS skaits
FROM skoleni
GROUP BY klase_id;

SELECT prieksmets_id, ROUND(AVG(atzime), 2) AS videja
FROM atzimes
GROUP BY prieksmets_id
ORDER BY videja DESC;

-- HAVING filtrē GRUPAS, WHERE filtrē IERAKSTUS.
--   WHERE  darbojas PIRMS grupēšanas
--   HAVING darbojas PĒC grupēšanas
SELECT skolens_id, COUNT(*) AS atzimju_skaits
FROM atzimes
GROUP BY skolens_id
HAVING COUNT(*) > 25;

-- Abi kopā: tikai rudens atzīmes, tad grupas ar vidējo virs 7
SELECT skolens_id, ROUND(AVG(atzime), 2) AS videja
FROM atzimes
WHERE datums >= '2025-10-01'
GROUP BY skolens_id
HAVING AVG(atzime) > 7;

-- Šis ir kļūda — grupas nevar filtrēt ar WHERE:
-- SELECT klase_id, COUNT(*) FROM skoleni WHERE COUNT(*) > 10 GROUP BY klase_id;


-- ============================================================
-- 8. RELĀCIJAS                                       [11-024]
-- ============================================================
-- Skolēna ierakstā neglabā klases nosaukumu, bet gan klases id.
-- Ja klasi pārsauc, tas jāmaina VIENĀ vietā, nevis 67.
--
-- ĀRĒJĀ ATSLĒGA norāda uz citas tabulas primāro atslēgu:
--   skoleni.klase_id  ->  klases.id
--
-- Saistību veidi mūsu datubāzē:
--   1:N   vienā klasē daudz skolēnu           klases -> skoleni
--   1:N   vienam skolotājam daudz priekšmetu  skolotaji -> prieksmeti
--   N:M   skolēns var būt daudzos pulciņos,
--         pulciņā var būt daudz skolēnu       skoleni <- dalibnieki -> pulcini
--
-- N:M saistībai VIENMĒR vajag starptabulu. dalibnieki un atzimes ir tieši tās.


-- ============================================================
-- 9. INNER JOIN                                      [11-025]
-- ============================================================
SELECT s.vards, s.uzvards, k.nosaukums AS klase
FROM skoleni AS s
INNER JOIN klases AS k ON s.klase_id = k.id;

SELECT p.nosaukums AS prieksmets, a.atzime, a.datums
FROM atzimes AS a
INNER JOIN prieksmeti AS p ON a.prieksmets_id = p.id
WHERE a.skolens_id = 5;

-- Trīs tabulas: skolēns, priekšmets un atzīme vienā rindā
SELECT s.vards, s.uzvards, p.nosaukums, a.atzime
FROM atzimes AS a
INNER JOIN skoleni AS s ON a.skolens_id = s.id
INNER JOIN prieksmeti AS p ON a.prieksmets_id = p.id
LIMIT 20;

-- Ja aizmirst ON, datubāze savieno KATRU rindu ar KATRU rindu.
-- 67 skolēni un 6 klases dod 402 rindas.


-- ============================================================
-- 10. LEFT JOIN                                      [11-026]
-- ============================================================
-- INNER JOIN atmet tos, kam nav pāra. LEFT JOIN patur visus no kreisās
-- tabulas un trūkstošo aizpilda ar NULL.
SELECT s.vards, s.uzvards, COUNT(a.id) AS atzimes
FROM skoleni AS s
LEFT JOIN atzimes AS a ON s.id = a.skolens_id
GROUP BY s.id
ORDER BY atzimes ASC;

-- Skolēni, kuriem nav nevienas atzīmes — ar INNER JOIN tos vispār
-- neieraudzītu:
SELECT s.vards, s.uzvards
FROM skoleni AS s
LEFT JOIN atzimes AS a ON s.id = a.skolens_id
WHERE a.id IS NULL;

-- Pulciņi bez dalībniekiem:
SELECT p.nosaukums
FROM pulcini AS p
LEFT JOIN dalibnieki AS d ON p.id = d.pulcins_id
WHERE d.id IS NULL;


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
--   pieteikumi(id, biedrs_id, trenina_id, datums)     <- starptabula
--
-- Zelta likums: ja vienu un to pašu informāciju raksti divās vietās,
-- shēma ir nepareiza. Piemēram, trenera vārds katrā treniņa ierakstā.


-- ============================================================
-- 12. CREATE TABLE                                   [11-028]
-- ============================================================
CREATE TABLE biedri (
    id INTEGER PRIMARY KEY,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    epasts TEXT UNIQUE
);

CREATE TABLE treninu_veidi (
    id INTEGER PRIMARY KEY,
    nosaukums TEXT NOT NULL,
    ilgums INTEGER
);

CREATE TABLE pieteikumi (
    id INTEGER PRIMARY KEY,
    biedrs_id INTEGER REFERENCES biedri(id),
    trenina_id INTEGER REFERENCES treninu_veidi(id),
    datums TEXT
);

-- Tabulu un lauku nosaukumus raksta bez garumzīmēm un atstarpēm.


-- ============================================================
-- 13. INSERT, UPDATE, DELETE                         [11-029]
-- ============================================================
INSERT INTO pulcini (nosaukums, skolotajs_id, diena, vietu_skaits)
VALUES ('Programmēšanas pulciņš', 4, 'ceturtdiena', 14);

UPDATE pulcini
SET vietu_skaits = 20
WHERE nosaukums = 'Šahs';

DELETE FROM dalibnieki
WHERE pulcins_id = 8;

-- ĻOTI SVARĪGI: bez WHERE šīs komandas attiecas uz VISIEM ierakstiem.
--   UPDATE skoleni SET klase_id = 1;    -- visi nonāk 10.a
--   DELETE FROM skoleni;                -- tabula tukša
-- Atsaukt nevar. Pirms UPDATE vai DELETE uzraksti to pašu nosacījumu
-- ar SELECT un pārbaudi, ko tas atlasa.


-- ============================================================
-- 14. DATU INTEGRITĀTE                               [11-030]
-- ============================================================
--   NOT NULL     lauks nedrīkst būt tukšs
--   UNIQUE       vērtība nedrīkst atkārtoties
--   PRIMARY KEY  NOT NULL + UNIQUE
--   REFERENCES   vērtībai jāeksistē otrā tabulā
--   CHECK        paša definēts nosacījums
--
-- Mūsu datubāzē atzīmei ir CHECK:
--   atzime INTEGER CHECK (atzime BETWEEN 1 AND 10)
--
-- Tāpēc šis neizdodas, un tas ir labi:
-- INSERT INTO atzimes (skolens_id, prieksmets_id, atzime, datums)
-- VALUES (1, 1, 15, '2025-11-01');                    -- ?
--
-- Kur validēt? Visur:
--   pārlūkā   — lai lietotājam uzreiz pateiktu, ka kaut kas nav kārtībā
--   serverī   — jo pārlūku var apiet
--   datubāzē  — jo arī serverī var būt kļūda
