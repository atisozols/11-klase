# 01. Objektorientētā programmēšana

**16 stundas (11-001 – 11-016)** · Standarta 5. temats “Kā izvēlēties un efektīvi savā
projektā izmantot jau esošu risinājumu?”

**Bloka mērķis:** modelēt reālas pasaules objektus ar klasēm un veidot programmas, kurās
dati un darbības ar tiem ir vienuviet.

**Teorija un piemēri:** [`teorija.py`](teorija.py) · **Darba fails:** [`uzdevumi.py`](uzdevumi.py)
**Pārbaudes darbi:** privātajā `sv-fv` repozitorijā
**Noslēgums:** SV1 — papīra darbs (11-016)

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 01-oop/README.md && python3 bin/darbafails.py 01-oop -->

| Nr. | Tēma | Sasniedzamais rezultāts | Pārbaude |
| --- | --- | --- | --- |
| 11-001 | Objektorientētās programmēšanas jēdziens. No mainīgajiem un funkcijām uz objektiem. | Skaidro, kāda problēma rodas, glabājot saistītus datus atsevišķos mainīgajos, un kā to risina klase. |  |
| 11-002 | Klases definēšana. Objekta izveide. Atribūti. | Definē klasi ar atribūtiem un izveido no tās objektus. |  |
| 11-003 | Konstruktors `__init__`. Objekta izveide ar sākuma vērtībām. | Uzraksta konstruktoru, kas objekta izveides brīdī piešķir atribūtiem vērtības. |  |
| 11-004 | Metodes. Darbības, kas pieder objektam. | Definē metodi, kas izmanto objekta atribūtus, un izsauc to. |  |
| 11-005 | Atslēgvārds `self` un tā nozīme. | Skaidro, ko nozīmē `self`, un atšķir objekta atribūtu no lokāla mainīgā. |  |
| 11-006 | Metodes, kas maina objekta stāvokli. | Uzraksta metodes, kas maina objekta atribūtus, un izseko stāvokļa izmaiņām. |  |
| 11-007 | Praktikums: klases izstrāde no apraksta. | Patstāvīgi izveido klasi ar konstruktoru un metodēm atbilstoši aprakstam. | **FV1** (dators) |
| 11-008 | Objektu saraksts. Darbs ar daudziem objektiem. | Glabā objektus sarakstā un apstrādā tos ar ciklu. |  |
| 11-009 | Objektu saglabāšana datnē un ielasīšana atpakaļ. | Saglabā objektu datus CSV datnē un izveido objektus no datnes satura. |  |
| 11-010 | Datu pārbaude klases iekšienē. | Pārbauda vērtību derīgumu konstruktorā un metodēs, neļaujot izveidot nederīgu objektu. |  |
| 11-011 | Metode `__str__` un objekta attēlošana tekstā. | Definē `__str__`, lai objektu varētu izvadīt saprotamā formā. |  |
| 11-012 | Iekapsulēšana. Kas ir publisks un kas — klases iekšējā lieta. | Skaidro, kāpēc daļa atribūtu nav paredzēta tiešai maiņai no ārpuses, un lieto metodes to vietā. |  |
| 11-013 | Mantošana. Kopīgu īpašību izcelšana virsklasē. | Izveido apakšklasi, kas manto virsklases atribūtus un metodes, un papildina tās. | **FV2** (papīrs) |
| 11-014 | Klašu modelēšana. Vienkārša klašu diagramma. | Attēlo klases, to atribūtus, metodes un saistības diagrammā. |  |
| 11-015 | Objektorientētā programmēšana: atkārtojums. Kods ar roku. | Atkārto bloka jēdzienus un vingrinās rakstīt klases kodu ar roku. |  |
| 11-016 | Pārbaudes darbs: klases, objekti, metodes, mantošana. | Demonstrē bloka sasniedzamos rezultātus patstāvīgā darbā. | **SV1** |

<!-- TABULA:BEIGAS -->

---

## 11-001 · Kāpēc vajadzīgas klases
`jaukta` · `teorija.py` §1

**Tēma:** Objektorientētās programmēšanas jēdziens. No mainīgajiem un funkcijām uz objektiem.
**SR:** Skaidro, kāda problēma rodas, glabājot saistītus datus atsevišķos mainīgajos, un kā to risina klase.
**Standarts:** T.Li.2. · T.O.2.4.15.

**Gaita**
- 10' — uzdevums uz tāfeles: glabā 30 skolēnu vārdu, klasi un trīs atzīmes. Cik sarakstu vajag?
- 10' — demo §1: tie paši dati kā klase; kas mainījās
- 15' — uzdevumi burtnīcā: no apraksta uz klasi
- 5' — kur ap mums ir objekti (čeks, konts, rezervācija, ieraksts)

**Uzdevumi**
1. Burtnīcā: dotajam aprakstam «bibliotēkas grāmata» pieraksti, kādi dati par to jāglabā un
   kādas darbības ar to var veikt.
2. Burtnīcā: tas pats «skolas ēdnīcas pasūtījumam».
3. Burtnīcā: dotajā programmā ir trīs paralēli saraksti (`vardi`, `klases`, `atzimes`).
   Pieraksti, kas notiks, ja no viena saraksta izdzēsīs elementu, bet no citiem ne.
4. ★ Atrodi savā 10. klases kodā vietu, kur būtu noderējusi klase, un pieraksti, kāpēc.

**Mājasdarbs:** 2. uzdevums

## 11-002 · Klase un objekts
`prakse` · `teorija.py` §2

**Tēma:** Klases definēšana. Objekta izveide. Atribūti.
**SR:** Definē klasi ar atribūtiem un izveido no tās objektus.
**Standarts:** T.O.2.4.15.

**Gaita**
- 5' — klase ir veidne, objekts ir konkrēts eksemplārs
- 10' — demo §2: `class`, objekta izveide, piekļuve atribūtiem ar punktu
- 20' — uzdevumi
- 5' — cik objektu var izveidot no vienas klases?

**Uzdevumi**
5. Izveido klasi `Skolens` ar atribūtiem `vards` un `klase`. Izveido divus objektus un
   izvadi to atribūtus.
6. Izveido klasi `Prece` ar atribūtiem `nosaukums` un `cena`. Izveido trīs objektus.
7. Nomaini viena objekta atribūta vērtību un pārbaudi, ka otrs objekts nemainījās.
8. Izveido klasi `Punkts` ar atribūtiem `x` un `y` un izvadi divu punktu koordinātas.
9. ★ Izveido divus objektus ar vienādām atribūtu vērtībām un pārbaudi, vai tie ir vienādi
   (`==`). Paskaidro rezultātu.

**Mājasdarbs:** 6. uzdevums

## 11-003 · Konstruktors
`prakse` · `teorija.py` §3

**Tēma:** Konstruktors `__init__`. Objekta izveide ar sākuma vērtībām.
**SR:** Uzraksta konstruktoru, kas objekta izveides brīdī piešķir atribūtiem vērtības.
**Standarts:** T.O.2.4.15.

**Gaita**
- 5' — kāpēc atribūtus nav ērti piešķirt pa vienam pēc izveides
- 10' — demo §3: `__init__`, parametri, `self.atribūts = parametrs`
- 20' — uzdevumi
- 5' — kas notiek, ja aizmirst `self`

**Uzdevumi**
10. Pārraksti klasi `Skolens` tā, lai vārdu un klasi padod objekta izveides brīdī.
11. Izveido klasi `Gramata` ar konstruktoru (`nosaukums`, `autors`, `gads`) un izveido
    trīs objektus.
12. Izveido klasi `Konts` ar konstruktoru (`ipasnieks`, `atlikums`) un izvadi abu kontu
    atlikumus.
13. Izveido klasi `Taisnsturis` ar konstruktoru (`platums`, `augstums`).
14. ★ Uzraksti konstruktoru, kuram daļai parametru ir noklusējuma vērtības, un izveido
    objektus abos veidos.

**Mājasdarbs:** 11. uzdevums

## 11-004 · Metodes
`prakse` · `teorija.py` §4

**Tēma:** Metodes. Darbības, kas pieder objektam.
**SR:** Definē metodi, kas izmanto objekta atribūtus, un izsauc to.
**Standarts:** T.O.2.4.15. · T.O.2.4.13.

**Gaita**
- 5' — funkcija, kurai vienmēr jāpadod tie paši dati → metode
- 10' — demo §4: metode kā funkcija klases iekšpusē; `self` piekļuve atribūtiem
- 20' — uzdevumi
- 5' — metode, kas atgriež, un metode, kas izvada

**Uzdevumi**
15. Klasei `Taisnsturis` pievieno metodes `laukums()` un `perimetrs()`.
16. Klasei `Konts` pievieno metodi `ieskaitit(summa)`, kas palielina atlikumu.
17. Klasei `Gramata` pievieno metodi `apraksts()`, kas atgriež tekstu
    `"Blēdis · Anšlavs Eglītis, 1943"`.
18. Klasei `Skolens` pievieno metodi `videja_atzime()`, ja atzīmes glabājas sarakstā.
19. ★ Klasei `Punkts` pievieno metodi `attalums(cits)`, kas atgriež attālumu līdz citam punktam.

**Mājasdarbs:** 17. uzdevums

## 11-005 · self
`jaukta` · `teorija.py` §5

**Tēma:** Atslēgvārds `self` un tā nozīme.
**SR:** Skaidro, ko nozīmē `self`, un atšķir objekta atribūtu no lokāla mainīgā.
**Standarts:** T.O.2.4.15. · T.Li.2.

**Gaita**
- 10' — viena metode, trīs objekti: kā metode zina, ar kuru strādāt?
- 10' — demo §5: `self` ir pats objekts; kas notiek bez tā
- 15' — uzdevumi, pirmie divi burtnīcā
- 5' — biežākā kļūda: `atlikums` vietā `self.atlikums`

**Uzdevumi**
20. Burtnīcā: dotajā klasē atrodi trīs vietas, kur trūkst `self`, un pieraksti, kas notiks.
21. Burtnīcā: pieraksti, ko izvadīs dotā programma ar trim objektiem.
22. Datorā: izlabo doto klasi, kurā metodes maina lokālu mainīgo, nevis atribūtu.
23. ★ Uzraksti klasi, kurā metode atgriež pati sevi (`return self`), un izsauc divas metodes
    vienā rindā.

**Mājasdarbs:** 22. uzdevums

## 11-006 · Objekta stāvoklis
`prakse` · `teorija.py` §6

**Tēma:** Metodes, kas maina objekta stāvokli.
**SR:** Uzraksta metodes, kas maina objekta atribūtus, un izseko stāvokļa izmaiņām.
**Standarts:** T.O.2.4.15.

**Gaita**
- 5' — objekts atceras savu stāvokli starp izsaukumiem
- 10' — demo §6: `ieskaitit` / `iznemt`, pārbaude pirms izmaiņas
- 20' — uzdevumi
- 5' — kāpēc metodei ir jāpārbauda, vai darbība ir atļauta

**Uzdevumi**
24. Klasei `Konts` pievieno metodi `iznemt(summa)`, kas neļauj atlikumam kļūt negatīvam un
    atgriež `True` vai `False`.
25. Izveido klasi `Skaititajs` ar metodēm `palielinat()`, `atiestatit()` un `vertiba()`.
26. Izveido klasi `Grozs`, kurā var pievienot preces un izvadīt kopsummu.
27. Izveido klasi `Termometrs`, kas atceras visas izmērītās temperatūras un atgriež vidējo.
28. ★ Klasei `Konts` pievieno darījumu vēsturi un metodi, kas izvada pēdējos piecus darījumus.

**Mājasdarbs:** 26. uzdevums

## 11-007 · Praktikums: klases
`prakse` · FV1 (dators)

**Tēma:** Praktikums: klases izstrāde no apraksta.
**SR:** Patstāvīgi izveido klasi ar konstruktoru un metodēm atbilstoši aprakstam.
**Standarts:** T.O.2.4.15. · T.O.2.4.8.

**Gaita**
- 5' — uzdevumu nolasīšana
- 20' — patstāvīgs darbs
- 15' — **FV1** pie datora

**Uzdevumi**
29. **Kases čeks.** Klase `Ceks` ar metodēm `pievienot(prece, cena)`, `summa()`,
    `izdrukat()`. Čeka izdruka ir izlīdzināta kolonnās.
30. **Rezervācija.** Klase `Rezervacija` ar atribūtiem un metodi `atcelt()`, kas maina
    statusu un neļauj atcelt divreiz.
31. ★ **Pulkstenis.** Klase `Laiks` ar metodēm `pieskaitit_minutes(n)` un `teksts()`,
    kas pareizi pāriet pār stundu un diennakts robežu.

**Mājasdarbs:** pabeigt 29. uzdevumu

## 11-008 · Objektu kolekcija
`prakse` · `teorija.py` §7

**Tēma:** Objektu saraksts. Darbs ar daudziem objektiem.
**SR:** Glabā objektus sarakstā un apstrādā tos ar ciklu.
**Standarts:** T.O.2.4.15. · T.O.2.4.14.

**Gaita**
- 5' — viens objekts ir maz; īsts uzdevums sākas ar simtiem
- 10' — demo §7: saraksts ar objektiem, cikls, filtrēšana, kārtošana pēc atribūta
- 20' — uzdevumi
- 5' — `sorted(saraksts, key=...)` — kā tas strādā

**Uzdevumi**
32. Izveido piecu `Skolens` objektu sarakstu un izvadi visu vārdus.
33. Atrodi sarakstā skolēnu ar augstāko vidējo atzīmi.
34. Izvadi tikai tos skolēnus, kuru vidējā atzīme ir virs klases vidējās.
35. Sakārto grāmatu sarakstu pēc izdošanas gada.
36. ★ Sagrupē skolēnus pa klasēm vārdnīcā, kur atslēga ir klase, bet vērtība — objektu saraksts.

**Mājasdarbs:** 34. uzdevums

## 11-009 · Objekti un datnes
`prakse` · `teorija.py` §8

**Tēma:** Objektu saglabāšana datnē un ielasīšana atpakaļ.
**SR:** Saglabā objektu datus CSV datnē un izveido objektus no datnes satura.
**Standarts:** T.O.2.4.14. · T.O.2.4.17.

**Gaita**
- 5' — atkārtojums no 10. klases: CSV rinda → saraksts
- 10' — demo §8: objekts → rinda, rinda → objekts
- 20' — uzdevumi
- 5' — kāpēc objekts pats zina, kā sevi saglabāt

**Uzdevumi**
37. Klasei `Gramata` pievieno metodi `uz_rindu()`, kas atgriež CSV rindu.
38. Uzraksti funkciju, kas no CSV rindas izveido `Gramata` objektu.
39. Saglabā visu grāmatu sarakstu datnē un ielasi to atpakaļ jaunā programmā.
40. Papildini programmu tā, lai jaunu grāmatu var pievienot un tā saglabājas.
41. ★ Uzraksti metodi, kas pārbauda, vai CSV rinda ir derīga, un atgriež `None`, ja nav.

**Mājasdarbs:** 39. uzdevums

## 11-010 · Validācija klasē
`prakse` · `teorija.py` §9

**Tēma:** Datu pārbaude klases iekšienē.
**SR:** Pārbauda vērtību derīgumu konstruktorā un metodēs, neļaujot izveidot nederīgu objektu.
**Standarts:** T.V.2.3.5. · T.O.2.4.15.

**Gaita**
- 5' — vai `Konts("Anna", -500)` drīkst eksistēt?
- 10' — demo §9: pārbaude konstruktorā; `raise ValueError`
- 20' — uzdevumi
- 5' — kur labāk pārbaudīt: klasē vai programmā, kas to lieto

**Uzdevumi**
42. Klasē `Konts` neļauj izveidot objektu ar negatīvu atlikumu.
43. Klasē `Skolens` neļauj pievienot atzīmi, kas nav no 1 līdz 10.
44. Klasē `Gramata` pārbaudi, ka gads ir no 1500 līdz šodienai.
45. Uzraksti programmu, kas noķer kļūdu ar `try` / `except` un turpina darbu.
46. ★ Pievieno klasei metodi `ir_deriga()`, kas atgriež visu problēmu sarakstu, nevis met kļūdu.

**Mājasdarbs:** 43. uzdevums

## 11-011 · Objekta izvade
`prakse` · `teorija.py` §10

**Tēma:** Metode `__str__` un objekta attēlošana tekstā.
**SR:** Definē `__str__`, lai objektu varētu izvadīt saprotamā formā.
**Standarts:** T.O.2.4.15. · T.V.2.3.10.

**Gaita**
- 5' — kāpēc `print(objekts)` izvada `<__main__.Gramata object at 0x...>`
- 10' — demo §10: `__str__`, formatēta izvade
- 20' — uzdevumi
- 5' — informācijas dizains: kas lietotājam tiešām jāredz

**Uzdevumi**
47. Klasei `Gramata` pievieno `__str__` un izvadi objektu ar `print`.
48. Klasei `Konts` pievieno `__str__` ar summu divos ciparos aiz komata.
49. Izvadi objektu sarakstu ciklā tā, lai iznāk izlīdzināta tabula.
50. ★ Pievieno klasei metodi `kopsavilkums()`, kas atgriež vairākrindu tekstu ar rāmīti.

**Mājasdarbs:** 47. uzdevums

## 11-012 · Iekapsulēšana
`jaukta` · `teorija.py` §11

**Tēma:** Iekapsulēšana. Kas ir publisks un kas — klases iekšējā lieta.
**SR:** Skaidro, kāpēc daļa atribūtu nav paredzēta tiešai maiņai no ārpuses, un lieto metodes to vietā.
**Standarts:** T.O.2.4.15. · T.Li.2.

**Gaita**
- 10' — `konts.atlikums = 1000000` — kāpēc tas ir problēma
- 10' — demo §11: `_` prefikss kā vienošanās; metodes piekļuvei
- 15' — uzdevumi
- 5' — Python neaizliedz, bet vienojas — kāpēc tas tomēr strādā

**Uzdevumi**
51. Pārraksti klasi `Konts` tā, lai atlikumu var mainīt tikai ar metodēm.
52. Burtnīcā: pieraksti, kuri no dotās klases atribūtiem drīkstētu būt publiski un kuri ne.
53. Pievieno klasei metodi, kas atgriež atribūta vērtību, bet neļauj to mainīt.
54. ★ Uzraksti klasi, kurā viens atribūts tiek aprēķināts no citiem un tāpēc to vispār nav
    jēgas glabāt.

**Mājasdarbs:** 51. uzdevums

## 11-013 · Mantošana
`jaukta` · FV2 (papīrs) · `teorija.py` §12

**Tēma:** Mantošana. Kopīgu īpašību izcelšana virsklasē.
**SR:** Izveido apakšklasi, kas manto virsklases atribūtus un metodes, un papildina tās.
**Standarts:** T.O.2.4.15.

**Gaita**
- 15' — **FV2** uz papīra, datori vēl aizvērti
- 10' — demo §12: `class Apaksklase(Virsklase)`, `super().__init__()`
- 15' — uzdevumi

**Uzdevumi**
55. Izveido klasi `Darbinieks` un apakšklasi `Skolotajs`, kas pievieno priekšmetu.
56. Izveido klasi `Transportlidzeklis` un divas apakšklases ar atšķirīgu metodi.
57. Pārraksti divas savas iepriekšējās klases tā, lai kopīgais būtu virsklasē.
58. ★ Uzraksti apakšklasi, kas pārraksta (override) virsklases metodi, un parādi abu darbību.

**Mājasdarbs:** 55. uzdevums

## 11-014 · Klašu diagramma
`teorija`

**Tēma:** Klašu modelēšana. Vienkārša klašu diagramma.
**SR:** Attēlo klases, to atribūtus, metodes un saistības diagrammā.
**Standarts:** T.O.2.4.15. · T.O.2.4.3.

**Gaita**
- 10' — kāpēc pirms rakstīšanas vērts uzzīmēt; diagrammas elementi
- 15' — kopīgi: no dota apraksta uz diagrammu uz tāfeles
- 10' — pāros: sava iepriekšējā uzdevuma diagramma
- 5' — kur šo redzēsim atkal (12. klasē, projekta specifikācijā)

**Uzdevumi**
59. Burtnīcā: uzzīmē klašu diagrammu bibliotēkas sistēmai (grāmata, lasītājs, izsniegums).
60. Burtnīcā: uzzīmē diagrammu savai 11-007 čeka programmai.
61. ★ Burtnīcā: uzzīmē diagrammu sistēmai ar mantošanu (lietotājs un administrators).

**Mājasdarbs:** 59. uzdevums

## 11-015 · Atkārtojums pirms pārbaudes darba
`jaukta`

**Tēma:** Objektorientētā programmēšana: atkārtojums. Kods ar roku.
**SR:** Atkārto bloka jēdzienus un vingrinās rakstīt klases kodu ar roku.
**Standarts:** viss bloks

**Gaita**
- 10' — kopīgi: `self`, konstruktors, atribūts pret lokālu mainīgo — kur klase kļūdījās
- 20' — **burtnīcā**, bez datora: trīs uzdevumi
- 10' — pārbaudām kopā uz tāfeles

**Uzdevumi**
62. Burtnīcā: uzraksti klasi `Ekskursija` ar konstruktoru un divām metodēm.
63. Burtnīcā: dots klases kods — pieraksti, ko izvadīs programma, kas to lieto.
64. Burtnīcā: dotajā klasē ir trīs kļūdas. Atrodi un izlabo.
65. ★ Burtnīcā: uzraksti apakšklasi dotajai virsklasei.

**Mājasdarbs:** gatavoties SV1

## 11-016 · Pārbaudes darbs
`pārbaudes darbs`

**Tēma:** Pārbaudes darbs: klases, objekti, metodes, mantošana.
**SR:** Demonstrē bloka sasniedzamos rezultātus patstāvīgā darbā.
**Standarts:** viss bloks

**Gaita**
- 40' — darbs uz papīra, datori aizvērti; kods jāraksta ar roku

**Materiāli:** SV1 — divi varianti, papīra darbs (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Šī klase klases jau ir redzējusi.** Pērn 10. klasē viņi darīja `klases_2026.py` — bet tur
  bija tikai konstruktors un pāris metodes. Jaunais šeit ir objektu kolekcijas (11-008),
  saglabāšana datnē (11-009), validācija (11-010), iekapsulēšana (11-012) un mantošana
  (11-013). Pirmās septiņas stundas var iet ātrāk, ja klase to pierāda 11-002 uzdevumos.
- **`self` ir vieta, kur puse klases apstājas.** 11-005 ir vesela stunda tikai par to, un tas
  nav par daudz. Ja skolēns raksta `atlikums` vietā `self.atlikums`, programma bieži strādā —
  līdz brīdim, kad tā vairs nestrādā.
- **Klase pret vārdnīcu.** Sagaidi jautājumu «kāpēc ne vienkārši vārdnīca?». Atbilde ir
  11-004: vārdnīcā ir dati, klasē ir dati **kopā ar darbībām**. Tas ir arī iemesls, kāpēc
  11-009 metode `uz_rindu()` pieder pašam objektam.
- **Mantošana ir pēdējā, ne pirmā.** Daudzi kursi sāk ar to; praksē skolēni to pārlieto un
  taisa piecu līmeņu hierarhijas tur, kur pietiktu ar vienu klasi. Tāpēc tā šeit ir viena
  stunda pirms atkārtojuma.
