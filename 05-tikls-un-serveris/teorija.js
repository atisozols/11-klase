// ============================================================
// 05. BLOKS — TĪKLS, SERVERIS, DROŠĪBA, MAŠĪNMĀCĪŠANĀS
// ============================================================
// Šis ir pirmais bloks, kur rakstām JavaScript, nevis Python.
// Python paliek algoritmiem, datu apstrādei un eksāmenam.
// JavaScript ir valoda, kas darbojas pārlūkā — un ar Node arī serverī.
//
// Uzstādīšana:
//   npm init -y
//   npm install express knex sqlite3
//
// Palaišana:
//   node serveris.js
//
// Komentārs  // ?  nozīmē: vispirms uzmini, kas notiks, tikai tad palaid.
// ============================================================


// ============================================================
// 1. KLIENTS UN SERVERIS                               [11-063]
// ============================================================
// Kas notiek, ievadot adresi pārlūkā:
//
//   1. pārlūks jautā DNS serverim: kāda IP adrese ir skola.lv?
//   2. DNS atbild: 89.111.22.33
//   3. pārlūks sūta HTTP pieprasījumu uz šo adresi
//   4. serveris atbild ar HTML, CSS, JavaScript un attēliem
//   5. pārlūks to visu attēlo
//
// KLIENTS  — tas, kurš prasa (pārlūks, mobilā lietotne, mūsu fetch)
// SERVERIS — tas, kurš atbild
//
// Viens un tas pats dators var būt abi. Kad palaid serveri savā datorā
// un atver localhost, tu esi gan klients, gan serveris.


// ============================================================
// 2. HTTP                                              [11-064]
// ============================================================
// HTTP ir saruna. Pieprasījumā ir metode, adrese un dažreiz dati.
//
//   GET  /skoleni        atdod man skolēnus
//   POST /pulcini        te ir jauns pulciņš, saglabā to
//
// Atbildē ir statusa kods un dati.
//
//   200  viss kārtībā
//   201  izveidots (pēc POST)
//   301  pārcelts uz citu adresi
//   400  slikts pieprasījums — vaina klientā
//   401  nav autorizēts
//   404  nav atrasts
//   500  servera kļūda — vaina serverī
//
// Kodu pirmais cipars pasaka galveno:
//   2xx  izdevās      4xx  vaina prasītājā      5xx  vaina atbildētājā
//
// Visu to var redzēt pārlūka DevTools cilnē Network.


// ============================================================
// 3. PIRMAIS SERVERIS                                   [11-065]
// ============================================================
// const express = require("express");
// const app = express();
//
// app.get("/", (req, res) => {
//     res.send("Sveika, pasaule");
//     });
//
// app.listen(3000, () => {
//     console.log("Serveris strādā: http://localhost:3000");
// });
//
// Palaiž ar:  node serveris.js
// Aptur ar:   Ctrl+C
//
// Serveris "karājas" ar nolūku — tas gaida pieprasījumus. Tas nav
// iekāries; tas dara savu darbu.
//
// Ja rādās "port already in use", iepriekšējais serveris vēl strādā.


// ============================================================
// 4. MARŠRUTI UN JSON                                   [11-066]
// ============================================================
// Maršruts ar parametru — daļa adreses ir mainīga:
//
// app.get("/sveiciens/:vards", (req, res) => {
//     res.send("Sveika, " + req.params.vards);
// });
//
// Vaicājuma parametri nāk aiz jautājumzīmes:
//   /skoleni?klase=11.a
//
// app.get("/skoleni", (req, res) => {
//     const klase = req.query.klase;      // "11.a" vai undefined
//     res.json(skoleni);
// });
//
// res.json() nosūta datus JSON formātā — tieši to, ko 03. blokā
// saņēmām no svešām API. Tagad mēs esam tie, kas atbild.
//
// Statusa kodu norāda pirms atbildes:
//
// app.get("/skoleni/:id", (req, res) => {
//     const skolens = atrast(req.params.id);
//     if (!skolens) {
//         return res.status(404).json({ kluda: "Skolens nav atrasts" });
//     }
//     res.json(skolens);
// });
//
// Uzmanību: req.params vērtības vienmēr ir TEKSTS, arī id.   // ?


// ============================================================
// 5. KLIENTS: fetch UN DOM                              [11-067]
// ============================================================
// Šis kods darbojas PĀRLŪKĀ, nevis serverī.
//
// async function ieladetSkolenus() {
//     const atbilde = await fetch("/skoleni");
//     const skoleni = await atbilde.json();
//
//     const saraksts = document.querySelector("#saraksts");
//     saraksts.innerHTML = "";
//
//     for (const skolens of skoleni) {
//         const rinda = document.createElement("li");
//         rinda.textContent = skolens.vards + " " + skolens.uzvards;
//         saraksts.appendChild(rinda);
//     }
// }
//
// ieladetSkolenus();
//
// await nozīmē "pagaidi, kamēr atbilde atnāk". Tīkls ir lēns —
// tāpēc dati parādās ar nelielu aizkavi, un tāpēc kods ir async.
//
// HTML pusē vajag tikai vietu, kur likt datus:
//   <ul id="saraksts"></ul>
//   <script src="klients.js"></script>


// ============================================================
// 6. DATUBĀZE SERVERĪ                                   [11-068]
// ============================================================
// Knex ir bibliotēka, kas raksta SQL mūsu vietā. SQL joprojām
// jāprot — bez tā nav saprotams, ko Knex dara.
//
// const knex = require("knex")({
//     client: "sqlite3",
//     connection: { filename: "./skola.db" },
//     useNullAsDefault: true,
// });
//
// Vienkāršs vaicājums:
//   knex("skoleni").select("vards", "uzvards")
//   -->  SELECT vards, uzvards FROM skoleni
//
// Ar nosacījumu:
//   knex("skoleni").where("klase_id", 3)
//   -->  SELECT * FROM skoleni WHERE klase_id = 3
//
// Ar savienojumu:
//   knex("skoleni")
//       .join("klases", "skoleni.klase_id", "klases.id")
//       .select("skoleni.vards", "klases.nosaukums")
//
// Maršrutā tas izskatās šādi:
//
// app.get("/skoleni", async (req, res) => {
//     const skoleni = await knex("skoleni").select("*");
//     res.json(skoleni);
// });
//
// Grupēšana ir tā pati, kas 02. blokā:
//
// app.get("/klases", async (req, res) => {
//     const rindas = await knex("klases")
//         .leftJoin("skoleni", "klases.id", "skoleni.klase_id")
//         .select("klases.nosaukums")
//         .count("skoleni.id as skaits")
//         .groupBy("klases.id");
//     res.json(rindas);
// });


// ============================================================
// 7. POST UN FORMAS                                     [11-070]
// ============================================================
// Lai serveris saprastu JSON pieprasījumā, tas jāpasaka:
//
//   app.use(express.json());
//
// Serverī:
//
// app.post("/pulcini", async (req, res) => {
//     const { nosaukums, vietu_skaits } = req.body;
//
//     if (!nosaukums || nosaukums.trim() === "") {
//         return res.status(400).json({ kluda: "Nosaukums ir obligats" });
//     }
//     if (vietu_skaits <= 0) {
//         return res.status(400).json({ kluda: "Vietu skaitam jabut pozitivam" });
//     }
//
//     const [id] = await knex("pulcini").insert({ nosaukums, vietu_skaits });
//     res.status(201).json({ id });
// });
//
// Klientā:
//
// await fetch("/pulcini", {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ nosaukums: "Šahs", vietu_skaits: 16 }),
// });
//
// SVARĪGI: serverim VIENMĒR jāpārbauda dati, arī ja forma tos jau
// pārbaudīja. Formu var apiet — pieprasījumu var nosūtīt bez tās.


// ============================================================
// 8. KĻŪDU APSTRĀDE SERVERĪ                             [11-071]
// ============================================================
// app.get("/skoleni/:id", async (req, res) => {
//     try {
//         const skolens = await knex("skoleni").where("id", req.params.id).first();
//         if (!skolens) {
//             return res.status(404).json({ kluda: "Skolens nav atrasts" });
//         }
//         res.json(skolens);
//     } catch (kluda) {
//         console.error(kluda);                    // detaļas serverī
//         res.status(500).json({ kluda: "Servera kluda" });   // vispārīgi lietotājam
//     }
// });
//
// Kāda atšķirība:
//   400  klients atsūtīja muļķības
//   404  klients prasīja kaut ko, kā nav
//   500  serverim pašam kaut kas salūza
//
// Kļūdas paziņojumā lietotājam NEDRĪKST būt SQL vaicājums, faila ceļš
// vai datubāzes struktūra. Tā ir informācija uzbrucējam.


// ============================================================
// 9. LOKĀLAIS TĪKLS                                     [11-072]
// ============================================================
// localhost jeb 127.0.0.1 ir TIKAI tavs dators. Neviens cits tur
// netiek, arī tas, kas sēž blakus.
//
// Lokālā IP adrese (parasti 192.168.x.x) ir tava datora adrese
// vietējā tīklā. To var noskaidrot:
//   macOS / Linux:  ifconfig  vai  ip addr
//   Windows:        ipconfig
//
// Ja serveris klausās uz visām adresēm, klasesbiedrs var atvērt
// http://192.168.1.42:3000
//
// Publiskā IP adrese ir tā, ko internetā redz pārējā pasaule. Visai
// mājai vai skolai tā parasti ir viena — maršrutētājs sadala.
//
// Lai no interneta piekļūtu serverim mājās, maršrutētājā jākonfigurē
// portu pāradresācija. Tas ir arī drošības risks: atvērts ports nozīmē,
// ka tavu serveri var atrast un pārbaudīt jebkurš.


// ============================================================
// 10. DROŠĪBA                                           [11-073]
// ============================================================
// HTTP dati ceļo atklātā tekstā. Ikviens, kas ir pa vidu (piemēram,
// atvērtā Wi-Fi tīklā), tos var izlasīt. HTTPS tos šifrē.
//
// PAROLES NEKAD NEGLABĀ ATKLĀTĀ TEKSTĀ. Ja datubāze noplūst — un tas
// notiek — visas paroles ir zināmas.
//
// Jaucējfunkcija (hash) pārvērš tekstu skaitļu virknē tā, ka:
//   - vienam tekstam vienmēr ir viena un tā pati jaucējvērtība;
//   - no jaucējvērtības tekstu atgūt nevar;
//   - viena burta maiņa maina visu vērtību.
//
// const crypto = require("crypto");
//
// function jauceja(teksts) {
//     return crypto.createHash("sha256").update(teksts).digest("hex");
// }
//
// console.log(jauceja("parole123"));
// console.log(jauceja("parole124"));      // ?  cik līdzīgas būs vērtības?
//
// Pārbaude notiek, salīdzinot jaucējvērtības, nevis paroles:
//
// if (jauceja(ievaditaParole) === lietotajs.paroles_jauceja) { ... }
//
// Īstā sistēmā lieto bcrypt un "sāli" (salt) — nejaušu papildinājumu,
// kas neļauj uzbrucējam izmantot gatavas jaucējvērtību tabulas.
