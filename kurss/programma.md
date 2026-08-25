# Programmēšana I — kursa programma (11. klase)

Pamatkurss **Programmēšana I** (optimālais līmenis) ir 210 stundas, sadalītas divos gados:

| | Stundas | Standarta temati |
| --- | --- | --- |
| 10. klase | ~100 | 1. temats, 4. temats, 3. temata pirmā daļa |
| **11. klase** | ~100 | 3. temata otrā daļa, 2. temats, 5. temats, 6. temats |

## Standarta temati un to segums 11. klasē

| Standarta temats | St. standartā | Kur mācām |
| --- | --- | --- |
| 2. Kā izplānot un izveidot lietotājam atbilstošu programmētu risinājumu? | 30 | Bloks 04 |
| 3. Kā automātiski apstrādāt un attēlot datus? (datubāzes) | 40 | Bloks 02 |
| 5. Kā izvēlēties un efektīvi izmantot jau esošu risinājumu? | 40 | Bloki 01, 03, 05 |
| 6. Kā īstenot risinājumu? | 50 | Bloks 06 |

## Kursa loģika

Bloki 04–06 veido vienu līniju: **04. blokā skolēns izpēta reālu problēmu un uzraksta
programmatūras prasību specifikāciju, 05. blokā iegūst tehnisko spēju to uzbūvēt, 06. blokā
uzbūvē tieši to, ko pats aprakstīja.** Specifikācija nav mācību vingrinājums, ko pēc tam
izmet — tā ir viņa paša projekta darba uzdevums.

Bloki 01–03 dod rīkus: objektorientēto pieeju, datubāzi un ārējo bibliotēku lietošanu.

## Bloki

### 01. Objektorientētā programmēšana — 16 st.
**Mērķis:** modelēt reālas pasaules objektus ar klasēm un veidot programmas, kurās dati un
darbības ar tiem ir vienuviet.

- **Ziņas:** Objektorientētā programmēšana atvieglo darbu ar kompleksām datu struktūrām un
  apkārtējās pasaules modelēšanu (T.Li.2.) · Standarta bibliotēkas izmantošana atvieglo
  risinājumu izveidi (T.Li.2.)
- **Prasmes:** T.O.2.4.15. · T.O.2.4.13. · T.O.2.4.10. · T.O.2.4.8.
- **Jēdzieni:** klase, objekts, metode, īpašība, konstruktors, iekapsulēšana, mantošana
- **Vērtēšana:** SV1 — papīra darbs

### 02. Datubāzes un SQL — 16 st.
**Mērķis:** izplānot un izveidot datubāzi ar vairākām saistītām tabulām un iegūt no tās
vajadzīgo informāciju ar vaicājumiem.

- **Ziņas:** Datubāzes pareiza izveide atvieglo darbu ar datiem (T.Li.2.) · Datu validācija
  aizsargā datubāzi (T.Li.2.) · Automatizācijas rīki atvieglo darbu ar apjomīgiem datiem (T.Li.2.)
- **Prasmes:** T.O.2.3.4. · T.V.2.3.7. · T.O.2.4.17. · T.V.2.3.5.
- **Jēdzieni:** datubāze, tabula, ieraksts, primārā un ārējā atslēga, relācija, vaicājums,
  JOIN, agregātfunkcija, datu validācija
- **Vērtēšana:** SV2 — biļetes

### 03. Bibliotēkas, API un dati no tīmekļa — 14 st.
**Mērķis:** atrast, pievienot un lietot ārējo bibliotēku un iegūt datus no publiskas
programmsaskarnes.

- **Ziņas:** API izmantošana var samazināt programmas izstrādes laiku (T.Li.2.) ·
  Kvalitatīvs informācijas avots ir priekšnosacījums augstas kvalitātes datiem (T.Li.2.)
- **Prasmes:** T.O.2.4.11. · T.O.2.4.10. · T.O.2.3.3. · T.V.2.3.6.
- **Jēdzieni:** bibliotēka, modulis, pakotne, API, JSON, API atslēga, licence
- **Vērtēšana:** SV3 — datora darbs

### 04. Lietotāju izpēte, specifikācija, projekta vadība — 16 st.
**Mērķis:** izpētīt reālu lietotāja vajadzību un uzrakstīt programmatūras prasību
specifikāciju, pēc kuras var izstrādāt risinājumu.

- **Ziņas:** Lai izveidotu lietotājam vajadzīgu risinājumu, jāveic mērķauditorijas izpēte
  (T.Li.3.) · Labas komunikācijas prasmes un empātija palīdz iegūt kvalitatīvu informāciju
  no lietotājiem (T.Li.1.) · Programmatūras prasību specifikācija apraksta vēlamo
  funkcionalitāti no lietotāja viedokļa (T.Li.2.)
- **Prasmes:** T.V.1.2.1. · T.O.2.4.4. · T.V.2.3.8. · T.V.2.3.4. · T.V.2.2.1. · T.V.2.3.10.
- **Komplekss SR:** Sava risinājuma izstrādes gaitā izvēlas un izmanto atbilstošus projekta
  vadības rīkus, izveido programmatūras prasību specifikāciju, balstoties uz lietotāja
  vajadzībām, un prezentē to. (T.V.1.2.1., T.V.2.3.8., T.O.2.4.4.)
- **Ieradumi:** Attīsta ieradumu veidot cieņpilnas attiecības, komunicējot ar lietotāju
  (tikums — laipnība) · Attīsta ieradumu izprast un risināt kompleksas problēmas, sadalot
  lielākas problēmas vairākās mazās (tikumi — gudrība, mērenība)
- **Jēdzieni:** ieinteresētā puse, mērķauditorija, lietotāja stāsts, funkcionālā un
  nefunkcionālā prasība, struktūrskice, lietotāja ceļvedis
- **Vērtēšana:** SV4 — specifikācijas aizstāvēšana ar biļetēm

### 05. Tīkls, serveris, drošība, mašīnmācīšanās — 14 st.
**Mērķis:** izveidot vienkāršu tīmekļa serveri ar savu programmsaskarni un saprast, kas
notiek starp pārlūku un serveri.

- **Ziņas:** Pastāv dažādi datortīkli (T.Li.2.) · Šifrētai un nešifrētai datu plūsmai ir
  dažādi pielietojumi (T.Li.3.) · Mašīnmācīšanās palīdz jomās, kurās nav vienkārši
  izmantojamu algoritmu (T.Li.2.)
- **Prasmes:** T.O.2.3.1. · T.V.2.3.1. · T.V.3.1.3. · T.O.3.1.3. · T.O.2.4.18. · T.O.3.2.5.
- **Jēdzieni:** klients, serveris, HTTP, statusa kods, maršruts, IP adrese, maršrutētājs,
  jaucējfunkcija, API atslēga, mašīnmācīšanās, mākslīgais intelekts
- **Vērtēšana:** SV5 — papīra darbs

### 06. Gala projekts: pilns cikls un ieviešana — 24 st.
**Mērķis:** izstrādāt, notestēt, publicēt un prezentēt risinājumu pēc savas specifikācijas.

- **Ziņas:** Izstrādājot programmatūru, ir noteikta veicamo darbību secība (T.Li.2.) ·
  Vizuāli patīkama un ērta saskarne motivē lietotāju izmantot lietotni (T.Li.2.) ·
  Lai aizsargātu savu risinājumu, jāparedz intelektuālā īpašuma aizsardzības veids (T.Li.3.)
- **Prasmes:** T.O.2.4.2. · T.O.2.4.3. · T.O.2.4.7. · T.O.3.1.5. · T.V.3.1.1. · T.V.2.2.3.
- **Komplekss SR:** Ievērojot dizaina procesa soļus, izstrādā projektu, kas ar programmēšanas
  palīdzību atrisina kādu lokālu problēmu. (T.O.1.1.2., T.O.2.4.1., T.O.2.4.8., T.O.2.4.13.)
- **Jēdzieni:** programmatūras izstrādes modelis, iteratīvā izstrāde, akcepttestēšana,
  ieviešana, atvērtā koda licence
- **Vērtēšana:** SV6 — projekts un aizstāvēšana

## Programmēšanas valodas

**Python** paliek domāšanas valoda: objektorientētā pieeja, algoritmi, datu apstrāde — un
tā ir valoda, kurā skolēni kārtos centralizēto eksāmenu 12. klasē.

**SQL** ienāk 02. blokā un paliek līdz gala projektam.

**JavaScript** ienāk 05. blokā tīmekļa daļai — serveris ar Express, klients ar `fetch` un
DOM, bez ietvariem. Mērķis ir, lai skolēns redz visu ķēdi: SQL → serveris → JSON → ekrāns.
Next.js un React ir pieejami kā ★ izvēle 06. blokā tiem, kas grib tālāk.
