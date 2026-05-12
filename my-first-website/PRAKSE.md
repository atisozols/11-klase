# Praktiskais darbs: React un Next.js — bibliotēkas saskarne

**Ilgums:** 120 minūtes
**Vide:** šis projekts (`my-first-website`) un Express servera projekts (`express-with-knex`)

---

## Mērķi

Šī darba laikā tu paplašināsi esošo bibliotēkas saskarni. Tu izmantosi tos backend endpoint-us, kurus mēs uzbūvējām, bet vēl neesam savienojuši ar interfeisu. Vienlaikus tu trenēsies veidot vairāk React komponentes — gan tādas, kas dzīvo serverī un fetcho datus, gan tādas, kuras strādā pārlūkā ar `useState`. Pēc darba tev būs sava bibliotēkas mini-aplikācija ar dinamiskām URL adresēm, atkārtoti izmantojamām komponentēm un interaktīviem elementiem.

## Sākotnējais stāvoklis

Pirms sākt, atver projekta mapi un saproti, kas jau eksistē:

- `app/library/authors/page.js` — izvada autoru sarakstu ar saitēm uz `/library/authors/[id]`, **bet šī dinamiskā lapa vēl neeksistē** (saites tagad ved uz 404).
- `app/library/books/page.js` — izvada visu grāmatu sarakstu vienā vienkāršā `<p>` rindā.
- `app/library/students/page.js` — izvada visu skolēnu sarakstu.
- `components/` mapē ir gatavi piemēri: `BusinessCard`, `Collapsible`, `PlusMinus`, kā arī `tennis/PlayerCard` un `tennis/TennisHeader`. Ieskaties tajos, ja aizmirsies, kā izskatās komponente ar props vai ar `useState`.

Backend serveris jau prot atbildēt uz daudz vairāk endpointiem nekā pašlaik tiek izmantots. Atver `express-with-knex/routes/` mapi un skaties, kādas `GET` adreses tur ir definētas — tās tu šodien izmantosi.

## Sagatavošana (5 min)

1. Vienā terminālī palaiž backend serveri (`npm run dev` mapē `express-with-knex`). Pārliecinies, ka adresē `http://localhost:5001/authors` saņem JSON ar autoriem.
2. Otrā terminālī palaid front-end serveri (`npm run dev` šajā mapē) un atver `http://localhost:3000/library/authors`.
3. Izveido sev darba mapju struktūras priekšstatu — pārlūko `app/library/` un `components/` mapes IDE sānjoslā, lai darba laikā nezaudē laiku ar meklēšanu.

---

## 1. uzdevums — Autora detalizētais skats ar dinamisku URL (20 min)

Pievērs uzmanību, ka `app/library/authors/page.js` jau veido saites formā `/library/authors/1`, bet šī adrese pašlaik atgriež 404. Tagad to salabosim.

**Ko darīt:**

- Mapē `app/library/authors/` izveido jaunu apakšmapi ar nosaukumu `[id]`. Kvadrātiekavas šeit ir nopietni svarīgas — Next.js tās izmanto kā signālu, ka šī ir dinamiska URL daļa.
- Šajā mapē izveido `page.js`. Komponente saņems argumentu, no kura var izvilkt `id` no URL. Skatīties var kā `params` objektu — uz to atsaucies dokumentācijā mapē `node_modules/next/dist/docs/`, ja neesi drošs par sintaksi.
- Funkcijai jābūt `async`, jo iekšā tu izsauksi `fetch` uz `http://localhost:5001/authors/<id>/books`. Šis endpoint atgriež objektu ar autora vārdu un viņa grāmatu sarakstu — atver `routes/authors/index.js`, lai redzētu precīzu formātu.
- Izvadi autora vārdu kā virsrakstu un zem tā ciklu pa grāmatām ar `map()`. Katrai grāmatai parādi nosaukumu un izdošanas gadu.

**Padomi:**

- Atceries `key` prop — bez tā React izvadīs brīdinājumu konsolē. `key` jāuzliek tieši uz tā elementa, ko atgriež `map()`.
- Ja `fetch` rezultāts izskatās dīvains, vienmēr vari pievienot `console.log` — tas izvadīsies servera terminālī, jo komponente ir server component, nevis pārlūkā.
- Ja URL adresē ievadīsi neeksistējošu id, backend atgriezīs 404 ar JSON `{ error: ... }`. Šī uzdevuma ietvaros nav obligāti to skaisti apstrādāt, bet padomā, kā tas izskatītos.

**Pārbaude:** uzklikšķini uz autora vārda autoru sarakstā un pārliecinies, ka atveras lapa ar viņa grāmatām.

---

## 2. uzdevums — Atkārtoti izmantojama `BookCard` komponente (15 min)

Šobrīd grāmatas tiek izvadītas kā vienkāršs teksts. Mēs grāmatu attēlošanu tagad izmantosim divās vietās — sarakstā un autora lapā — tāpēc loģiski uz to izveidot atsevišķu komponenti.

**Ko darīt:**

- Mapē `components/` izveido jaunu failu `BookCard.jsx`. Vadies pēc `BusinessCard.jsx` parauga — tā ir vienkārša prezentācijas komponente bez stāvokļa.
- Komponente lai saņem props: grāmatas nosaukumu, autora vārdu un izdošanas gadu. Vairākus props vienlaikus ir ērti destrukturēt jau funkcijas argumentu sarakstā, līdzīgi kā tas darīts `PlayerCard.jsx`.
- Noformē ar Tailwind klasēm — kartiņa ar maliņu, mazliet padding-u, atstarpe starp kartiņām. Mēģini nepiekrāsot pārāk daudz, bet panākt, lai vizuāli skaidri redzams, kur viena grāmata beidzas un sākas otra.
- Izmanto šo komponenti gan `app/library/books/page.js` failā, gan tikko izveidotajā autora detalizētajā lapā.

**Padomi:**

- Ja grāmatas atribūti dažādos endpointos saucās dažādi (piem., `name` pret `title`, vai autors atrodas iekšā objektā vai blakus), tad uz lapas pirms padošanas komponentei sakārto datus tā, lai komponente vienmēr saņem to pašu props nosaukumu kopu. Komponente nedrīkst zināt, no kura endpointa nāca dati.
- Default vērtības props var uzlikt tāpat kā `BusinessCard.jsx` — tas palīdz, kad lauks ir tukšs.

**Pārbaude:** abas lapas izvada grāmatas vizuāli vienādās kartiņās. Ja kaut kur trūkst autora vai gada — pārliecinies, ka padevi pareizos props.

---

## 3. uzdevums — Grāmatas detalizētais skats ar pieejamību (20 min)

Backend prot atbildēt uz `GET /books/:id/availability` un atgriež informāciju, vai grāmata šobrīd ir aizņemta vai pieejama. Izveidosim lapu, kas to parāda.

**Ko darīt:**

- Pārveido `app/library/books/page.js` tā, lai katra grāmata ir saite uz `/library/books/<id>` (analoģiski tam, kā autoru lapā ir saites uz `/library/authors/<id>`). Iespējams, ka šeit ērtāk saiti ielikt iekšā `BookCard` komponentē, bet padomā, vai tā gribi vienmēr — ne vienmēr karte ir saite. Pārdomā, kurā līmenī (lapā vai komponentē) saiti ievietot.
- Mapē `app/library/books/` izveido `[id]/page.js`. Tā ir async server component, kas no URL paņem grāmatas id un izsauc `fetch` uz `availability` endpointu.
- Ja grāmata ir pieejama, izvadi to lielā zaļā tekstā (vai citā skaidri pozitīvā stilā). Ja nav pieejama, izvadi sarkanā tekstā, kā arī parādi, no kura datuma tā ir aizņemta. Atver backend kodu un saproti, kāds tieši lauks atnāk atpakaļ — tev jāstrādā ar reāliem datu nosaukumiem, ne minējumiem.

**Padomi:**

- Nosacījumiem JSX iekšienē var lietot ternaro operatoru `condition ? <A /> : <B />` vai īsslēgumu `condition && <A />`. Pirmais der, kad ir abi gadījumi; otrais, kad vēlies kaut ko rādīt tikai tad, ja nosacījums ir patiess.
- Datums no servera atnāk kā teksts ISO formātā. Ja vēlies to pasniegt skaistāk, lasītājam draudzīgāk, vari izmantot `new Date(...).toLocaleDateString("lv-LV")`.
- Pievieno arī saiti vai pogu “Atpakaļ uz visām grāmatām”, lai navigācija būtu loģiska.

**Pārbaude:** atver vairāku grāmatu detalizētās lapas. Vismaz vienai vajadzētu būt aizņemtai (skat. testa datus `GUIDE.md` failā backend mapē).

---

## 4. uzdevums — Aizņemšanās vēsture ar atveramu komponenti (15 min)

Tajā pašā grāmatas detalizētajā lapā tagad parādīsim arī tās aizņemšanās vēsturi. Endpoint `GET /books/:id/history` atgriež visus aizņēmumus konkrētajai grāmatai kopā ar skolēna informāciju.

**Ko darīt:**

- Tajā pašā `[id]/page.js` failā izsauc otru `fetch` — uz `history` endpointu. Abus var izsaukt paralēli, izmantojot `Promise.all`, vai vienkārši secīgi ar diviem `await`. Pirmais variants ir ātrāks, bet abi strādā.
- Vēsturi izvadi kā tabulu vai sarakstu zem pieejamības informācijas. Katrai rindai parādi skolēna vārdu, aizņemšanās datumu un atgriešanas datumu (vai tekstu “vēl nav atgriezta”, ja `returned_at` ir `null`).
- Izveido jaunu komponenti, piemēram `BorrowingHistory.jsx`, kas saņem vēstures masīvu kā props un to izvada. Tā paliks atkārtoti izmantojama 6. uzdevumam.

**Padomi:**

- Padomā, vai izvadīt **visu** vēsturi uzreiz, vai paslēpt to aiz pogas “Rādīt vēsturi”. Ja vēlies pogu, šī komponente kļūst par client component (pievieno `"use client"` augšā) un izmanto `useState` līdzīgi kā `Collapsible.jsx`. Tas ir labs piemērs tam, kā vienā lapā var sadarboties server un client komponentes.
- Ja iztaisīsi atveramu vēsturi — pārliecinies, ka data fetch joprojām notiek serverī un masīvs tiek **padots** kā props uz client komponenti. Client komponente nedrīkst pati saukt `fetch` uz backend šajā uzdevumā.

**Pārbaude:** atver grāmatas, kurai testa datos ir aizņemšanās vēsture (piemēram, “Uguns un nakts”). Pārliecinies, ka redzami gan atgrieztie, gan vēl neatgrieztie ieraksti.

---

## 5. uzdevums — Skolēna profils ar filtrējamu aizņēmumu sarakstu (25 min)

Tagad lielākais šodienas uzdevums. Skolēna lapā parādīsim viņa pamatinformāciju un aizņēmumu sarakstu, kuru lietotājs varēs filtrēt.

**Ko darīt:**

- Mapē `app/library/students/` izveido `[id]/page.js`. Šī lapa izsauks **divus** endpointus: `GET /students/:id` (skolēna pamatinfo) un `GET /borrowings/:studentId` (visi viņa aizņēmumi).
- Augšpusē izvadi skolēna vārdu un e-pastu kā profila “galviņu”.
- Aizņēmumu sarakstam izmanto iepriekšējā uzdevumā veidoto `BorrowingHistory` komponenti vai izveido jaunu — kā tev liekas tīrāk. Ja iepriekš tā saņēma vēsturi par grāmatu, padomā, vai šis konteksts (vēsture par skolēnu) tiešām ir tas pats — varbūt vajag mazas izmaiņas vai citu komponenti.
- Jāizveido **filtrs**: poga vai pārslēdzējs, kas ļauj rādīt visus aizņēmumus vai tikai aktīvos (vēl neatgrieztos). Backend jau prot to izdarīt — `GET /borrowings/:studentId?active=true`.
- Pārslēdzēja loģika dzīvos client komponentē. Padomā: vai tu vēlies, lai client komponente pati izsauc `fetch` ar atjaunoto URL katru reizi, vai labāk lai serveris atsūta visus datus un client komponente tos vienkārši filtrē atmiņā ar `.filter()`. Abi ir derīgi, tikai pamato sev, kāpēc izvēlies vienu.

**Padomi:**

- Ja izvēlies, ka client komponente pati fetcho — tev būs jāizmanto `useState` un `useEffect` kombinācija. `useEffect` darbojas līdzīgi kā `PlusMinus.jsx` piemērā: tas izpildās, kad mainās konkrēts mainīgais. Šeit šis mainīgais būs filtra stāvoklis.
- Ja izvēlies filtrēt klienta pusē — vienkāršāks variants, bet padomā, vai tas labi mērogojas, ja ierakstu būtu tūkstoši. Klasē varam to pārrunāt.
- Izmanto stāvokļa pārslēgšanai vai nu pogu (kā `PlusMinus.jsx`), vai HTML `<input type="checkbox">`. Ja izvēlies checkbox — tas ir “controlled component”, kuram jāuzliek gan `checked`, gan `onChange`.
- Vizuāli skaidri parādi, ka filtrs ir aktīvs (piemēram, izceltu pogu vai uzrakstu “Rādīti tikai aktīvi aizņēmumi”).

**Pārbaude:** atver skolēnu, kuram testa datos ir gan atgrieztas, gan neatgrieztas grāmatas (piemēram, Anna Berziņa). Pārliecinies, ka filtrs tiešām maina redzamo sarakstu un nekas “nemirgo” ar pirmajiem datiem.

---

## 6. uzdevums (papildus, ja paliek laiks) — Meklēšana grāmatu sarakstā (10 min)

Ja ātri tiec galā ar pamata uzdevumiem, pievieno meklēšanas lauku grāmatu sarakstā.

**Ko darīt:**

- Pārveido `app/library/books/page.js` (vai tās daļu) par client komponenti, kurai ir `useState` ar meklēšanas tekstu un `<input>` lauks.
- Filtrē grāmatu sarakstu pēc nosaukuma vai autora, izmantojot `.filter()` un `.toLowerCase()`, lai meklēšana nav reģistrjutīga.
- Padomā, vai vēlies turēt visu grāmatu fetcho serverī (server komponentē), kas padod datus klienta filtrēšanas komponentei kā props, vai pārcelt visu uz klientu. Pirmais variants ir tīrāks: dati nāk no servera vienreiz, klients tikai filtrē.

---

## Iesniegšana un atrādīšana

Kad esi pabeidzis, demonstrē:

1. Autora detalizēto lapu ar viņa grāmatām.
2. `BookCard` komponenti, ko izmanto vairākās vietās.
3. Grāmatas detalizēto lapu ar pieejamību un vēsturi.
4. Skolēna profilu ar darbojošos filtru.
5. Komponenšu mapi un atver vienu komponenti, lai parādītu, kā tā ir uzbūvēta.

Tev jāspēj atbildēt uz šādiem jautājumiem:

- Kāpēc daži faili sākas ar `"use client"` un citi ne?
- Kā Next.js zina, ka `[id]` ir dinamiska URL daļa?
- Kā tava komponente saņem datus — kā props vai pati izsauc `fetch`?
- Kur tieši tavā kodā tiek lietots `map()` un kāpēc tur ir `key` prop?

---

## Vērtēšanas kritēriji (orientējoši)

| Kritērijs                                                | Svars |
| -------------------------------------------------------- | ----- |
| 1. uzdevums (dinamisks autora skats)                     | 20%   |
| 2. uzdevums (atkārtoti izmantojama komponente)           | 15%   |
| 3.–4. uzdevums (grāmatas skats ar pieejamību un vēsturi) | 30%   |
| 5. uzdevums (skolēna profils ar filtru)                  | 25%   |
| Koda kārtīgums, mapju struktūra, Tailwind lietojums      | 10%   |
| Bonus par 6. uzdevumu                                    | +5%   |

**Veiksmi!**
