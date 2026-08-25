# 02. Datubāzes un SQL

**16 stundas (11-017 – 11-032)** · Standarta 3. temats “Kā automātiski apstrādāt un attēlot datus?”

**Bloka mērķis:** izplānot un izveidot datubāzi ar vairākām saistītām tabulām un iegūt no
tās vajadzīgo informāciju ar vaicājumiem.

**Teorija un piemēri:** [`teorija.sql`](teorija.sql) · **Darba fails:** [`uzdevumi.sql`](uzdevumi.sql)
**Pārbaudes darbi:** privātajā `sv-fv` repozitorijā
**Noslēgums:** SV2 — biļetes (11-032)

**Rīki.** Vaicājumus rakstām [w3schools SQL Tryit](https://www.w3schools.com/sql/trysql.asp) —
tur jau ir gatava datubāze un nekas nav jāuzstāda. Savu datubāzi veidojam ar **DB Browser
for SQLite**. Abi ir tie paši rīki, kas atļauti centralizētajā eksāmenā.

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 02-datubazes/README.md && python3 bin/darbafails.py 02-datubazes -->

| Nr. | Tēma | Sasniedzamais rezultāts |
| --- | --- | --- |
| 11-017 | Datubāzes jēdziens. No datnes uz datubāzi. | Skaidro, kādas problēmas rodas, glabājot datus CSV datnē, un kā tās risina datubāze. |
| 11-018 | Tabula, ieraksts, lauks. Datu tipi un primārā atslēga. | Nosauc tabulas daļas, izvēlas lauka datu tipu un skaidro primārās atslēgas nozīmi. |
| 11-019 | Vaicājums `SELECT`. Datu atlase ar `WHERE`. | Uzraksta vaicājumu, kas atlasa noteiktus laukus un ierakstus. |
| 11-020 | `ORDER BY`, `LIMIT`, `DISTINCT`. | Sakārto un ierobežo vaicājuma rezultātu. |
| 11-021 | `AND`, `OR`, `IN`, `BETWEEN`, `LIKE`, `NULL`. | Veido saliktus atlases nosacījumus un meklē tekstā. |
| 11-022 | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`. | Aprēķina kopsavilkuma vērtības no daudziem ierakstiem. |
| 11-023 | Grupēšana ar `GROUP BY` un filtrēšana ar `HAVING`. | Sagrupē ierakstus pēc lauka un aprēķina kopsavilkumu katrai grupai. |
| 11-024 | Saistītas tabulas. Ārējā atslēga. Saistību veidi 1:1, 1:N, N:M. | Atpazīst tabulu saistības un skaidro, kāpēc dati ir sadalīti vairākās tabulās. |
| 11-025 | Tabulu savienošana ar `INNER JOIN`. | Savieno divas tabulas un izvada datus no abām. |
| 11-026 | `LEFT JOIN`. Agregātfunkcijas pār savienotām tabulām. | Izvēlas piemērotu savienojuma veidu un aprēķina kopsavilkumu pār vairākām tabulām. |
| 11-027 | No apraksta uz datubāzes shēmu. | Izplāno datubāzi ar vairākām saistītām tabulām atbilstoši uzdevuma aprakstam. |
| 11-028 | Tabulu izveide. Datu tipi un ierobežojumi. | Izveido tabulas ar primārajām un ārējām atslēgām DB Browser for SQLite vidē. |
| 11-029 | `INSERT`, `UPDATE`, `DELETE`. | Pievieno, maina un dzēš ierakstus, saprotot izmaiņu neatgriezeniskumu. |
| 11-030 | Datu validācija un integritāte datubāzē. | Skaidro, kā ierobežojumi pasargā datus, un pievieno tos savai tabulai. |
| 11-031 | Datubāzes un SQL: atkārtojums. Gatavošanās biļetēm. | Atkārto bloka jēdzienus un vingrinās mutiski pamatot savu vaicājumu. |
| 11-032 | Pārbaudes darbs: datubāzes plānošana un SQL vaicājumi. | Demonstrē bloka sasniedzamos rezultātus, aizstāvot atbildi mutiski. |

<!-- TABULA:BEIGAS -->

---

## 11-017 · Kāpēc datubāze
`jaukta` · `teorija.sql` §1

**Tēma:** Datubāzes jēdziens. No datnes uz datubāzi.
**SR:** Skaidro, kādas problēmas rodas, glabājot datus CSV datnē, un kā tās risina datubāze.
**Standarts:** T.Li.2. · T.O.2.3.4.

**Gaita**
- 10' — pērnā gada CSV programma: kas notiek, ja datu ir 100 000 un meklē pēc vārda?
- 10' — demo §1: tā pati informācija tabulā; vaicājums pret ciklu
- 15' — uzdevumi burtnīcā
- 5' — kur ap mums ir datubāzes (e-klase, veikala kase, bibliotēka)

**Uzdevumi**
1. Burtnīcā: uzskaiti trīs problēmas, kas rodas, glabājot skolas datus CSV datnēs.
2. Burtnīcā: dotajam CSV fragmentam pieraksti, kā izskatītos atbilstoša tabula — kādi lauki
   un kāda tipa dati.
3. Burtnīcā: pieraksti, kuri dati skolas sistēmā atkārtojas un tāpēc būtu jāglabā atsevišķi.
4. ★ Atrodi savā 10. klases projektā vietu, kur datubāze būtu bijusi ērtāka par datni.

**Mājasdarbs:** 2. uzdevums

## 11-018 · Tabula un datu tipi
`prakse` · `teorija.sql` §2

**Tēma:** Tabula, ieraksts, lauks. Datu tipi un primārā atslēga.
**SR:** Nosauc tabulas daļas, izvēlas lauka datu tipu un skaidro primārās atslēgas nozīmi.
**Standarts:** T.O.2.3.4.

**Gaita**
- 5' — tabulas anatomija uz tāfeles
- 10' — demo §2: INTEGER, TEXT, REAL, DATE; kāpēc cenai nav INTEGER
- 20' — uzdevumi
- 5' — kāpēc katrai tabulai vajag `id`

**Uzdevumi**
5. Aplūko w3schools datubāzes tabulu `Products` un pieraksti katra lauka datu tipu.
6. Dotajam aprakstam «skolas pulciņi» pieraksti lauku sarakstu ar datu tipiem.
7. Pieraksti, kurš lauks katrā no trim dotajām tabulām būtu primārā atslēga un kāpēc.
8. Atrodi w3schools datubāzē divas tabulas, kurās ir viena un tā paša veida informācija.
9. ★ Pieraksti, kas notiktu, ja primārā atslēga nebūtu unikāla — dod konkrētu piemēru ar
   diviem ierakstiem.

**Mājasdarbs:** 6. uzdevums

## 11-019 · SELECT un WHERE
`prakse` · `teorija.sql` §3

**Tēma:** Vaicājums `SELECT`. Datu atlase ar `WHERE`.
**SR:** Uzraksta vaicājumu, kas atlasa noteiktus laukus un ierakstus.
**Standarts:** T.V.2.3.7.

**Gaita**
- 5' — vaicājums ir jautājums datubāzei, nevis programma
- 10' — demo §3: `SELECT ... FROM ... WHERE ...`
- 20' — uzdevumi w3schools redaktorā
- 5' — kāpēc `SELECT *` ir ērts, bet ne vienmēr labs

**Uzdevumi**
10. Izvadi visus produktus.
11. Izvadi tikai produktu nosaukumus un cenas.
12. Izvadi produktus, kuru cena ir lielāka par 50.
13. Izvadi klientus no Vācijas.
14. Izvadi darbiniekus, kas dzimuši pirms 1960. gada.
15. ★ Izvadi produktus, kuru cena ir tieši 18 vai 19, neizmantojot `OR`.

**Mājasdarbs:** 13. uzdevums

## 11-020 · Kārtošana un ierobežošana
`prakse` · `teorija.sql` §4

**Tēma:** `ORDER BY`, `LIMIT`, `DISTINCT`.
**SR:** Sakārto un ierobežo vaicājuma rezultātu.
**Standarts:** T.V.2.3.7.

**Gaita**
- 5' — atkārtojums: kārtošana Python un kārtošana datubāzē
- 10' — demo §4: `ASC`/`DESC`, vairāki lauki, `LIMIT`, `DISTINCT`
- 20' — uzdevumi
- 5' — kāpēc kārtošana datubāzē ir ātrāka par kārtošanu programmā

**Uzdevumi**
16. Izvadi produktus, sakārtotus pēc cenas dilstoši.
17. Izvadi piecus dārgākos produktus.
18. Izvadi klientus, sakārtotus pēc valsts, tad pēc pilsētas.
19. Izvadi visas valstis, kurās ir klienti, katru vienu reizi.
20. ★ Izvadi produktu, kura cena ir otrā augstākā.

**Mājasdarbs:** 18. uzdevums

## 11-021 · Salikti nosacījumi
`prakse` · `teorija.sql` §5

**Tēma:** `AND`, `OR`, `IN`, `BETWEEN`, `LIKE`, `NULL`.
**SR:** Veido saliktus atlases nosacījumus un meklē tekstā.
**Standarts:** T.V.2.3.7.

**Gaita**
- 5' — atkārtojums no 10. klases: loģiskie operatori
- 10' — demo §5: `LIKE` šabloni, `IS NULL` un kāpēc `= NULL` nestrādā
- 20' — uzdevumi
- 5' — `%` un `_` atšķirība

**Uzdevumi**
21. Izvadi produktus, kuru cena ir no 20 līdz 40.
22. Izvadi klientus no Vācijas vai Francijas, izmantojot `IN`.
23. Izvadi klientus, kuru nosaukums sākas ar burtu «A».
24. Izvadi klientus, kuru nosaukumā ir vārds «Market».
25. Izvadi ierakstus, kuriem kāds lauks ir tukšs (`NULL`).
26. ★ Izvadi klientus, kuru pasta indekss sākas ar cipariem un ir tieši 5 simbolus garš.

**Mājasdarbs:** 23. uzdevums

## 11-022 · Agregātfunkcijas
`prakse` · `teorija.sql` §6

**Tēma:** `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
**SR:** Aprēķina kopsavilkuma vērtības no daudziem ierakstiem.
**Standarts:** T.V.2.3.7. · T.V.2.3.5.

**Gaita**
- 5' — «cik» un «vidēji» — jautājumi, uz kuriem viens ieraksts neatbild
- 10' — demo §6: piecas funkcijas, `AS` rezultāta nosaukšanai
- 20' — uzdevumi
- 5' — `COUNT(*)` pret `COUNT(lauks)` — kāda atšķirība ar NULL

**Uzdevumi**
27. Cik pavisam ir produktu?
28. Kāda ir vidējā produkta cena?
29. Kāda ir lētākā un dārgākā produkta cena vienā vaicājumā?
30. Cik klientu ir no Vācijas?
31. Kāda ir visu produktu kopējā vērtība noliktavā?
32. ★ Cik produktu cena ir virs vidējās? _Norāde: vaicājums vaicājumā._

**Mājasdarbs:** 29. uzdevums

## 11-023 · GROUP BY
`prakse` · FV3 (dators) · `teorija.sql` §7

**Tēma:** Grupēšana ar `GROUP BY` un filtrēšana ar `HAVING`.
**SR:** Sagrupē ierakstus pēc lauka un aprēķina kopsavilkumu katrai grupai.
**Standarts:** T.V.2.3.7.

**Gaita**
- 5' — «cik produktu katrā kategorijā» — viena skaitļa vietā tabula
- 10' — demo §7: `GROUP BY`, `HAVING`, un ar ko tas atšķiras no `WHERE`
- 15' — uzdevumi
- 10' — **FV3** pie datora

**Uzdevumi**
33. Cik produktu ir katrā kategorijā?
34. Cik klientu ir katrā valstī, sakārtots dilstoši?
35. Kāda ir vidējā cena katrā kategorijā?
36. Izvadi tikai tās valstis, kurās ir vairāk nekā pieci klienti.
37. ★ Izvadi katra piegādātāja produktu skaitu un vidējo cenu, sakārtotu pēc skaita.

**Mājasdarbs:** 34. uzdevums

## 11-024 · Relācijas
`jaukta` · `teorija.sql` §8

**Tēma:** Saistītas tabulas. Ārējā atslēga. Saistību veidi 1:1, 1:N, N:M.
**SR:** Atpazīst tabulu saistības un skaidro, kāpēc dati ir sadalīti vairākās tabulās.
**Standarts:** T.O.2.3.4.

**Gaita**
- 10' — kāpēc pasūtījumā neglabā klienta adresi, bet gan klienta `id`
- 10' — demo §8: ārējā atslēga, 1:N; kur w3schools datubāzē tā ir
- 15' — uzdevumi burtnīcā
- 5' — N:M un starptabula — kur to redzam (`OrderDetails`)

**Uzdevumi**
38. Burtnīcā: uzzīmē w3schools tabulu `Products`, `Categories` un `Suppliers` saistības.
39. Burtnīcā: pieraksti, kāda saistība ir starp `Orders` un `Customers` — 1:1, 1:N vai N:M.
40. Burtnīcā: dotajam aprakstam «skolēni un pulciņi» nosaki saistības veidu un pamato.
41. ★ Burtnīcā: uzzīmē shēmu skolas bibliotēkai, kur viena grāmata var būt izsniegta daudzas
    reizes dažādiem skolēniem.

**Mājasdarbs:** 40. uzdevums

## 11-025 · INNER JOIN
`prakse` · `teorija.sql` §9

**Tēma:** Tabulu savienošana ar `INNER JOIN`.
**SR:** Savieno divas tabulas un izvada datus no abām.
**Standarts:** T.V.2.3.7.

**Gaita**
- 5' — «rādi produktu un tā kategorijas nosaukumu» — divās tabulās
- 10' — demo §9: `JOIN ... ON`, tabulu aizstājvārdi
- 20' — uzdevumi
- 5' — kas notiek, ja aizmirst `ON`

**Uzdevumi**
42. Izvadi produktu nosaukumus kopā ar to kategoriju nosaukumiem.
43. Izvadi pasūtījumus kopā ar klienta nosaukumu.
44. Izvadi produktus kopā ar piegādātāja nosaukumu un valsti.
45. Izvadi pasūtījumus kopā ar darbinieka vārdu un uzvārdu.
46. ★ Izvadi produktus ar kategoriju un piegādātāju — trīs tabulas vienā vaicājumā.

**Mājasdarbs:** 43. uzdevums

## 11-026 · LEFT JOIN un grupēšana pār tabulām
`prakse` · `teorija.sql` §10

**Tēma:** `LEFT JOIN`. Agregātfunkcijas pār savienotām tabulām.
**SR:** Izvēlas piemērotu savienojuma veidu un aprēķina kopsavilkumu pār vairākām tabulām.
**Standarts:** T.V.2.3.7.

**Gaita**
- 5' — kā izvadīt arī tos klientus, kuriem nav neviena pasūtījuma?
- 10' — demo §10: `LEFT JOIN`, `NULL` rezultātā, `COUNT` ar savienojumu
- 20' — uzdevumi
- 5' — kad `INNER`, kad `LEFT`

**Uzdevumi**
47. Izvadi visus klientus un to pasūtījumu skaitu, arī tos, kuriem pasūtījumu nav.
48. Izvadi katras kategorijas produktu skaitu, izmantojot savienojumu.
49. Izvadi darbiniekus un cik pasūtījumu katrs apstrādājis, sakārtotus dilstoši.
50. Izvadi produktus, kas nekad nav pasūtīti.
51. ★ Izvadi katra klienta kopējo pasūtījumu summu, izmantojot `OrderDetails`.

**Mājasdarbs:** 49. uzdevums

## 11-027 · Datubāzes plānošana
`jaukta` · `teorija.sql` §11

**Tēma:** No apraksta uz datubāzes shēmu.
**SR:** Izplāno datubāzi ar vairākām saistītām tabulām atbilstoši uzdevuma aprakstam.
**Standarts:** T.O.2.3.4.

**Gaita**
- 10' — soļi: atrodi lietas → atrodi to īpašības → atrodi saistības
- 15' — kopīgi uz tāfeles: sporta kluba sistēma
- 10' — uzdevumi burtnīcā
- 5' — kāpēc vienu un to pašu informāciju negrib glabāt divās vietās

**Uzdevumi**
52. Burtnīcā: izplāno datubāzi skolas ēdnīcai (ēdieni, pasūtījumi, skolēni).
53. Burtnīcā: izplāno datubāzi mūzikas bibliotēkai (izpildītāji, albumi, dziesmas).
54. Burtnīcā: atrodi savā shēmā vietu, kur dati atkārtojas, un izlabo to.
55. ★ Burtnīcā: izplāno datubāzi, kurā ir N:M saistība, un pieraksti starptabulas laukus.

**Mājasdarbs:** 53. uzdevums

## 11-028 · CREATE TABLE
`prakse` · `teorija.sql` §12

**Tēma:** Tabulu izveide. Datu tipi un ierobežojumi.
**SR:** Izveido tabulas ar primārajām un ārējām atslēgām DB Browser for SQLite vidē.
**Standarts:** T.O.2.3.4.

**Gaita**
- 5' — DB Browser: jaunas datubāzes izveide
- 10' — demo §12: `CREATE TABLE`, `PRIMARY KEY`, `NOT NULL`, `REFERENCES`
- 20' — uzdevumi
- 5' — saglabā `.db` failu un `.sql` skriptu repozitorijā

**Uzdevumi**
56. Izveido tabulu `skoleni` ar id, vārdu, klasi un e-pastu.
57. Izveido tabulu `pulcini` un tabulu `dalibnieki`, kas tās saista.
58. Realizē savu 11-027 53. uzdevuma shēmu ar `CREATE TABLE`.
59. Saglabā izveides skriptu datnē `shema.sql` savā repozitorijā.
60. ★ Pievieno ierobežojumu, kas neļauj vienu skolēnu pierakstīt vienā pulciņā divreiz.

**Mājasdarbs:** 58. uzdevums

## 11-029 · Datu pievienošana un maiņa
`prakse` · FV4 (papīrs) · `teorija.sql` §13

**Tēma:** `INSERT`, `UPDATE`, `DELETE`.
**SR:** Pievieno, maina un dzēš ierakstus, saprotot izmaiņu neatgriezeniskumu.
**Standarts:** T.O.2.3.4. · T.V.2.3.5.

**Gaita**
- 15' — **FV4** uz papīra, datori vēl aizvērti
- 10' — demo §13: `INSERT`, `UPDATE ... WHERE`, `DELETE ... WHERE`
- 15' — uzdevumi

**Uzdevumi**
61. Ievieto savā tabulā piecus ierakstus.
62. Nomaini viena ieraksta vērtību.
63. Dzēs vienu ierakstu pēc nosacījuma.
64. Pieraksti, kas notiek, ja `UPDATE` izpilda bez `WHERE`. Izmēģini uz testa tabulas.
65. ★ Uzraksti vaicājumu, kas paaugstina visas cenas par 10 %, bet tikai vienā kategorijā.

**Mājasdarbs:** 62. uzdevums

## 11-030 · Datu integritāte
`jaukta` · `teorija.sql` §14

**Tēma:** Datu validācija un integritāte datubāzē.
**SR:** Skaidro, kā ierobežojumi pasargā datus, un pievieno tos savai tabulai.
**Standarts:** T.V.2.3.5. · T.O.2.3.4.

**Gaita**
- 10' — kas notiek, ja izdzēš klientu, kuram ir pasūtījumi?
- 10' — demo §14: `NOT NULL`, `UNIQUE`, `CHECK`, ārējās atslēgas ierobežojums
- 15' — uzdevumi
- 5' — kur validēt: datubāzē, serverī vai pārlūkā? Atbilde: visur

**Uzdevumi**
66. Pievieno savai tabulai `NOT NULL` un `UNIQUE` ierobežojumus un pārbaudi tos.
67. Pievieno `CHECK`, kas neļauj negatīvu cenu.
68. Izmēģini dzēst ierakstu, uz kuru norāda cita tabula, un pieraksti rezultātu.
69. ★ Pieraksti, kuras trīs pārbaudes tavā 06. bloka projektā būs datubāzē un kuras — kodā.

**Mājasdarbs:** 66. uzdevums

## 11-031 · Atkārtojums un biļešu izmēģinājums
`jaukta`

**Tēma:** Datubāzes un SQL: atkārtojums. Gatavošanās biļetēm.
**SR:** Atkārto bloka jēdzienus un vingrinās mutiski pamatot savu vaicājumu.
**Standarts:** viss bloks

**Gaita**
- 10' — kopīgi: `WHERE` pret `HAVING`, `INNER` pret `LEFT`, ko dara `GROUP BY`
- 20' — pāros: viens velk izmēģinājuma biļeti, otrs klausās un jautā; tad maina vietām
- 10' — biežākās kļūdas un ko darīt, ja vaicājums nestrādā

**Uzdevumi**
70. Velc izmēģinājuma biļeti un atbildi uz to sola biedram.
71. Uzraksti vaicājumu, kas apvieno `JOIN`, `GROUP BY` un `ORDER BY`.
72. Pieraksti savā valodā, ko dara katrs no pieciem dotajiem vaicājumiem.
73. ★ Dots vaicājums ar kļūdu — atrodi to, nepalaižot.

**Mājasdarbs:** gatavoties SV2

## 11-032 · Pārbaudes darbs
`pārbaudes darbs`

**Tēma:** Pārbaudes darbs: datubāzes plānošana un SQL vaicājumi.
**SR:** Demonstrē bloka sasniedzamos rezultātus, aizstāvot atbildi mutiski.
**Standarts:** viss bloks

**Gaita**
- 40' — biļetes: katrs velk biļeti ar diviem uzdevumiem, sagatavojas 10 min, atbild 5 min

**Materiāli:** SV2 — biļešu kopums (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **w3schools nav kompromiss, bet izvēle.** Tā ir vienīgā vietne, ko atļauj centralizētais
  eksāmens, un tur nav jāuzstāda nekas. Vaicājumus mācāmies tur; savu datubāzi veidojam DB
  Browser vidē, kas eksāmenā arī ir atļauta. Tā skolēns visu gadu strādā eksāmena rīkos.
- **`WHERE` pret `HAVING`** ir vieta, kur klase apjuks. Vienkāršais skaidrojums: `WHERE`
  atsijā ierakstus **pirms** grupēšanas, `HAVING` — grupas **pēc** tās.
- **Biļetes, nevis rakstisks darbs.** SQL vaicājumu var uzrakstīt un tūlīt pamatot mutiski —
  «kāpēc te `LEFT`, nevis `INNER`». Tas parāda izpratni daudz precīzāk nekā pareizs rezultāts.
- **Šis bloks ir tiešs ieguldījums 06. blokā un 12. klasē.** Gala projekta datu modelis nāk
  no 11-027, un centralizētajā eksāmenā datubāzes daļa ir 17 %.
