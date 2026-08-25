# 06. Gala projekts: pilns cikls un ieviešana

**24 stundas (11-077 – 11-100)** · Standarta 6. temats “Kā īstenot risinājumu?”

**Bloka mērķis:** izstrādāt, notestēt, publicēt un prezentēt risinājumu pēc savas
specifikācijas, ejot cauri visiem programmatūras izstrādes posmiem.

**Darba uzdevums:** tava paša specifikācija no 04. bloka.
**Ceļvedis:** [`projekts.md`](projekts.md) · **Noslēgums:** SV6 — demonstrācija un
aizstāvēšana (11-099, 11-100)

> Specifikācijai jābūt **apstiprinātai** pirms 11-077. Ja tā nav, pirmā stunda paiet, to
> sakārtojot.

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 06-projekts/README.md && python3 bin/darbafails.py 06-projekts -->

| Nr. | Tēma | Sasniedzamais rezultāts |
| --- | --- | --- |
| 11-077 | No specifikācijas uz darba plānu. Repozitorija sagatavošana. | Sagatavo projekta repozitoriju un pārbauda, ka specifikācija ir izpildāma. |
| 11-078 | Projekta datubāzes izveide. | Izveido projekta datubāzi ar visām tabulām un saistībām. |
| 11-079 | Servera izveide un datu izgūšana. | Izveido serveri, kas atgriež datus no projekta datubāzes. |
| 11-080 | `POST` maršruti un validācija. | Pieņem un pārbauda lietotāja datus serverī. |
| 11-081 | Klienta puses izveide. Datu attēlošana. | Izveido lapu, kas attēlo datus no sava servera. |
| 11-082 | Datu ievade no klienta puses. | Izveido formu, kas nosūta datus serverim un atsvaidzina skatu. |
| 11-083 | Projekta izstrāde pēc plāna. | Realizē nākamās specifikācijas prasības. |
| 11-084 | Starpposma demonstrācija un atgriezeniskā saite. | Demonstrē paveikto un sniedz citiem konkrētu atgriezenisko saiti. |
| 11-085 | Uzlabojumi pēc atgriezeniskās saites. | Ievieš uzlabojumus un pārbauda tos. |
| 11-086 | Projekta izstrāde. | Realizē atlikušās galvenās prasības. |
| 11-087 | Projekta izstrāde. | Pabeidz obligāto funkcionalitāti. |
| 11-088 | Koda strukturēšana un labās prakses principi. | Sakārto kodu: sadala failos, izmet lieko, pievieno komentārus. |
| 11-089 | Akcepttestēšana pret specifikāciju. | Izveido testa plānu, kas pārbauda katru specifikācijas prasību. |
| 11-090 | Testa plāna izpilde. | Izpilda testus un dokumentē rezultātus. |
| 11-091 | Testēšanā atrasto kļūdu novēršana. | Novērš kļūdas un atkārtoti izpilda attiecīgos testus. |
| 11-092 | Otrā demonstrācija. Gatavības izvērtējums. | Demonstrē gandrīz gatavu risinājumu un plāno atlikušo darbu. |
| 11-093 | Minimālās drošības prasības. | Pārbauda un novērš savas lietotnes drošības trūkumus. |
| 11-094 | Risinājuma ieviešana. Publicēšana internetā. | Publicē savu risinājumu publiski pieejamā vietā. |
| 11-095 | Lietotāja ceļvedis un projekta dokumentācija. | Uzraksta lietotājam saprotamu pamācību un projekta aprakstu. |
| 11-096 | Licences izvēle. Intelektuālā īpašuma aizsardzība. | Izvēlas savam projektam licenci un pamato izvēli. |
| 11-097 | Projekta prezentācijas sagatavošana. | Sagatavo demonstrāciju, kas parāda problēmu, risinājumu un izstrādes gaitu. |
| 11-098 | Pēdējie labojumi un pašpārbaude. | Pabeidz projektu un pārbauda tā atbilstību specifikācijai. |
| 11-099 | Projekta demonstrācija un aizstāvēšana. | Demonstrē risinājumu un pamato izstrādes laikā pieņemtos lēmumus. |
| 11-100 | Projekta aizstāvēšana. Kursa noslēgums. | Demonstrē risinājumu; reflektē par divos gados apgūto. |

<!-- TABULA:BEIGAS -->

---

## 11-077 · Projekta uzsākšana
`jaukta`

**Tēma:** No specifikācijas uz darba plānu. Repozitorija sagatavošana.
**SR:** Sagatavo projekta repozitoriju un pārbauda, ka specifikācija ir izpildāma.
**Standarts:** T.O.2.4.2. · T.V.2.3.8.

**Gaita**
- 10' — 24 stundas: kā tās sadalās; starpposmi 11-084 un 11-092
- 10' — repozitorija struktūra: `serveris/`, `klients/`, `dati/`, dokumentācija
- 15' — uzdevumi
- 5' — pirmais commit

**Uzdevumi**
1. Izveido projekta repozitoriju un ieliec tajā savu `SPECIFIKACIJA.md`.
2. Izveido mapju struktūru un `README.md` ar projekta nosaukumu un vienu teikumu par to.
3. Pārnes savus uzdevumus no 04. bloka GitHub Projects dēļa uz šo repozitoriju.
4. Pārbaudi savu plānu: vai pirmais starpposms ir izpildāms astoņās stundās?
5. ★ Pievieno `.gitignore` ar `node_modules/`, `.env` un `*.db`, ja datubāzi ģenerē skripts.

**Mājasdarbs:** pabeigt sagatavošanu

## 11-078 · Datu modelis
`prakse`

**Tēma:** Projekta datubāzes izveide.
**SR:** Izveido projekta datubāzi ar visām tabulām un saistībām.
**Standarts:** T.O.2.3.4. · T.O.2.4.17.

**Gaita**
- 5' — atkārtojums: shēma no specifikācijas 6. daļas
- 30' — datubāzes izveide un testa datu ievietošana
- 5' — commit

**Stundas beigās:** repozitorijā ir `shema.sql` un datubāze ar vismaz trim testa ierakstiem
katrā tabulā.

**Uzdevumi**
6. Izveido visas tabulas ar primārajām un ārējām atslēgām.
7. Pievieno vismaz trīs testa ierakstus katrā tabulā.
8. Uzraksti skriptu, kas datubāzi izveido no nulles, lai to var atjaunot.
9. ★ Pievieno ierobežojumus (`NOT NULL`, `UNIQUE`, `CHECK`) tur, kur specifikācija to prasa.

**Mājasdarbs:** commit ar paveikto

## 11-079 · Serveris: pirmie maršruti
`prakse`

**Tēma:** Servera izveide un datu izgūšana.
**SR:** Izveido serveri, kas atgriež datus no projekta datubāzes.
**Standarts:** T.O.2.4.11. · T.O.2.4.17.

**Gaita**
- 5' — maršrutu saraksts: kuri būs vajadzīgi
- 30' — izstrāde
- 5' — commit

**Stundas beigās:** serveris palaižas un vismaz viens maršruts atgriež datus no datubāzes.

**Uzdevumi**
10. Uzstādi Express, Knex un `sqlite3` un pieslēdz datubāzi.
11. Izveido vismaz divus `GET` maršrutus.
12. Pārbaudi tos pārlūkā un pieraksti, ko katrs atgriež.
13. ★ Pievieno maršrutu, kas atgriež kopsavilkumu ar `GROUP BY`.

**Mājasdarbs:** commit ar paveikto

## 11-080 · Serveris: datu pievienošana
`prakse`

**Tēma:** `POST` maršruti un validācija.
**SR:** Pieņem un pārbauda lietotāja datus serverī.
**Standarts:** T.O.2.4.17. · T.V.2.3.5.

**Gaita**
- 5' — kuras prasības no specifikācijas šodien tiek izpildītas
- 30' — izstrāde
- 5' — commit

**Stundas beigās:** vismaz viens `POST` maršruts saglabā datus datubāzē un noraida nederīgus.

**Uzdevumi**
14. Izveido vismaz vienu `POST` maršrutu.
15. Pievieno validāciju un atbilstošus statusa kodus.
16. Pārbaudi to ar nederīgiem datiem un pieraksti rezultātu.
17. ★ Pievieno maršrutu datu labošanai vai dzēšanai.

**Mājasdarbs:** commit ar paveikto

## 11-081 · Klients: pirmais ekrāns
`prakse`

**Tēma:** Klienta puses izveide. Datu attēlošana.
**SR:** Izveido lapu, kas attēlo datus no sava servera.
**Standarts:** T.V.2.3.10. · T.O.2.4.11.

**Gaita**
- 5' — atkārtojums: struktūrskice no 04. bloka
- 30' — izstrāde
- 5' — commit

**Stundas beigās:** lapa rāda īstus datus no datubāzes.

**Uzdevumi**
18. Izveido HTML lapu pēc savas struktūrskices.
19. Pievieno `fetch`, kas ielādē datus un attēlo tos.
20. Pievieno CSS, kas sakārto izkārtojumu.
21. ★ Pievieno tukšā stāvokļa paziņojumu: ko lapa rāda, ja datu nav.

**Mājasdarbs:** commit ar paveikto

## 11-082 · Klients: forma
`prakse`

**Tēma:** Datu ievade no klienta puses.
**SR:** Izveido formu, kas nosūta datus serverim un atsvaidzina skatu.
**Standarts:** T.V.2.3.5. · T.O.2.4.11.

**Gaita**
- 35' — izstrāde
- 5' — commit

**Stundas beigās:** lietotājs var pievienot ierakstu caur lapu, un tas parādās sarakstā.

**Uzdevumi**
22. Izveido formu un nosūti datus ar `fetch` un `POST`.
23. Pēc veiksmīgas pievienošanas atsvaidzini sarakstu.
24. Parādi kļūdas paziņojumu, ja serveris atgriež 400.
25. ★ Pievieno pārbaudi arī pārlūka pusē, lai lietotājs uzzina ātrāk.

**Mājasdarbs:** commit ar paveikto

## 11-083 · Izstrāde
`prakse`

**Tēma:** Projekta izstrāde pēc plāna.
**SR:** Realizē nākamās specifikācijas prasības.
**Standarts:** T.O.2.4.2.

**Gaita**
- 35' — izstrāde, individuālas konsultācijas
- 5' — commit un uzdevumu dēļa atjaunināšana

**Stundas beigās:** vismaz viens jauns uzdevums pārvietots uz «Gatavs».

**Uzdevumi**
26. Izpildi nākamos uzdevumus no sava dēļa.
27. ★ Ja esi priekšā plānam, paņem vienu prasību no saraksta «ja paliek laiks».

**Mājasdarbs:** commit ar paveikto

## 11-084 · Pirmais starpposms
`jaukta`

**Tēma:** Starpposma demonstrācija un atgriezeniskā saite.
**SR:** Demonstrē paveikto un sniedz citiem konkrētu atgriezenisko saiti.
**Standarts:** T.V.1.3.2. · Ieradumi

**Gaita**
- 20' — katrs 2 minūtēs parāda, kas strādā
- 15' — atgriezeniskā saite: kas strādā, kas nav skaidrs, ko ieteiktu
- 5' — katrs pieraksta trīs lietas, ko labos

**Uzdevumi**
28. Demonstrē savu projektu un pieraksti saņemtās piezīmes.
29. Salīdzini paveikto ar plānu: vai esi grafikā?
30. Ja neesi, izlem, ko izmetīsi, un pieraksti to specifikācijā.
31. ★ Sniedz vismaz vienam klasesbiedram konkrētu tehnisku ieteikumu.

**Mājasdarbs:** plāna atjaunināšana

## 11-085 · Izstrāde
`prakse` · FV11 (dators)

**Tēma:** Uzlabojumi pēc atgriezeniskās saites.
**SR:** Ievieš uzlabojumus un pārbauda tos.
**Standarts:** T.V.1.3.2.

**Gaita**
- 20' — izstrāde
- 15' — **FV11** pie datora: pašpārbaude pret specifikāciju
- 5' — commit

**Uzdevumi**
32. Ievies vismaz divus uzlabojumus no saņemtajām piezīmēm.
33. Aizpildi pašpārbaudes tabulu: katrai prasībai — izpildīts, daļēji vai nē.
34. ★ Pieraksti, kura prasība izrādījās grūtāka, nekā plānoji, un kāpēc.

**Mājasdarbs:** commit ar paveikto

## 11-086 · Izstrāde
`prakse`

**Tēma:** Projekta izstrāde.
**SR:** Realizē atlikušās galvenās prasības.
**Standarts:** T.O.2.4.2.

**Gaita**
- 35' — izstrāde
- 5' — commit

**Stundas beigās:** visas obligātās funkcionālās prasības ir vismaz uzsāktas.

**Uzdevumi**
35. Turpini pēc sava plāna.
36. ★ Pārbaudi savu kodu: vai kāda funkcija ir garāka par 30 rindām? Sadali to.

**Mājasdarbs:** commit ar paveikto

## 11-087 · Izstrāde
`prakse`

**Tēma:** Projekta izstrāde.
**SR:** Pabeidz obligāto funkcionalitāti.
**Standarts:** T.O.2.4.2.

**Gaita**
- 35' — izstrāde
- 5' — commit

**Stundas beigās:** visas obligātās prasības strādā vismaz pamata līmenī.

**Uzdevumi**
37. Pabeidz obligāto funkcionalitāti.
38. ★ Pievieno kārtošanu vai filtrēšanu, ja specifikācija to paredz.

**Mājasdarbs:** commit ar paveikto

## 11-088 · Koda sakārtošana
`prakse`

**Tēma:** Koda strukturēšana un labās prakses principi.
**SR:** Sakārto kodu: sadala failos, izmet lieko, pievieno komentārus.
**Standarts:** T.O.2.4.8.

**Gaita**
- 10' — kā izskatās projekts, pie kura atgriezīsies pēc mēneša
- 25' — sakārtošana
- 5' — commit

**Uzdevumi**
39. Sadali serveri vairākos failos, ja tas pārsniedz 150 rindas.
40. Izmet aizkomentēto un neizmantoto kodu.
41. Pievieno komentārus vietās, kur risinājums nav acīmredzams.
42. ★ Pārbaudi, vai visi mainīgo un funkciju nosaukumi ir jēgpilni un vienotā stilā.

**Mājasdarbs:** commit ar paveikto

## 11-089 · Testa plāns
`jaukta`

**Tēma:** Akcepttestēšana pret specifikāciju.
**SR:** Izveido testa plānu, kas pārbauda katru specifikācijas prasību.
**Standarts:** T.V.1.3.2. · T.O.2.4.6.

**Gaita**
- 10' — atkārtojums no 10. klases: testa plāna tabula, robežgadījumi
- 25' — testa plāna izveide
- 5' — `TESTI.md` iet repozitorijā

**Uzdevumi**
43. Izveido testa plānu ar vismaz 12 testiem, pa vienam katrai funkcionālajai prasībai.
44. Iekļauj vismaz trīs testus ar nederīgu ievadi.
45. Iekļauj vismaz divus robežgadījumus.
46. ★ Pievieno testu tukšai datubāzei: ko programma rāda, ja datu vēl nav?

**Mājasdarbs:** pabeigt `TESTI.md`

## 11-090 · Testēšana
`prakse`

**Tēma:** Testa plāna izpilde.
**SR:** Izpilda testus un dokumentē rezultātus.
**Standarts:** T.O.2.4.6.

**Gaita**
- 30' — testu izpilde un rezultātu pierakstīšana
- 10' — apmaināmies projektiem un testējam viens otra darbu

**Uzdevumi**
47. Izpildi savu testa plānu un aizpildi faktisko rezultātu kolonnu.
48. Notestē klasesbiedra projektu un uzraksti vismaz divus kļūdas ziņojumus.
49. ★ Atrodi kļūdu, ko tavs testa plāns nepamanīja, un pievieno tai testu.

**Mājasdarbs:** commit ar `TESTI.md`

## 11-091 · Kļūdu labošana
`prakse`

**Tēma:** Testēšanā atrasto kļūdu novēršana.
**SR:** Novērš kļūdas un atkārtoti izpilda attiecīgos testus.
**Standarts:** T.V.1.3.2.

**Gaita**
- 35' — labošana; pēc katras kļūdas tests jāizpilda vēlreiz
- 5' — `TESTI.md` atjaunināšana

**Uzdevumi**
50. Izlabo visas kļūdas, kas atzīmētas kā neizdevušās.
51. Atzīmē `TESTI.md`, kuras kļūdas izlaboji un kuras paliek.
52. ★ Pieraksti, kāpēc kāda kļūda paliek nelabota — tas ir godīgi un normāli.

**Mājasdarbs:** commit ar paveikto

## 11-092 · Otrais starpposms
`jaukta`

**Tēma:** Otrā demonstrācija. Gatavības izvērtējums.
**SR:** Demonstrē gandrīz gatavu risinājumu un plāno atlikušo darbu.
**Standarts:** T.V.1.3.2.

**Gaita**
- 20' — demonstrācijas
- 15' — atgriezeniskā saite ar uzsvaru uz lietojamību
- 5' — atlikušo astoņu stundu plāns

**Uzdevumi**
53. Demonstrē projektu un pieraksti piezīmes.
54. Uzraksti, kas obligāti jāpaspēj atlikušajās stundās.
55. ★ Iedod savu projektu cilvēkam, kas to nekad nav redzējis, un vēro, kur viņš apstājas.

**Mājasdarbs:** plāna atjaunināšana

## 11-093 · Drošība
`jaukta`

**Tēma:** Minimālās drošības prasības.
**SR:** Pārbauda un novērš savas lietotnes drošības trūkumus.
**Standarts:** T.V.3.1.3. · T.O.3.1.3.

**Gaita**
- 10' — trīs jautājumi: vai validācija ir serverī? vai noslēpumi ir ārpus koda? ko rāda kļūda?
- 25' — labošana
- 5' — commit

**Uzdevumi**
56. Pārbaudi, ka visa validācija ir arī servera pusē, ne tikai formā.
57. Pārbaudi, ka `.env` un datubāze nav repozitorijā, ja tajos ir kaut kas privāts.
58. Pārbaudi, ka kļūdas paziņojumos nav SQL vaicājumu vai failu ceļu.
59. ★ Ja tavā projektā ir paroles, pārbaudi, ka tās glabājas kā jaucējvērtības.

**Mājasdarbs:** commit ar paveikto

## 11-094 · Publicēšana
`prakse` · FV12 (dators)

**Tēma:** Risinājuma ieviešana. Publicēšana internetā.
**SR:** Publicē savu risinājumu publiski pieejamā vietā.
**Standarts:** T.O.2.4.2. · T.O.1.1.2.

**Gaita**
- 10' — divi ceļi: GitHub Pages statiskajai daļai, Render serverim
- 20' — publicēšana
- 10' — **FV12** pie datora: pārbaudi, ka publicētā versija tiešām strādā

**Uzdevumi**
60. Publicē savu risinājumu: klienta daļu GitHub Pages vai visu Render bezmaksas kontā.
61. Pārbaudi publicēto versiju no cita datora vai telefona.
62. Pieraksti `README.md` saiti uz publicēto versiju.
63. ★ Pieraksti, kas atšķiras starp lokālo un publicēto versiju un kāpēc.

**Mājasdarbs:** pabeigt publicēšanu

## 11-095 · Dokumentācija
`jaukta`

**Tēma:** Lietotāja ceļvedis un projekta dokumentācija.
**SR:** Uzraksta lietotājam saprotamu pamācību un projekta aprakstu.
**Standarts:** T.O.2.4.7. · T.V.2.3.10.

**Gaita**
- 10' — ko lietotājs grib zināt: kas tas ir, kā sākt, ko var darīt
- 25' — rakstīšana
- 5' — apmaināmies: vai pēc svešas pamācības var lietot programmu?

**Uzdevumi**
64. Uzraksti `README.md`: apraksts, ekrānuzņēmums, kā palaist, saite uz publicēto versiju.
65. Uzraksti lietotāja ceļvedi ar galvenajām darbībām soli pa solim.
66. Pievieno vismaz vienu ekrānuzņēmumu.
67. ★ Iedod pamācību cilvēkam, kas projektu nav redzējis, un izlabo vietas, kur viņš apmaldās.

**Mājasdarbs:** pabeigt dokumentāciju

## 11-096 · Licence un intelektuālais īpašums
`jaukta`

**Tēma:** Licences izvēle. Intelektuālā īpašuma aizsardzība.
**SR:** Izvēlas savam projektam licenci un pamato izvēli.
**Standarts:** T.O.3.1.5. · T.V.3.1.5.

**Gaita**
- 10' — atkārtojums no 03. bloka: MIT, GPL, Apache
- 10' — kā licence maina to, ko citi drīkst darīt ar tavu darbu
- 15' — uzdevumi
- 5' — svešu attēlu un fontu izmantošana projektā

**Uzdevumi**
68. Izvēlies licenci un pievieno `LICENSE` datni repozitorijam.
69. Pieraksti `README.md`, kāpēc izvēlējies tieši šo licenci.
70. Pārbaudi, vai projektā izmantotie attēli un fonti ir brīvi izmantojami.
71. ★ Pieraksti, ko tu darītu, ja kāds tavu projektu paņemtu un pārdotu.

**Mājasdarbs:** commit ar licenci

## 11-097 · Prezentācijas sagatavošana
`jaukta`

**Tēma:** Projekta prezentācijas sagatavošana.
**SR:** Sagatavo demonstrāciju, kas parāda problēmu, risinājumu un izstrādes gaitu.
**Standarts:** T.O.2.4.7. · T.V.2.3.10.

**Gaita**
- 10' — struktūra: problēma, izpēte, demonstrācija, grūtākā vieta, ko iemācījos
- 20' — sagatavošanās un ģenerālmēģinājums pāros
- 10' — divi brīvprātīgie izmēģina visas klases priekšā

**Uzdevumi**
72. Sagatavo 5 minūšu prezentāciju pēc dotās struktūras.
73. Sagatavo demonstrācijas scenāriju: tieši kurus soļus rādīsi.
74. ★ Sagatavo atbildi uz jautājumu «ko tu darītu citādi, ja sāktu no jauna».

**Mājasdarbs:** gatavoties aizstāvēšanai

## 11-098 · Pabeigšana
`prakse`

**Tēma:** Pēdējie labojumi un pašpārbaude.
**SR:** Pabeidz projektu un pārbauda tā atbilstību specifikācijai.
**Standarts:** T.V.1.1.1.

**Gaita**
- 30' — pēdējie labojumi
- 10' — pašpārbaudes tabulas pabeigšana un pēdējais commit

**Uzdevumi**
75. Aizpildi pašpārbaudes tabulu pilnībā un godīgi.
76. Pārbaudi, ka publicētā versija strādā un saite `README.md` ir pareiza.
77. ★ Pārbaudi savu commit vēsturi: vai no tās var saprast, kā projekts auga?

**Mājasdarbs:** —

## 11-099 · SV6: aizstāvēšana
`pārbaudes darbs`

**Tēma:** Projekta demonstrācija un aizstāvēšana.
**SR:** Demonstrē risinājumu un pamato izstrādes laikā pieņemtos lēmumus.
**Standarts:** komplekss SR

**Gaita**
- 40' — aizstāvēšanās pēc grafika, 5 min katram

**Materiāli:** vērtēšanas rubrika un jautājumi — `sv-fv` repozitorijā

**Mājasdarbs:** —

## 11-100 · SV6: aizstāvēšana un kursa noslēgums
`pārbaudes darbs`

**Tēma:** Projekta aizstāvēšana. Kursa noslēgums.
**SR:** Demonstrē risinājumu; reflektē par divos gados apgūto.
**Standarts:** komplekss SR

**Gaita**
- 30' — atlikušās aizstāvēšanās
- 10' — refleksija: ko protam tagad, ko negribētu darīt vēlreiz, kas gaida 12. klasē

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Katrai izstrādes stundai ir «stundas beigās».** Bez tā projekta stundas pārvēršas par
  40 minūtēm, kurās kods nekustas. Ja skolēns mērķi nesasniedz, tā ir konsultācijas, nevis
  vērtējuma vieta.
- **Divi starpposmi ir obligāti.** 11-084 un 11-092. Tieši tur atklājas, kurš ir iestrēdzis,
  un tur vēl var paspēt samazināt apjomu. Bez tiem puse klases to atklās pēdējā nedēļā.
- **«Ko izmetīšu» saraksts no 04. bloka tagad noder.** Kad 11-084 kāds nav grafikā, atbilde
  jau ir uzrakstīta — nav jālemj panikā.
- **Publicēšana ir standarta prasība, ne papildinājums.** Ja Render bezmaksas konts sagādā
  grūtības, klienta daļa GitHub Pages plus demonstrācija lokāli arī ir derīgs risinājums —
  bet publicēšanas mēģinājums ir jāizdara katram.
- **Aizstāvēšana svarīgāka par programmu.** Tas pats princips, kas 10. klasē: skolēns, kurš
  nespēj paskaidrot savu kodu un veikt tajā nelielu izmaiņu, nav izpildījis kompleksu
  sasniedzamo rezultātu, lai cik laba būtu programma.
