# 05. Tīkls, serveris, drošība, mašīnmācīšanās

**14 stundas (11-063 – 11-076)** · Standarta 5. temats “Kā izvēlēties un efektīvi savā
projektā izmantot jau esošu risinājumu?”

**Bloka mērķis:** izveidot vienkāršu tīmekļa serveri ar savu programmsaskarni un saprast,
kas notiek starp pārlūku un serveri.

**Teorija un piemēri:** [`teorija.js`](teorija.js) · **Darba fails:** [`uzdevumi.js`](uzdevumi.js)
**Datubāze:** izmantojam to pašu [`skola.db`](../02-datubazes/skola.db)
**Noslēgums:** SV5 — papīra darbs (11-076)

**Rīki.** Node.js, Express, Knex un `sqlite3` draiveris. Datubāze ir tā pati, ko lietojām
iepriekšējā blokā — nekāds serveris nav jāuzstāda.

```bash
npm init -y
npm install express knex sqlite3
```

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 05-tikls-un-serveris/README.md && python3 bin/darbafails.py 05-tikls-un-serveris -->

| Nr. | Tēma | Sasniedzamais rezultāts |
| --- | --- | --- |
| 11-063 | Klienta un servera arhitektūra. Kas notiek, atverot tīmekļa lapu. | Apraksta soļus no adreses ievadīšanas līdz lapas parādīšanai. |
| 11-064 | HTTP protokols. Pieprasījums, atbilde, statusa kodi. | Izpēta tīkla pieprasījumus pārlūka rīkos un skaidro statusa kodus. |
| 11-065 | Node.js un Express. Servera izveide. | Izveido un palaiž tīmekļa serveri, kas atbild uz pieprasījumu. |
| 11-066 | Maršruti ar parametriem. JSON atbilde. | Veido maršrutus ar parametriem un atgriež datus JSON formātā. |
| 11-067 | Datu pieprasīšana no pārlūka. `fetch` un DOM. | Pieprasa datus no sava servera un attēlo tos lapā. |
| 11-068 | Knex un SQLite. Datubāzes pieslēgšana serverim. | Pieslēdz datubāzi serverim un atgriež no tās datus. |
| 11-069 | Pilna datu ķēde: datubāze → serveris → JSON → pārlūks. | Izveido risinājumu, kurā dati no datubāzes nonāk līdz lietotāja ekrānam. |
| 11-070 | Datu sūtīšana uz serveri. Formas un POST pieprasījumi. | Pieņem serverī lietotāja ievadītos datus un saglabā tos datubāzē. |
| 11-071 | Kļūdu apstrāde un statusa kodi servera pusē. | Atgriež pareizu statusa kodu un saprotamu paziņojumu katrā kļūdas gadījumā. |
| 11-072 | Lokālais tīkls. IP adreses, maršrutētājs, portu pāradresācija. | Skaidro lokālā tīkla uzbūvi un konfigurē piekļuves punktu. |
| 11-073 | HTTPS, paroļu glabāšana, jaucējfunkcijas. | Skaidro, kāpēc paroles neglabā atklātā tekstā, un lieto jaucējfunkciju. |
| 11-074 | Mašīnmācīšanās pamatprincipi. Atšķirība no algoritma. | Skaidro, ar ko mašīnmācīšanās atšķiras no parasta algoritma un kas tai nepieciešams. |
| 11-075 | Gatava mašīnmācīšanās risinājuma izmantošana. Ētikas jautājumi. | Izmanto gatavu modeli un izvērtē tā lietojuma ietekmi. |
| 11-076 | Pārbaudes darbs: klients un serveris, HTTP, drošība, mašīnmācīšanās. | Demonstrē bloka sasniedzamos rezultātus patstāvīgā darbā. |

<!-- TABULA:BEIGAS -->

---

## 11-063 · Klients un serveris
`teorija` · `teorija.js` §1

**Tēma:** Klienta un servera arhitektūra. Kas notiek, atverot tīmekļa lapu.
**SR:** Apraksta soļus no adreses ievadīšanas līdz lapas parādīšanai.
**Standarts:** T.Li.2. · T.V.2.3.1.

**Gaita**
- 10' — uz tāfeles kopā izsekojam, kas notiek, ievadot adresi pārlūkā
- 10' — DNS, IP adrese, pieprasījums, atbilde
- 15' — uzdevumi
- 5' — kur šajā ķēdē ir mūsu 02. bloka datubāze

**Uzdevumi**
1. Burtnīcā: uzzīmē soļus no adreses ievadīšanas līdz lapas parādīšanai.
2. Burtnīcā: pieraksti, kura daļa notiek tavā datorā un kura — kaut kur citur.
3. Ar komandu `ping` noskaidro kādas vietnes IP adresi un pieraksti to.
4. ★ Noskaidro, cik ilgi ceļo pieprasījums līdz serverim Latvijā un līdz serverim ASV.
   Kāpēc atšķiras?

**Mājasdarbs:** 1. uzdevums

## 11-064 · HTTP
`prakse` · `teorija.js` §2

**Tēma:** HTTP protokols. Pieprasījums, atbilde, statusa kodi.
**SR:** Izpēta tīkla pieprasījumus pārlūka rīkos un skaidro statusa kodus.
**Standarts:** T.V.2.3.1. · T.Li.2.

**Gaita**
- 5' — HTTP ir saruna: pieprasījums un atbilde
- 10' — DevTools cilne Network uz reālas lapas
- 20' — uzdevumi
- 5' — metodes GET un POST: ar ko atšķiras

**Uzdevumi**
5. Atver DevTools cilni Network un pieraksti, cik pieprasījumu veic viena mājaslapa.
6. Atrodi vienu pieprasījumu un pieraksti tā metodi, statusa kodu un atbildes izmēru.
7. Atrodi lapu, kas atgriež 404, un pieraksti, kā pārlūks to parāda.
8. Pieraksti, ko nozīmē kodi 200, 301, 400, 401, 404, 500.
9. ★ Atrodi pieprasījumu, kas atgriež JSON, nevis HTML, un pieraksti tā adresi.

**Mājasdarbs:** 8. uzdevums

## 11-065 · Pirmais serveris
`prakse` · `teorija.js` §3

**Tēma:** Node.js un Express. Servera izveide.
**SR:** Izveido un palaiž tīmekļa serveri, kas atbild uz pieprasījumu.
**Standarts:** T.O.2.3.1. · T.O.2.4.11.

**Gaita**
- 5' — Node ir Python, tikai JavaScript un serverī
- 10' — demo §3: `npm init`, `npm install express`, pirmais maršruts
- 20' — uzdevumi
- 5' — kāpēc serveris «karājas» un kā to apturēt

**Uzdevumi**
10. Izveido projektu ar `npm init -y` un uzstādi Express.
11. Uzraksti serveri, kas uz `/` atbild ar tekstu `Sveika, pasaule`.
12. Pievieno maršrutu `/laiks`, kas atgriež pašreizējo laiku.
13. Pievieno maršrutu `/sveiciens/anna`, kas atbild ar `Sveika, anna`.
14. ★ Pievieno maršrutu, kas atgriež nejaušu skaitli no 1 līdz 6, un atsvaidzini lapu
    piecas reizes.

**Mājasdarbs:** 12. uzdevums

## 11-066 · Maršruti un JSON
`prakse` · `teorija.js` §4

**Tēma:** Maršruti ar parametriem. JSON atbilde.
**SR:** Veido maršrutus ar parametriem un atgriež datus JSON formātā.
**Standarts:** T.O.2.4.11. · T.O.2.4.14.

**Gaita**
- 5' — atkārtojums: JSON no 03. bloka, tagad no otras puses
- 10' — demo §4: `res.json()`, `req.params`, `req.query`
- 20' — uzdevumi
- 5' — kā izskatās mūsu API atbilde pārlūkā

**Uzdevumi**
15. Izveido maršrutu `/skoleni`, kas atgriež JSON masīvu ar trim izdomātiem skolēniem.
16. Izveido maršrutu `/skoleni/:id`, kas atgriež vienu skolēnu pēc `id`.
17. Ja tāda `id` nav, atgriez statusa kodu 404 un paskaidrojumu JSON formātā.
18. Izveido maršrutu, kas pieņem parametru `?klase=11.a` un atgriež tikai tos skolēnus.
19. ★ Pievieno parametru `?kartot=uzvards` un atgriez sakārtotu sarakstu.

**Mājasdarbs:** 16. uzdevums

## 11-067 · Klients: fetch un DOM
`prakse` · `teorija.js` §5

**Tēma:** Datu pieprasīšana no pārlūka. `fetch` un DOM.
**SR:** Pieprasa datus no sava servera un attēlo tos lapā.
**Standarts:** T.O.2.4.11. · T.V.2.3.10.

**Gaita**
- 5' — tagad esam otrā pusē: pārlūks prasa, serveris atbild
- 10' — demo §5: `fetch`, `await`, `document.createElement`
- 20' — uzdevumi
- 5' — kāpēc dati parādās ar aizkavi

**Uzdevumi**
20. Izveido HTML lapu, kas ar `fetch` paņem datus no `/skoleni` un izvada tos konsolē.
21. Attēlo saņemtos skolēnus kā sarakstu lapā.
22. Attēlo tos tabulā ar diviem stabiņiem.
23. Pievieno pogu, kas datus pārlādē no jauna.
24. ★ Pievieno ievades lauku, kas filtrē sarakstu pēc uzvārda, nepieprasot datus no jauna.

**Mājasdarbs:** 21. uzdevums

## 11-068 · Datubāze serverī
`prakse` · `teorija.js` §6

**Tēma:** Knex un SQLite. Datubāzes pieslēgšana serverim.
**SR:** Pieslēdz datubāzi serverim un atgriež no tās datus.
**Standarts:** T.O.2.4.17. · T.O.2.3.4.

**Gaita**
- 5' — līdz šim dati bija kodā; tagad tie nāk no `skola.db`
- 10' — demo §6: `knexfile`, savienojums, pirmais vaicājums
- 20' — uzdevumi
- 5' — kāpēc SQL vairs neraksta ar rokām — un kāpēc tomēr jāprot

**Uzdevumi**
25. Pieslēdz `skola.db` savam serverim ar Knex un izvadi skolēnu skaitu konsolē.
26. Pārtaisi maršrutu `/skoleni` tā, lai dati nāk no datubāzes.
27. Izveido maršrutu `/klases`, kas atgriež klases ar skolēnu skaitu katrā.
28. Izveido maršrutu `/skoleni/:id/atzimes`, kas atgriež viena skolēna atzīmes ar priekšmetu
    nosaukumiem.
29. ★ Pievieno maršrutu, kas atgriež katras klases vidējo atzīmi, sakārtotu dilstoši.

**Mājasdarbs:** 26. uzdevums

## 11-069 · Pilna ķēde
`prakse` · FV9 (dators)

**Tēma:** Pilna datu ķēde: datubāze → serveris → JSON → pārlūks.
**SR:** Izveido risinājumu, kurā dati no datubāzes nonāk līdz lietotāja ekrānam.
**Standarts:** T.O.2.4.11. · T.O.2.4.17.

**Gaita**
- 5' — uz tāfeles visa ķēde vienā zīmējumā
- 20' — patstāvīgs darbs
- 15' — **FV9** pie datora

**Uzdevumi**
30. Izveido lapu, kas rāda visu klašu sarakstu ar skolēnu skaitu, ņemot datus no datubāzes.
31. Pievieno iespēju uzklikšķināt uz klases un redzēt tās skolēnus.
32. ★ Pievieno katram skolēnam vidējo atzīmi, aprēķinātu datubāzē, nevis pārlūkā.

**Mājasdarbs:** pabeigt 31. uzdevumu

## 11-070 · POST un formas
`prakse` · `teorija.js` §7

**Tēma:** Datu sūtīšana uz serveri. Formas un POST pieprasījumi.
**SR:** Pieņem serverī lietotāja ievadītos datus un saglabā tos datubāzē.
**Standarts:** T.O.2.4.17. · T.V.2.3.5.

**Gaita**
- 5' — GET prasa, POST sūta
- 10' — demo §7: `express.json()`, `req.body`, `fetch` ar `method: "POST"`
- 20' — uzdevumi
- 5' — kāpēc serverim jāpārbauda dati, arī ja forma tos jau pārbaudīja

**Uzdevumi**
33. Pievieno maršrutu `POST /pulcini`, kas pieņem jaunu pulciņu un ievieto to datubāzē.
34. Izveido formu lapā, kas nosūta datus uz šo maršrutu.
35. Pievieno validāciju serverī: nosaukums nedrīkst būt tukšs, vietu skaits — pozitīvs.
36. Ja dati nav derīgi, atgriez statusa kodu 400 un paskaidrojumu.
37. ★ Pēc veiksmīgas pievienošanas atsvaidzini sarakstu lapā, nepārlādējot visu lapu.

**Mājasdarbs:** 34. uzdevums

## 11-071 · Kļūdu apstrāde serverī
`prakse` · `teorija.js` §8

**Tēma:** Kļūdu apstrāde un statusa kodi servera pusē.
**SR:** Atgriež pareizu statusa kodu un saprotamu paziņojumu katrā kļūdas gadījumā.
**Standarts:** T.V.1.3.2. · T.O.3.1.3.

**Gaita**
- 5' — ko rāda lietotājs, kad kaut kas nestrādā?
- 10' — demo §8: `try`/`catch` maršrutā, 400 pret 404 pret 500
- 20' — uzdevumi
- 5' — kāpēc kļūdas paziņojumā nedrīkst būt datubāzes teksts

**Uzdevumi**
38. Papildini visus savus maršrutus ar `try`/`catch`.
39. Atgriez 404, ja ieraksta nav, un 400, ja dati nav derīgi.
40. Pārbaudi, kas notiek, ja datubāzes fails ir pārsaukts. Panāc, lai serveris nekrīt.
41. Attēlo kļūdas paziņojumu lapā lietotājam saprotamā valodā.
42. ★ Pieraksti, kāpēc kļūdas tekstā nedrīkst nokļūt SQL vaicājums vai faila ceļš.

**Mājasdarbs:** 39. uzdevums

## 11-072 · Lokālais tīkls
`jaukta` · `teorija.js` §9

**Tēma:** Lokālais tīkls. IP adreses, maršrutētājs, portu pāradresācija.
**SR:** Skaidro lokālā tīkla uzbūvi un konfigurē piekļuves punktu.
**Standarts:** T.O.2.3.1. · T.V.2.3.1. · T.O.3.1.3.

**Gaita**
- 10' — lokālā un publiskā IP adrese; kāpēc `localhost` neredz kaimiņš
- 10' — maršrutētāja konfigurācija: demonstrācija ar īstu maršrutētāju
- 15' — uzdevumi, pāros ar telefona karstvietu
- 5' — kādi drošības riski rodas, atverot serveri tīklam

**Uzdevumi**
43. Noskaidro sava datora lokālo IP adresi un pieraksti to.
44. Palaid savu serveri un atver to no klasesbiedra datora, izmantojot IP adresi.
45. Pāros: izveido telefona karstvietu ar paroli un pieslēdz tai otru ierīci.
46. Pieraksti, ar ko atšķiras lokālā un publiskā IP adrese.
47. ★ Noskaidro, kas ir portu pāradresācija, un pieraksti, kāpēc tā ir drošības risks.

**Mājasdarbs:** 46. uzdevums

## 11-073 · Drošība
`jaukta` · `teorija.js` §10

**Tēma:** HTTPS, paroļu glabāšana, jaucējfunkcijas.
**SR:** Skaidro, kāpēc paroles neglabā atklātā tekstā, un lieto jaucējfunkciju.
**Standarts:** T.V.3.1.3. · T.O.3.1.3.

**Gaita**
- 10' — kas notiek ar datiem HTTP un HTTPS savienojumā
- 10' — demo §10: jaucējfunkcija; kāpēc to nevar apgriezt
- 15' — uzdevumi
- 5' — ko darīt, ja datubāze noplūst

**Uzdevumi**
48. Uzraksti programmu, kas aprēķina teksta jaucējvērtību, un pārbaudi, ka vienādam tekstam
    tā vienmēr ir vienāda.
49. Pārbaudi, kas notiek ar jaucējvērtību, ja tekstā maina vienu burtu.
50. Pievieno savai datubāzei tabulu `lietotaji`, kurā parole glabājas kā jaucējvērtība.
51. Uzraksti pārbaudi, kas salīdzina ievadīto paroli ar saglabāto.
52. ★ Noskaidro, kas ir «sāls» (salt) un kāpēc ar to jaucējvērtība kļūst drošāka.

**Mājasdarbs:** 49. uzdevums

## 11-074 · Mašīnmācīšanās
`teorija` · FV10 (papīrs)

**Tēma:** Mašīnmācīšanās pamatprincipi. Atšķirība no algoritma.
**SR:** Skaidro, ar ko mašīnmācīšanās atšķiras no parasta algoritma un kas tai nepieciešams.
**Standarts:** T.O.2.4.18. · T.O.3.2.5.

**Gaita**
- 15' — **FV10** uz papīra, datori vēl aizvērti
- 10' — algoritms: mēs uzrakstām likumus. Mašīnmācīšanās: mēs dodam piemērus
- 10' — vadītā un nevadītā mācīšanās; kāpēc ievaddati ir viss
- 5' — kur to jau lieto: ieteikumi, sejas atpazīšana, tulkošana

**Uzdevumi**
53. Burtnīcā: dotajiem pieciem uzdevumiem atzīmē, kuriem der parasts algoritms un kuriem
    mašīnmācīšanās.
54. Burtnīcā: pieraksti, kādi dati būtu vajadzīgi, lai iemācītu programmu atpazīt surogātpastu.
55. ★ Pieraksti piemēru, kur nepilnīgi ievaddati padarītu teorētiski labu risinājumu par
    nederīgu.

**Mājasdarbs:** 54. uzdevums

## 11-075 · Mašīnmācīšanās praksē un ētika
`jaukta`

**Tēma:** Gatava mašīnmācīšanās risinājuma izmantošana. Ētikas jautājumi.
**SR:** Izmanto gatavu modeli un izvērtē tā lietojuma ietekmi.
**Standarts:** T.O.2.4.18. · T.O.3.2.5. · Ieradumi

**Gaita**
- 15' — izmēģinām gatavu risinājumu un aplūkojam, kur tas kļūdās
- 10' — diskusija: kas atbild, ja algoritms kļūdās? Kas notiek, ja dati ir neobjektīvi?
- 10' — atkārtojums pirms SV5
- 5' — kas būs pārbaudes darbā

**Uzdevumi**
56. Izmēģini gatavu tiešsaistes risinājumu un atrodi gadījumu, kad tas kļūdās.
57. Pieraksti, kāpēc, tavuprāt, tas kļūdījās.
58. Diskusijai: uzraksti vienu argumentu par un vienu pret mašīnmācīšanās lietošanu skolēnu
    darbu vērtēšanā.
59. ★ Atrodi rakstu par neobjektīviem datiem mašīnmācīšanā un uzraksti trīs teikumu kopsavilkumu.

**Mājasdarbs:** gatavoties SV5

## 11-076 · Pārbaudes darbs
`pārbaudes darbs`

**Tēma:** Pārbaudes darbs: klients un serveris, HTTP, drošība, mašīnmācīšanās.
**SR:** Demonstrē bloka sasniedzamos rezultātus patstāvīgā darbā.
**Standarts:** viss bloks

**Gaita**
- 40' — darbs uz papīra, datori aizvērti

**Materiāli:** SV5 — divi varianti, papīra darbs (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Šis ir tas brīdis, kur viss saliekas kopā.** 02. bloka datubāze, 03. bloka JSON un
  10. klases DOM prasmes 11-069 stundā beidzot ir viena ķēde. Uzzīmē to uz tāfeles un
  atstāj tur līdz bloka beigām.
- **Bez ietvariem.** Nekāda React vai Next.js — tikai HTML, `fetch` un `document`. Mērķis ir,
  lai skolēns redz mehānismu, ne abstrakciju. Ietvars ir 06. bloka ★ izvēle tiem, kas grib.
- **JavaScript ir otrā valoda, ne aizstājēja.** Python paliek algoritmiem un eksāmenam;
  JavaScript ir tīmeklim. Skolēnam to pasaki tieši šādi, citādi rodas iespaids, ka mācāmies
  visu no jauna.
- **Maršrutētājs.** Ja kabinetā nav pieejams īsts maršrutētājs, 11-072 strādā ar telefona
  karstvietu — to paredz arī standarts. Galvenais, ko skolēnam saprast: `localhost` ir tikai
  tavs dators, un, lai citi tiktu klāt, jādara vēl kaut kas.
