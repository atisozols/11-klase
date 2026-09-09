# 04. Lietotāju izpēte, specifikācija, projekta vadība

**16 stundas (11-047 – 11-062)** · Standarta 2. temats “Kā izplānot un izveidot lietotājam
atbilstošu programmētu risinājumu un uzraudzīt tā īstenošanu?”

**Bloka mērķis:** izpētīt reālu lietotāja vajadzību un uzrakstīt programmatūras prasību
specifikāciju, pēc kuras var izstrādāt risinājumu.

**Teorija un paraugi:** [`teorija.md`](teorija.md) · **Darba fails:** [`uzdevumi.md`](uzdevumi.md)
**Specifikācijas veidne:** [`specifikacija-veidne.md`](specifikacija-veidne.md)
**Noslēgums:** SV4 — savas specifikācijas aizstāvēšana ar biļetēm (11-062)

> **Svarīgi.** Specifikācija, ko uzrakstīsi šajā blokā, ir tava **06. bloka projekta darba
> uzdevums**. Tas nav vingrinājums, ko pēc tam izmet. Tāpēc izvēlies problēmu, kuru tiešām
> gribi atrisināt, un tādu, ko var uzbūvēt kā tīmekļa lietotni ar datubāzi.

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 04-izpete-un-specifikacija/README.md && python3 bin/darbafails.py 04-izpete-un-specifikacija -->

| Nr. | Tēma | Sasniedzamais rezultāts | Pārbaude |
| --- | --- | --- | --- |
| 11-047 | Prasību problēma. Kāpēc programmatūra neatbilst vajadzībām. | Skaidro, kā rodas neatbilstība starp pasūtīto un izstrādāto, un kā to novērš specifikācija. |  |
| 11-048 | Ieinteresētās puses un mērķauditorija. | Nosaka risinājuma ieinteresētās puses un izvēlas mērķauditoriju. |  |
| 11-049 | Lietotāju izpētes metodes: intervija, aptauja, novērojums, esošo risinājumu analīze. | Izvēlas uzdevumam piemērotu izpētes metodi un pamato izvēli. |  |
| 11-050 | Intervijas jautājumu veidošana. Labs un slikts jautājums. | Formulē atvērtus jautājumus, kas neuzspiež atbildi. |  |
| 11-051 | Aptaujas izveide. Jautājumu veidi un datu validācija. | Izveido aptauju ar derīgiem jautājumu veidiem un iebūvētu datu pārbaudi. | **FV7** (papīrs) |
| 11-052 | Izpētes plāna īstenošana. | Veic interviju vai novērojumu un dokumentē iegūto. |  |
| 11-053 | Aptaujas datu apkopošana un attēlošana ar programmu. | Apstrādā aptaujas CSV datus un izveido kopsavilkumu, kas atbild uz izpētes jautājumu. | **FV8** (dators) |
| 11-054 | Lietotāja stāsti. No izpētes datiem uz konkrētām vajadzībām. | Pārvērš izpētes rezultātus lietotāja stāstos. |  |
| 11-055 | Funkcionālās un nefunkcionālās prasības. | Atšķir funkcionālās un nefunkcionālās prasības un formulē tās pārbaudāmi. |  |
| 11-056 | Programmatūras prasību specifikācijas uzbūve. | Nosauc specifikācijas daļas un skaidro, kam katra vajadzīga. |  |
| 11-057 | Lietotāja saskarnes struktūrskice (wireframe). HTML un CSS atkārtojums. | Izveido saskarnes skici un attēlo to kā vienkāršu HTML lapu. |  |
| 11-058 | Uzdevumu sadalīšana un projekta vadības rīki. | Sadala projektu izpildāmos uzdevumos un ievieto tos projekta vadības rīkā. |  |
| 11-059 | Laika plānošana. Ganta diagramma. | Izplāno projekta izstrādi laikā un nosaka starpposmu termiņus. |  |
| 11-060 | Specifikācijas pabeigšana. | Pabeidz programmatūras prasību specifikāciju atbilstoši veidnei. |  |
| 11-061 | Specifikācijas recenzēšana. Atgriezeniskā saite. | Izvērtē citu specifikāciju pēc kritērijiem un sniedz konkrētu atgriezenisko saiti. |  |
| 11-062 | Specifikācijas aizstāvēšana. Izpētes un lēmumu pamatošana. | Pamato savu izpēti, izvēles un prasības, atbildot uz jautājumiem. | **SV4** |

<!-- TABULA:BEIGAS -->

---

## 11-047 · Kāpēc programmatūra neizdodas
`teorija` · `teorija.md` §1

**Tēma:** Prasību problēma. Kāpēc programmatūra neatbilst vajadzībām.
**SR:** Skaidro, kā rodas neatbilstība starp pasūtīto un izstrādāto, un kā to novērš specifikācija.
**Standarts:** T.Li.2. · T.Li.1.

**Gaita**
- 10' — «uztaisi man kalkulatoru»: klase saraksta, kas var noiet greizi
- 15' — gadījuma izpēte: reāls projekts, kas neizdevās, un kāpēc
- 10' — divas specifikācijas vienam uzdevumam: laba un slikta; kur trūkst informācijas
- 5' — kas ir specifikācija un kam tā palīdz

**Uzdevumi**
1. Burtnīcā: dotajam vienas rindas uzdevumam «vajag sistēmu pulciņu pieteikumiem» uzraksti
   piecus jautājumus, kas obligāti jāuzdod pasūtītājam.
2. Burtnīcā: salīdzini divas dotās specifikācijas un pieraksti trīs vietas, kur sliktākajā
   trūkst informācijas.
3. ★ Atrodi kādu lietotni, ko tu lieto un kas kaut ko dara neērti. Uzraksti, kāda prasība,
   tavuprāt, tur ir palikusi nenoskaidrota.

**Mājasdarbs:** 1. uzdevums

## 11-048 · Ieinteresētās puses
`jaukta` · `teorija.md` §2

**Tēma:** Ieinteresētās puses un mērķauditorija.
**SR:** Nosaka risinājuma ieinteresētās puses un izvēlas mērķauditoriju.
**Standarts:** T.V.1.2.1. · T.Li.3.

**Gaita**
- 10' — skolas ēdnīcas sistēma: kurš tajā ir ieinteresēts? Saraksts uz tāfeles
- 10' — mērķauditorija nav «visi»; kāpēc tas ir svarīgi
- 15' — uzdevumi
- 5' — katrs nosauc savu problēmu, ko gribētu risināt

**Uzdevumi**
4. Burtnīcā: dotajai sistēmai uzskaiti vismaz piecas ieinteresētās puses un pieraksti,
   kas katrai ir svarīgi.
5. Burtnīcā: izvēlies vienu no tām par mērķauditoriju un pamato izvēli.
6. Pieraksti savu projekta ideju vienā teikumā: kam un kādu problēmu tā risina.
7. ★ Atrodi divas ieinteresētās puses, kuru vēlmes ir pretrunā, un pieraksti, kā tu izšķirtu.

**Mājasdarbs:** 6. uzdevums

## 11-049 · Izpētes metodes
`teorija` · `teorija.md` §3

**Tēma:** Lietotāju izpētes metodes: intervija, aptauja, novērojums, esošo risinājumu analīze.
**SR:** Izvēlas uzdevumam piemērotu izpētes metodi un pamato izvēli.
**Standarts:** T.V.1.2.1.

**Gaita**
- 10' — četras metodes: ko katra dod un ko nedod
- 15' — kad kura der: seši scenāriji, klase izvēlas un strīdas
- 10' — izpētes plāns: ko, kam, kad, kā pierakstīšu
- 5' — cik cilvēku pietiek? Atbilde nav «visi»

**Uzdevumi**
8. Burtnīcā: aizpildi tabulu par četrām metodēm — ko dod, cik laika prasa, kad neder.
9. Izvēlies savai idejai vienu vai divas metodes un pamato rakstiski.
10. Uzraksti savu izpētes plānu: ar ko runāsi, ko jautāsi, kā pierakstīsi.
11. ★ Atrodi divus esošus risinājumus savai problēmai un pieraksti, ko katrs dara labi un ko ne.

**Mājasdarbs:** 10. uzdevums

## 11-050 · Intervijas jautājumi
`jaukta` · `teorija.md` §4

**Tēma:** Intervijas jautājumu veidošana. Labs un slikts jautājums.
**SR:** Formulē atvērtus jautājumus, kas neuzspiež atbildi.
**Standarts:** T.V.1.2.1. · Ieradumi

**Gaita**
- 10' — «Vai tev nešķiet, ka pašreizējā sistēma ir neērta?» — kas ar šo jautājumu nav kārtībā
- 10' — atvērts pret slēgtu; jautājums par pagātni pret jautājumu par nākotni
- 15' — uzdevumi, pāros izmēģina
- 5' — kā pierakstīt atbildes, lai pēc nedēļas tās vēl saprot

**Uzdevumi**
12. Burtnīcā: pieci doti jautājumi — atzīmē, kuri ir slikti, un pārraksti tos.
13. Uzraksti astoņus jautājumus savai intervijai; vismaz pieciem jābūt atvērtiem.
14. Pāros: uzdod savus jautājumus sola biedram un pieraksti atbildes.
15. Pēc izmēģinājuma pārraksti divus jautājumus, kas nestrādāja.
16. ★ Uzraksti jautājumu, kas noskaidro, ko cilvēks **tiešām dara**, nevis ko viņš domā, ka dara.

**Mājasdarbs:** 13. uzdevums

## 11-051 · Aptauja
`jaukta` · FV7 (papīrs) · `teorija.md` §5

**Tēma:** Aptaujas izveide. Jautājumu veidi un datu validācija.
**SR:** Izveido aptauju ar derīgiem jautājumu veidiem un iebūvētu datu pārbaudi.
**Standarts:** T.V.2.3.4. · T.V.2.3.5.

**Gaita**
- 15' — **FV7** uz papīra, datori vēl aizvērti
- 10' — jautājumu veidi: izvēle, skala, atvērts; kad kurš
- 15' — aptaujas izveide tiešsaistes rīkā ar validāciju

**Uzdevumi**
17. Izveido aptauju ar vismaz sešiem jautājumiem savai izpētei.
18. Vismaz diviem jautājumiem iestati datu validāciju un pārbaudi, ka tā strādā.
19. Iedod aptauju diviem cilvēkiem un pieraksti, kas viņiem nebija skaidrs.
20. ★ Pievieno jautājumu, kura atbildes vēlāk varēs attēlot diagrammā, un pieraksti, kādā.

**Mājasdarbs:** izsūtīt aptauju

## 11-052 · Izpētes veikšana
`prakse`

**Tēma:** Izpētes plāna īstenošana.
**SR:** Veic interviju vai novērojumu un dokumentē iegūto.
**Standarts:** T.V.1.2.1. · Ieradumi

**Gaita**
- 5' — kā uzvesties intervijā: klausies vairāk, nekā runā
- 25' — intervijas vai novērojumi (skolā, ar skolotāju, ar ēdnīcas darbinieku)
- 10' — pierakstu sakārtošana, kamēr atmiņā svaigs

**Uzdevumi**
21. Veic vismaz vienu interviju un pieraksti atbildes.
22. Pieraksti trīs lietas, kas tevi pārsteidza — kaut ko, ko negaidīji.
23. ★ Veic arī novērojumu un salīdzini: vai cilvēks dara to, ko stāstīja?

**Mājasdarbs:** pabeigt pierakstus

## 11-053 · Izpētes datu apstrāde
`prakse` · FV8 (dators)

**Tēma:** Aptaujas datu apkopošana un attēlošana ar programmu.
**SR:** Apstrādā aptaujas CSV datus un izveido kopsavilkumu, kas atbild uz izpētes jautājumu.
**Standarts:** T.V.2.3.6. · T.O.2.4.14.

**Gaita**
- 5' — no aptaujas rīka lejupielādē CSV
- 20' — apstrāde ar Python: skaitīšana, vidējais, sadalījums (10. klases prasmes)
- 15' — **FV8** pie datora

**Uzdevumi**
24. Lejupielādē savas aptaujas atbildes CSV formātā un ielasi tās programmā.
25. Saskaiti atbilžu sadalījumu katram izvēles jautājumam.
26. Aprēķini vidējo vērtību skalas jautājumiem.
27. Saglabā kopsavilkumu CSV datnē un izveido vienu diagrammu.
28. ★ Atrodi datos kādu sakarību starp diviem jautājumiem un pieraksti to.

**Mājasdarbs:** 27. uzdevums

## 11-054 · No vajadzībām uz lietotāja stāstiem
`jaukta` · `teorija.md` §6

**Tēma:** Lietotāja stāsti. No izpētes datiem uz konkrētām vajadzībām.
**SR:** Pārvērš izpētes rezultātus lietotāja stāstos.
**Standarts:** T.O.2.4.1. · T.O.2.4.4.

**Gaita**
- 10' — lietotāja stāsta forma: kā **kas** es gribu **ko**, lai **kāpēc**
- 10' — no intervijas citāta uz stāstu: kopīgi uz tāfeles
- 15' — uzdevumi
- 5' — stāsts, kas ir par lielu, jāsadala

**Uzdevumi**
29. Burtnīcā: pārvērš trīs dotos intervijas citātus par lietotāja stāstiem.
30. Uzraksti vismaz astoņus lietotāja stāstus savam projektam.
31. Atzīmē, kuri no taviem stāstiem ir obligāti un kuri — ja paliek laiks.
32. ★ Atrodi savu stāstu, kas ir par lielu, un sadali to trijos mazākos.

**Mājasdarbs:** 30. uzdevums

## 11-055 · Prasības
`jaukta` · `teorija.md` §7

**Tēma:** Funkcionālās un nefunkcionālās prasības.
**SR:** Atšķir funkcionālās un nefunkcionālās prasības un formulē tās pārbaudāmi.
**Standarts:** T.O.2.4.4.

**Gaita**
- 10' — «programmai jābūt ātrai» — kā to pārbaudīt? Prasība, ko nevar pārbaudīt, nav prasība
- 10' — funkcionālā (ko dara) pret nefunkcionālo (cik labi dara)
- 15' — uzdevumi
- 5' — katra prasība sākas ar «sistēma …»

**Uzdevumi**
33. Burtnīcā: sadali desmit dotās prasības funkcionālajās un nefunkcionālajās.
34. Burtnīcā: pārraksti trīs nepārbaudāmas prasības tā, lai tās var pārbaudīt.
35. Uzraksti vismaz desmit funkcionālās prasības savam projektam.
36. Uzraksti vismaz trīs nefunkcionālās prasības.
37. ★ Katrai savai prasībai pieraksti, kā tu pārbaudīsi, ka tā ir izpildīta.

**Mājasdarbs:** 35. uzdevums

## 11-056 · Specifikācijas struktūra
`teorija` · [`specifikacija-veidne.md`](specifikacija-veidne.md)

**Tēma:** Programmatūras prasību specifikācijas uzbūve.
**SR:** Nosauc specifikācijas daļas un skaidro, kam katra vajadzīga.
**Standarts:** T.O.2.4.4.

**Gaita**
- 10' — veidnes caurskatīšana: septiņas daļas un kāpēc katra
- 15' — divu gatavu specifikāciju salīdzināšana
- 10' — savas veidnes aizpildīšanas sākums
- 5' — cik gara ir laba specifikācija? Tik, cik vajag, ne vairāk

**Uzdevumi**
38. Nokopē veidni savā repozitorijā un aizpildi pirmās trīs daļas.
39. Burtnīcā: dotajā specifikācijā atzīmē, kura daļa trūkst.
40. ★ Pieraksti, kura veidnes daļa tavam projektam būs visgrūtākā, un kāpēc.

**Mājasdarbs:** 38. uzdevums

## 11-057 · Struktūrskices
`prakse` · `teorija.md` §8

**Tēma:** Lietotāja saskarnes struktūrskice (wireframe). HTML un CSS atkārtojums.
**SR:** Izveido saskarnes skici un attēlo to kā vienkāršu HTML lapu.
**Standarts:** T.V.2.2.1. · T.V.2.3.10.

**Gaita**
- 5' — skice nav dizains: kastītes un uzraksti, ne krāsas
- 10' — HTML pamati atkārtojums: virsraksti, saraksti, forma, tabula
- 20' — uzdevumi
- 5' — kur šī skice pārtaps par īstu lapu (06. bloks)

**Uzdevumi**
41. Uzzīmē uz papīra sava risinājuma galvenā ekrāna skici.
42. Pārtaisi to par HTML lapu ar virsrakstiem, sarakstu un formu.
43. Pievieno CSS, kas sakārto elementus, bet neizmanto vairāk par trim krāsām.
44. Izveido otro skici — ekrānam, kurā lietotājs pievieno jaunu ierakstu.
45. ★ Pievieno skicei paskaidrojumus: kas notiek, nospiežot katru pogu.

**Mājasdarbs:** 42. uzdevums

## 11-058 · Projekta vadība
`jaukta` · `teorija.md` §9

**Tēma:** Uzdevumu sadalīšana un projekta vadības rīki.
**SR:** Sadala projektu izpildāmos uzdevumos un ievieto tos projekta vadības rīkā.
**Standarts:** T.V.2.3.8.

**Gaita**
- 10' — kāpēc «uztaisīt sistēmu» nav uzdevums; kāds ir labs uzdevuma izmērs
- 10' — GitHub Projects: kolonnas, kartītes, saites uz commit
- 15' — uzdevumi
- 5' — kas notiek ar uzdevumu, kas nekustas divas nedēļas

**Uzdevumi**
46. Sadali savu projektu vismaz 15 uzdevumos, katrs izpildāms vienā stundā.
47. Izveido GitHub Projects dēli ar kolonnām «Darāmie», «Procesā», «Gatavs».
48. Ievieto uzdevumus dēlī un sakārto tos izpildes secībā.
49. ★ Atzīmē, kuri uzdevumi ir atkarīgi cits no cita, un pieraksti, kurš jāizdara pirmais.

**Mājasdarbs:** 48. uzdevums

## 11-059 · Laika plānošana
`jaukta` · `teorija.md` §10

**Tēma:** Laika plānošana. Ganta diagramma.
**SR:** Izplāno projekta izstrādi laikā un nosaka starpposmu termiņus.
**Standarts:** T.V.2.3.8.

**Gaita**
- 10' — 06. blokā ir 24 stundas; kā tās sadalīt
- 15' — Ganta diagramma: uzdevumi pa nedēļām, starpposmi
- 10' — uzdevumi
- 5' — kāpēc plānā jāatstāj rezerve

**Uzdevumi**
50. Izveido sava projekta laika plānu 06. bloka 24 stundām.
51. Atzīmē divus starpposmus: kas būs gatavs 8. un 16. stundā.
52. Pieraksti, kuras daļas tu izmetīsi, ja pietrūks laika.
53. ★ Uzzīmē Ganta diagrammu un atzīmē, kuri uzdevumi var notikt paralēli.

**Mājasdarbs:** 51. uzdevums

## 11-060 · Specifikācijas rakstīšana
`prakse`

**Tēma:** Specifikācijas pabeigšana.
**SR:** Pabeidz programmatūras prasību specifikāciju atbilstoši veidnei.
**Standarts:** T.O.2.4.4. · komplekss SR

**Gaita**
- 5' — kas vēl trūkst: katrs pārbauda savu veidni
- 30' — patstāvīgs darbs, skolotājs konsultē pēc kārtas
- 5' — commit

**Uzdevumi**
54. Pabeidz visas specifikācijas daļas.
55. Pievieno specifikācijai struktūrskices un datu modeli.
56. ★ Pievieno sadaļu «ārpus apjoma»: ko tu apzināti **nedarīsi**.

**Mājasdarbs:** pabeigt specifikāciju

## 11-061 · Savstarpējā recenzēšana
`jaukta`

**Tēma:** Specifikācijas recenzēšana. Atgriezeniskā saite.
**SR:** Izvērtē citu specifikāciju pēc kritērijiem un sniedz konkrētu atgriezenisko saiti.
**Standarts:** T.V.1.3.2. · Ieradumi

**Gaita**
- 5' — recenzijas kritēriji un kā formulēt piezīmi cieņpilni
- 20' — katrs recenzē divas specifikācijas
- 10' — saņemtās piezīmes un labojumi
- 5' — kuras piezīmes bija visnoderīgākās

**Uzdevumi**
57. Recenzē divas klasesbiedru specifikācijas pēc dotajiem kritērijiem.
58. Katrai uzraksti vismaz vienu jautājumu, uz kuru specifikācija neatbild.
59. Izlabo savu specifikāciju pēc saņemtajām piezīmēm un pieraksti, ko mainīji.
60. ★ Atrodi savā specifikācijā prasību, kuru tu, godīgi sakot, nepaspēsi izpildīt, un
    pārceļ to uz «ārpus apjoma».

**Mājasdarbs:** gatavoties SV4

## 11-062 · SV4: specifikācijas aizstāvēšana
`pārbaudes darbs`

**Tēma:** Specifikācijas aizstāvēšana. Izpētes un lēmumu pamatošana.
**SR:** Pamato savu izpēti, izvēles un prasības, atbildot uz jautājumiem.
**Standarts:** komplekss SR

**Gaita**
- 40' — biļetes: katrs velk biļeti ar diviem jautājumiem par savu darbu, atbild 5 min

**Materiāli:** SV4 — biļešu kopums un kritēriji (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Šis ir bloks, kurā programmēšanas stundā gandrīz nav programmēšanas.** Divas stundas
  (11-053 un 11-057) ir pie datora, pārējās — saruna, pieraksti un dokuments. Motivāciju
  tur nevis metode, bet mērķis: viņi raksta **sava** projekta darba uzdevumu. Atgādini to
  regulāri, it īpaši 11-054 un 11-055, kur intereses līkne ir viszemākā.
- **Specifikācija jāapstiprina.** Pirms 06. bloka pārskati katru un pasaki skaidri: šis ir
  izpildāms, šis nav. Biežākā problēma — mobilā lietotne vai mākslīgais intelekts. Prasība
  ir vienkārša: tīmekļa lietotne ar datubāzi, serveri un klienta daļu.
- **Intervija ar reālu cilvēku, ne ar klasesbiedru.** Skolotājs, bibliotekārs, ēdnīcas
  darbinieks, treneris, vecāki. Tieši tur rodas pārsteigumi, kas 11-052 22. uzdevumā tiek
  prasīti — un tieši tie padara projektu par īstu.
- **Ganta diagramma nav pašmērķis.** Vajag, lai skolēns saprot: 24 stundas ir maz, un tas,
  kas nav saplānots, netiks izdarīts. 11-059 52. uzdevums — «ko izmetīšu» — praksē izrādās
  vissvarīgākais.
