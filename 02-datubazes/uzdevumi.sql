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

-- 5. Atver skola.db ar DB Browser un pieraksti, cik ierakstu ir katrā no septiņām tabulām.




-- 6. Pieraksti katra skoleni tabulas lauka datu tipu un paskaidro, kāpēc tieši tāds.




-- 7. Kurš lauks katrā tabulā ir primārā atslēga? Kāpēc vards par to nederētu?




-- 8. Atrodi tabulas, kurās ir lauks, kas norāda uz citu tabulu. Pieraksti visus pārus.




-- 9. ★ Pieraksti, kas notiktu, ja skoleni.id nebūtu unikāls — dod konkrētu piemēru ar diviem
--    ierakstiem un vienu atzīmi.





-- ----------------------------------------------------------
-- 11-019 · SELECT un WHERE
-- ----------------------------------------------------------

-- 10. Izvadi visus skolēnus.




-- 11. Izvadi tikai skolēnu vārdus un uzvārdus.




-- 12. Izvadi skolēnus, kas dzimuši pirms 2009. gada.




-- 13. Izvadi to priekšmetu nosaukumus, kurus māca skolotājs ar id 3.




-- 14. Izvadi visas atzīmes, kas ir 10.




-- 15. ★ Izvadi skolēnus, kuru id ir tieši 5 vai 12, neizmantojot OR.





-- ----------------------------------------------------------
-- 11-020 · Kārtošana un ierobežošana
-- ----------------------------------------------------------

-- 16. Izvadi skolēnus, sakārtotus pēc uzvārda alfabētiski.




-- 17. Izvadi 10 jaunākos skolēnus.




-- 18. Izvadi skolēnus, sakārtotus pēc dzimšanas gada dilstoši, tad pēc uzvārda.




-- 19. Izvadi visus dažādos dzimšanas gadus, katru vienu reizi.




-- 20. ★ Izvadi piecas jaunākās atzīmes, sakārtotas pēc datuma.





-- ----------------------------------------------------------
-- 11-021 · Salikti nosacījumi
-- ----------------------------------------------------------

-- 21. Izvadi skolēnus, kas dzimuši no 2008. līdz 2010. gadam.




-- 22. Izvadi pulciņus, kas notiek otrdienā vai trešdienā, izmantojot IN.




-- 23. Izvadi skolēnus, kuru uzvārds sākas ar burtu «K».




-- 24. Izvadi skolēnus, kuru uzvārdā ir «ozol».




-- 25. Izvadi skolēnus, kuriem nav norādīts e-pasts.




-- 26. ★ Izvadi skolēnus, kuru vārda otrais burts ir «n».





-- ----------------------------------------------------------
-- 11-022 · Agregātfunkcijas
-- ----------------------------------------------------------

-- 27. Cik pavisam ir skolēnu?




-- 28. Kāda ir vidējā atzīme visā skolā, noapaļota līdz diviem cipariem?




-- 29. Kāda ir zemākā un augstākā atzīme vienā vaicājumā?




-- 30. Cik skolēniem nav norādīts e-pasts?




-- 31. Cik pavisam ir izliktas atzīmes?




-- 32. ★ Cik skolēnu ir dzimuši visbiežāk sastopamajā dzimšanas gadā?





-- ----------------------------------------------------------
-- 11-023 · GROUP BY
-- ----------------------------------------------------------

-- 33. Cik skolēnu ir katrā klasē?




-- 34. Kāda ir vidējā atzīme katrā priekšmetā, sakārtota dilstoši?




-- 35. Cik atzīmju ir katram skolēnam?




-- 36. Izvadi tikai tos skolēnus, kuriem ir vairāk nekā 20 atzīmes.




-- 37. ★ Izvadi vidējo atzīmi katrā priekšmetā, rēķinot tikai atzīmes, kas izliktas no oktobra.





-- ----------------------------------------------------------
-- 11-024 · Relācijas
-- ----------------------------------------------------------

-- 38. Burtnīcā: uzzīmē skoleni, klases un skolotaji saistības ar bultiņām.




-- 39. Burtnīcā: kāda saistība ir starp skoleni un pulcini — 1:1, 1:N vai N:M? Pamato.




-- 40. Burtnīcā: kāpēc atzimes ir atsevišķa tabula, nevis lauki skoleni tabulā?




-- 41. ★ Burtnīcā: uzzīmē shēmu skolas bibliotēkai, kur viena grāmata var būt izsniegta daudzas
--    reizes dažādiem skolēniem.





-- ----------------------------------------------------------
-- 11-025 · INNER JOIN
-- ----------------------------------------------------------

-- 42. Izvadi skolēnu vārdus, uzvārdus un viņu klases nosaukumu.




-- 43. Izvadi priekšmetus kopā ar skolotāja vārdu un uzvārdu.




-- 44. Izvadi visas skolēna ar id 5 atzīmes kopā ar priekšmeta nosaukumu.




-- 45. Izvadi pulciņus kopā ar vadītāja vārdu un uzvārdu.




-- 46. ★ Izvadi skolēna vārdu, priekšmeta nosaukumu un atzīmi — trīs tabulas vienā vaicājumā.





-- ----------------------------------------------------------
-- 11-026 · LEFT JOIN un grupēšana pār tabulām
-- ----------------------------------------------------------

-- 47. Izvadi visus skolēnus un viņu atzīmju skaitu, arī tos, kuriem atzīmju nav.




-- 48. Izvadi skolēnus, kuriem nav nevienas atzīmes.




-- 49. Izvadi katra pulciņa dalībnieku skaitu, arī tiem pulciņiem, kuros dalībnieku nav.




-- 50. Izvadi katras klases skolēnu vidējo atzīmi, sakārtotu dilstoši.




-- 51. ★ Izvadi katram skolēnam, cik pulciņos viņš piedalās, un izceļ tos, kas piedalās vairāk
--    nekā vienā.





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

-- 56. Izveido jaunu datubāzi mans.db un tajā tabulu biedri ar id, vārdu, uzvārdu un e-pastu.




-- 57. Pievieno tabulu treninu_veidi un starptabulu pieteikumi, kas tās saista.




-- 58. Realizē savu 53. uzdevuma shēmu ar CREATE TABLE.




-- 59. Saglabā izveides skriptu datnē shema.sql savā repozitorijā.




-- 60. ★ Pievieno ierobežojumu, kas neļauj vienu biedru pieteikt vienam treniņam divreiz.





-- ----------------------------------------------------------
-- 11-029 · Datu pievienošana un maiņa
-- ----------------------------------------------------------

-- 61. Ievieto savā tabulā biedri piecus ierakstus.




-- 62. Nomaini viena biedra e-pastu.




-- 63. Dzēs vienu ierakstu pēc nosacījuma.




-- 64. Pieraksti, kas notiek, ja UPDATE izpilda bez WHERE. Izmēģini uz savas mans.db,
--    nevis uz skola.db.




-- 65. ★ Uzraksti vaicājumu, kas visiem viena pulciņa dalībniekiem nomaina pieteikšanās datumu.





-- ----------------------------------------------------------
-- 11-030 · Datu integritāte
-- ----------------------------------------------------------

-- 66. Pievieno savai tabulai NOT NULL un UNIQUE ierobežojumus un pārbaudi, ka tie strādā.




-- 67. Pievieno CHECK, kas neļauj negatīvu treniņa ilgumu.




-- 68. Mēģini ievietot skola.db atzīmi ar vērtību 15 un pieraksti, kas notiek un kāpēc.




-- 69. ★ Pieraksti, kuras trīs pārbaudes tavā 06. bloka projektā būs datubāzē un kuras — kodā.





-- ----------------------------------------------------------
-- 11-031 · Atkārtojums un biļešu izmēģinājums
-- ----------------------------------------------------------

-- 70. Velc izmēģinājuma biļeti un atbildi uz to sola biedram.




-- 71. Uzraksti vaicājumu, kas apvieno JOIN, GROUP BY un ORDER BY.




-- 72. Pieraksti savā valodā, ko dara katrs no pieciem dotajiem vaicājumiem.




-- 73. ★ Dots vaicājums ar kļūdu — atrodi to, nepalaižot.
