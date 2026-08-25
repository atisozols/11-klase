# Gala projekts — ceļvedis

**Izstrādes laiks:** 11-077 – 11-098 (22 stundas) · **Aizstāvēšana:** 11-099, 11-100
**Vērtējums:** SV6 — 35 % no gada vērtējuma

Darba uzdevums ir **tava paša specifikācija** no 04. bloka. Nekas jauns nav jāizdomā —
jāizpilda tas, ko pats uzrakstīji.

## Repozitorija struktūra

```
mans-projekts/
├── SPECIFIKACIJA.md    no 04. bloka, ar atzīmētām izmaiņām
├── README.md           apraksts, ekrānuzņēmums, kā palaist, saite uz publicēto versiju
├── TESTI.md            testa plāns un rezultāti
├── PASPARBAUDE.md      prasību izpildes tabula
├── LICENSE             izvēlētā licence
├── shema.sql           datubāzes izveides skripts
├── serveris/           Express + Knex
└── klients/            HTML, CSS, JavaScript
```

## Termiņi

| Kad | Kas jābūt gatavam |
| --- | --- |
| 11-078 | datubāze ar visām tabulām un testa datiem |
| 11-082 | serveris atgriež datus, lapa tos rāda, forma tos pievieno |
| **11-084** | **1. starpposms:** demonstrācija, pamata funkcionalitāte strādā |
| 11-089 | testa plāns |
| **11-092** | **2. starpposms:** visas obligātās prasības izpildītas |
| 11-094 | publicēts internetā |
| 11-098 | dokumentācija, licence, pašpārbaude |

## Tehniskās prasības

- datubāze SQLite ar vismaz **trim** saistītām tabulām;
- serveris ar vismaz **trim** maršrutiem, no kuriem vismaz viens ir `POST`;
- validācija **servera pusē** visur, kur specifikācija to prasa;
- klienta puse: HTML, CSS un vanilla JavaScript ar `fetch`;
- kods sadalīts failos; funkcijas nav garākas par 30 rindām;
- commit pēc katras izstrādes stundas.

**Ietvari (React, Next.js) nav obligāti un nav vajadzīgi.** Ja gribi tos izmantot, tā ir
★ izvēle — bet vispirms jāstrādā versijai bez tiem.

## Publicēšana

Divi ceļi, abi bez maksas:

- **GitHub Pages** — der, ja klienta daļa var strādāt bez sava servera;
- **Render** (bezmaksas konts) — der visai lietotnei kopā ar serveri un datubāzi.

Publicētā versija jāpārbauda no cita datora vai telefona. Saite jāieliek `README.md`.

## Kā tiek vērtēts

Vērtē gan projektu, gan aizstāvēšanu. Aizstāvēšanā tev būs:

1. jāparāda, kā risinājums strādā;
2. jāatbild uz jautājumiem par savu kodu;
3. **jāveic tajā neliela izmaiņa uz vietas.**

Projekts, kuru tu nespēj paskaidrot un mainīt, netiek novērtēts neatkarīgi no tā, cik labi
tas strādā. Tas nav sods — komplekss sasniedzamais rezultāts pēc definīcijas nozīmē, ka tu
pats spēj rīkoties jaunā situācijā.

## Ja pietrūkst laika

Tas ir normāli un paredzēts. 04. blokā tu uzrakstīji sarakstu «ko izmetīšu» — tagad tas
noder. Godīgi pārceļ prasību uz sadaļu «ārpus apjoma», pieraksti, kāpēc, un pabeidz pārējo.

Nepabeigts projekts ar godīgu pašpārbaudi tiek vērtēts augstāk nekā projekts, kura
pašpārbaudē visur rakstīts «izpildīts», bet demonstrācijā tas nav tiesa.
