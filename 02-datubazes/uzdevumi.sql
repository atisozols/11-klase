-- ==========================================================
-- 02. DATUBĀZES UN SQL — DARBA FAILS
-- ==========================================================
-- Šeit raksti savus risinājumus.
-- Teorija, piemēri un atgādne: teorija.sql
-- Uzdevumu numuri iet cauri visam blokam.
-- ==========================================================


-- ----------------------------------------------------------
-- 11-017 · Kāpēc datubāze
-- ----------------------------------------------------------

-- 1. Burtnīcā: uzskaiti trīs problēmas, kas rodas, glabājot skolas datus CSV datnēs.




-- 2. Burtnīcā: dotajam CSV fragmentam pieraksti, kā izskatītos atbilstoša tabula — kādi lauki
--    un kāda tipa dati.




-- 3. Burtnīcā: pieraksti, kuri dati skolas sistēmā atkārtojas un tāpēc būtu jāglabā atsevišķi.




-- 4. ★ Atrodi savā 10. klases projektā vietu, kur datubāze būtu bijusi ērtāka par datni.





-- ----------------------------------------------------------
-- 11-018 · Tabula un datu tipi
-- ----------------------------------------------------------

-- 5. Aplūko w3schools datubāzes tabulu Products un pieraksti katra lauka datu tipu.




-- 6. Dotajam aprakstam «skolas pulciņi» pieraksti lauku sarakstu ar datu tipiem.




-- 7. Pieraksti, kurš lauks katrā no trim dotajām tabulām būtu primārā atslēga un kāpēc.




-- 8. Atrodi w3schools datubāzē divas tabulas, kurās ir viena un tā paša veida informācija.




-- 9. ★ Pieraksti, kas notiktu, ja primārā atslēga nebūtu unikāla — dod konkrētu piemēru ar
--    diviem ierakstiem.





-- ----------------------------------------------------------
-- 11-019 · SELECT un WHERE
-- ----------------------------------------------------------

-- 10. Izvadi visus produktus.




-- 11. Izvadi tikai produktu nosaukumus un cenas.




-- 12. Izvadi produktus, kuru cena ir lielāka par 50.




-- 13. Izvadi klientus no Vācijas.




-- 14. Izvadi darbiniekus, kas dzimuši pirms 1960. gada.




-- 15. ★ Izvadi produktus, kuru cena ir tieši 18 vai 19, neizmantojot OR.





-- ----------------------------------------------------------
-- 11-020 · Kārtošana un ierobežošana
-- ----------------------------------------------------------

-- 16. Izvadi produktus, sakārtotus pēc cenas dilstoši.




-- 17. Izvadi piecus dārgākos produktus.




-- 18. Izvadi klientus, sakārtotus pēc valsts, tad pēc pilsētas.




-- 19. Izvadi visas valstis, kurās ir klienti, katru vienu reizi.




-- 20. ★ Izvadi produktu, kura cena ir otrā augstākā.





-- ----------------------------------------------------------
-- 11-021 · Salikti nosacījumi
-- ----------------------------------------------------------

-- 21. Izvadi produktus, kuru cena ir no 20 līdz 40.




-- 22. Izvadi klientus no Vācijas vai Francijas, izmantojot IN.




-- 23. Izvadi klientus, kuru nosaukums sākas ar burtu «A».




-- 24. Izvadi klientus, kuru nosaukumā ir vārds «Market».




-- 25. Izvadi ierakstus, kuriem kāds lauks ir tukšs (NULL).




-- 26. ★ Izvadi klientus, kuru pasta indekss sākas ar cipariem un ir tieši 5 simbolus garš.





-- ----------------------------------------------------------
-- 11-022 · Agregātfunkcijas
-- ----------------------------------------------------------

-- 27. Cik pavisam ir produktu?




-- 28. Kāda ir vidējā produkta cena?




-- 29. Kāda ir lētākā un dārgākā produkta cena vienā vaicājumā?




-- 30. Cik klientu ir no Vācijas?




-- 31. Kāda ir visu produktu kopējā vērtība noliktavā?




-- 32. ★ Cik produktu cena ir virs vidējās? Norāde: vaicājums vaicājumā.





-- ----------------------------------------------------------
-- 11-023 · GROUP BY
-- ----------------------------------------------------------

-- 33. Cik produktu ir katrā kategorijā?




-- 34. Cik klientu ir katrā valstī, sakārtots dilstoši?




-- 35. Kāda ir vidējā cena katrā kategorijā?




-- 36. Izvadi tikai tās valstis, kurās ir vairāk nekā pieci klienti.




-- 37. ★ Izvadi katra piegādātāja produktu skaitu un vidējo cenu, sakārtotu pēc skaita.





-- ----------------------------------------------------------
-- 11-024 · Relācijas
-- ----------------------------------------------------------

-- 38. Burtnīcā: uzzīmē w3schools tabulu Products, Categories un Suppliers saistības.




-- 39. Burtnīcā: pieraksti, kāda saistība ir starp Orders un Customers — 1:1, 1:N vai N:M.




-- 40. Burtnīcā: dotajam aprakstam «skolēni un pulciņi» nosaki saistības veidu un pamato.




-- 41. ★ Burtnīcā: uzzīmē shēmu skolas bibliotēkai, kur viena grāmata var būt izsniegta daudzas
--    reizes dažādiem skolēniem.





-- ----------------------------------------------------------
-- 11-025 · INNER JOIN
-- ----------------------------------------------------------

-- 42. Izvadi produktu nosaukumus kopā ar to kategoriju nosaukumiem.




-- 43. Izvadi pasūtījumus kopā ar klienta nosaukumu.




-- 44. Izvadi produktus kopā ar piegādātāja nosaukumu un valsti.




-- 45. Izvadi pasūtījumus kopā ar darbinieka vārdu un uzvārdu.




-- 46. ★ Izvadi produktus ar kategoriju un piegādātāju — trīs tabulas vienā vaicājumā.





-- ----------------------------------------------------------
-- 11-026 · LEFT JOIN un grupēšana pār tabulām
-- ----------------------------------------------------------

-- 47. Izvadi visus klientus un to pasūtījumu skaitu, arī tos, kuriem pasūtījumu nav.




-- 48. Izvadi katras kategorijas produktu skaitu, izmantojot savienojumu.




-- 49. Izvadi darbiniekus un cik pasūtījumu katrs apstrādājis, sakārtotus dilstoši.




-- 50. Izvadi produktus, kas nekad nav pasūtīti.




-- 51. ★ Izvadi katra klienta kopējo pasūtījumu summu, izmantojot OrderDetails.





-- ----------------------------------------------------------
-- 11-027 · Datubāzes plānošana
-- ----------------------------------------------------------

-- 52. Burtnīcā: izplāno datubāzi skolas ēdnīcai (ēdieni, pasūtījumi, skolēni).




-- 53. Burtnīcā: izplāno datubāzi mūzikas bibliotēkai (izpildītāji, albumi, dziesmas).




-- 54. Burtnīcā: atrodi savā shēmā vietu, kur dati atkārtojas, un izlabo to.




-- 55. ★ Burtnīcā: izplāno datubāzi, kurā ir N:M saistība, un pieraksti starptabulas laukus.





-- ----------------------------------------------------------
-- 11-028 · CREATE TABLE
-- ----------------------------------------------------------

-- 56. Izveido tabulu skoleni ar id, vārdu, klasi un e-pastu.




-- 57. Izveido tabulu pulcini un tabulu dalibnieki, kas tās saista.




-- 58. Realizē savu 11-027 53. uzdevuma shēmu ar CREATE TABLE.




-- 59. Saglabā izveides skriptu datnē shema.sql savā repozitorijā.




-- 60. ★ Pievieno ierobežojumu, kas neļauj vienu skolēnu pierakstīt vienā pulciņā divreiz.





-- ----------------------------------------------------------
-- 11-029 · Datu pievienošana un maiņa
-- ----------------------------------------------------------

-- 61. Ievieto savā tabulā piecus ierakstus.




-- 62. Nomaini viena ieraksta vērtību.




-- 63. Dzēs vienu ierakstu pēc nosacījuma.




-- 64. Pieraksti, kas notiek, ja UPDATE izpilda bez WHERE. Izmēģini uz testa tabulas.




-- 65. ★ Uzraksti vaicājumu, kas paaugstina visas cenas par 10 %, bet tikai vienā kategorijā.





-- ----------------------------------------------------------
-- 11-030 · Datu integritāte
-- ----------------------------------------------------------

-- 66. Pievieno savai tabulai NOT NULL un UNIQUE ierobežojumus un pārbaudi tos.




-- 67. Pievieno CHECK, kas neļauj negatīvu cenu.




-- 68. Izmēģini dzēst ierakstu, uz kuru norāda cita tabula, un pieraksti rezultātu.




-- 69. ★ Pieraksti, kuras trīs pārbaudes tavā 06. bloka projektā būs datubāzē un kuras — kodā.





-- ----------------------------------------------------------
-- 11-031 · Atkārtojums un biļešu izmēģinājums
-- ----------------------------------------------------------

-- 70. Velc izmēģinājuma biļeti un atbildi uz to sola biedram.




-- 71. Uzraksti vaicājumu, kas apvieno JOIN, GROUP BY un ORDER BY.




-- 72. Pieraksti savā valodā, ko dara katrs no pieciem dotajiem vaicājumiem.




-- 73. ★ Dots vaicājums ar kļūdu — atrodi to, nepalaižot.
