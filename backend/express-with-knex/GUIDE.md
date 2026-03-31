# Praktiskais ceļvedis: Knex + Express + PostgreSQL

## 1) Datubāzes struktūra

Mēs strādāsim ar **skolas bibliotēkas** sistēmu. Tajā ir 4 tabulas:

### `authors` – grāmatu autori

| Kolonna | Tips   | Piezīmes             |
| ------- | ------ | -------------------- |
| id      | serial | primārā atslēga (PK) |
| name    | text   | NOT NULL             |
| country | text   |                      |

### `books` – grāmatas

| Kolonna        | Tips    | Piezīmes                        |
| -------------- | ------- | ------------------------------- |
| id             | serial  | PK                              |
| title          | text    | NOT NULL                        |
| author_id      | integer | ārējā atslēga (FK) → authors.id |
| published_year | integer |                                 |

### `students` – skolēni

| Kolonna | Tips    | Piezīmes         |
| ------- | ------- | ---------------- |
| id      | serial  | PK               |
| name    | text    | NOT NULL         |
| email   | text    | UNIQUE, NOT NULL |
| grade   | integer |                  |

### `borrowings` – grāmatu izsniegšana

| Kolonna     | Tips      | Piezīmes                    |
| ----------- | --------- | --------------------------- |
| id          | serial    | PK                          |
| student_id  | integer   | FK → students.id            |
| book_id     | integer   | FK → books.id               |
| borrowed_at | timestamp | DEFAULT now()               |
| returned_at | timestamp | NULL (ja vēl nav atgriezta) |

### Tabulu attiecības

- Viens autors → daudzas grāmatas (**1:N**)
- Viens skolēns var aizņemties daudzas grāmatas, viena grāmata var tikt aizņemta daudziem skolēniem → **N:N** caur `borrowings`

---

## 2) Izveido datubāzi un tabulas PostgreSQL

Izveido jaunu datubāzi:

```sql
CREATE DATABASE school_library;
```

Pieslēdzies tai:

```sql
\c school_library
```

Izveido tabulas:

```sql
CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  country TEXT
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  author_id INTEGER REFERENCES authors(id),
  published_year INTEGER
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  grade INTEGER
);

CREATE TABLE borrowings (
  id SERIAL PRIMARY KEY,
  student_id INTEGER REFERENCES students(id),
  book_id INTEGER REFERENCES books(id),
  borrowed_at TIMESTAMP DEFAULT now(),
  returned_at TIMESTAMP
);
```

---

## 3) Pievieno testa datus

```sql
INSERT INTO authors (name, country) VALUES
  ('Rainis', 'Latvija'),
  ('Aspazija', 'Latvija'),
  ('Rudolfs Blaumanis', 'Latvija'),
  ('Vilis Lacis', 'Latvija');

INSERT INTO books (title, author_id, published_year) VALUES
  ('Uguns un nakts', 1, 1905),
  ('Zelta zirgs', 1, 1909),
  ('Aspazijas dzejoļi', 2, 1894),
  ('Naves ena', 3, 1899),
  ('Zvejnieka dels', 4, 1933),
  ('Pazudusais dels', 3, 1893);

INSERT INTO students (name, email, grade) VALUES
  ('Anna Berzina', 'anna@skola.lv', 11),
  ('Karlis Ozols', 'karlis@skola.lv', 11),
  ('Elina Kalnina', 'elina@skola.lv', 10),
  ('Martins Liepa', 'martins@skola.lv', 12);

INSERT INTO borrowings (student_id, book_id, borrowed_at, returned_at) VALUES
  (1, 1, '2025-09-01', '2025-09-15'),
  (1, 4, '2025-10-01', NULL),
  (2, 2, '2025-10-05', NULL),
  (3, 5, '2025-09-20', '2025-10-01'),
  (4, 3, '2025-11-01', NULL);
```

Pārbaudi, vai dati ir ievietoti:

```sql
SELECT * FROM authors;
SELECT * FROM books;
SELECT * FROM students;
SELECT * FROM borrowings;
```

---

## 4) Instalē `knex` un `pg`

Atver termināli **savā projekta mapē** (`express-with-knex`) un izpildi:

```bash
npm i
```

un tad

```bash
npm install knex pg
```

Pēc instalācijas tavā `package.json` failā `dependencies` sadaļā parādīsies `knex` un `pg`.

---

## 5) Izveido Knex konfigurācijas failu

Projekta mapē izveido jaunu failu `knexfile.js`:

```js
module.exports = {
  client: "pg",
  connection: {
    host: "localhost",
    port: 5432,
    user: "postgres",
    password: "admin", // <-- nomainī uz savu PostgreSQL paroli
    database: "school_library",
  },
};
```

> **Svarīgi:** nomainī `password` uz to paroli, kuru tu lieto, lai pieslēgtos PostgreSQL.

---

## 6) Izveido Knex instanci

Izveido jaunu failu `db.js` – šis būs vienīgais fails, kas izveido savienojumu ar datubāzi:

```js
const knexLib = require("knex");
const knexConfig = require("./knexfile.js");

const knex = knexLib(knexConfig);

module.exports = knex;
```

Ko šis fails dara:

1. Ielādē `knex` bibliotēku ar `require`.
2. Ielādē mūsu konfigurāciju no `knexfile.js`.
3. Izveido **vienu** Knex instanci (savienojumu ar DB).
4. Eksportē to ar `module.exports`, lai citi faili var ielādēt un lietot.

---

## 7) Lieto Knex savā Express serverī

Tagad atver `index.js` un pievieno pirmo Knex vaicājumu – vienkāršu `SELECT` no `authors` tabulas.

Nomainī savu `index.js` saturu uz:

```js
const express = require("express");
const knex = require("./db.js");

const app = express();
const PORT = 5000;

app.use(express.json());

app.get("/", (req, res) => {
  res.json({ message: "ok" });
});

app.get("/authors", async (req, res) => {
  try {
    const authors = await knex("authors").select("*");
    res.json(authors);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt autorus" });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

### Kas te notiek?

1. Ielādējam `knex` no `db.js` ar `require` (mūsu DB savienojums).
2. Izveidojam jaunu `GET /authors` maršrutu.
3. Tajā izsaucam `knex('authors').select('*')` – tas ir tas pats, kas SQL:
   ```sql
   SELECT * FROM authors;
   ```
4. `await` – gaidām, līdz datubāze atgriež rezultātu.
5. Rezultāts ir **JavaScript masīvs ar objektiem** – katrs objekts ir viena rinda no tabulas.
6. Nosūtām to klientam kā JSON.
7. Ja kaut kas noiet greizi, noķeram kļūdu ar `catch` un atgriežam 500 kļūdu.

---

## 8) Testē

Palaiž serveri:

```bash
npm run dev
```

Atver pārlūku vai izmanto termināli:

```bash
curl http://localhost:5000/authors
```

Tev vajadzētu saņemt atpakaļ kaut ko līdzīgu:

```json
[
  { "id": 1, "name": "Rainis", "country": "Latvija" },
  { "id": 2, "name": "Aspazija", "country": "Latvija" },
  { "id": 3, "name": "Rūdolfs Blaumanis", "country": "Latvija" },
  { "id": 4, "name": "Vilis Lācis", "country": "Latvija" }
]
```

Ja redzi šo – **tavs Express serveris tagad lasa datus no PostgreSQL caur Knex!**

---

## 9) Ko tieši Knex izdarīja?

Kad tu uzrakstīji:

```js
const authors = await knex("authors").select("*");
```

Knex:

1. Paņēma tabulas nosaukumu `'authors'` un metodi `.select('*')`.
2. Uzģenerēja SQL vaicājumu: `SELECT * FROM "authors"`.
3. Nosūtīja to caur `pg` draiveri uz PostgreSQL.
4. Saņēma atpakaļ rindas no DB.
5. Pārvērta tās JavaScript masīvā ar objektiem.
6. Atgrieza tev šo masīvu.

Tu nerakstīji nevienu SQL rindiņu pats – Knex to izdarīja tavā vietā.

---

## 10) Kopsavilkums – failu struktūra

Pēc šī soļa tavā projektā ir šādi faili:

```
express-with-knex/
├── index.js        ← Express serveris ar maršrutiem
├── db.js           ← Knex instance (DB savienojums)
├── knexfile.js     ← Knex konfigurācija (DB pieslēguma dati)
├── package.json
└── node_modules/
```

### Kas ir kas:

- **`knexfile.js`** – "kur ir mana datubāze un kā tai pieslēgties"
- **`db.js`** – "izveido savienojumu un eksportē to"
- **`index.js`** – "Express serveris, kas lieto DB savienojumu, lai apstrādātu pieprasījumus"

---

## 11) Migrations un seeds - migrācijas un datu ielāde

Līdz šim mēs tabulas un testa datus veidojām **manuāli ar SQL** (`CREATE TABLE`, `INSERT INTO`).

Tas ir labs sākums, lai saprastu datubāzi. Taču reālos projektos ļoti bieži izmanto:

- **migrations** – failus, kas apraksta datubāzes struktūru
- **seeds** – failus, kas ieliek sākuma vai testa datus

Kāpēc tas ir ērti:

1. Visa datubāzes struktūra glabājas projekta failos.
2. Cits cilvēks komandā var palaist tās pašas komandas un iegūt to pašu rezultātu.
3. Izmaiņas var atcelt ar `rollback`.
4. Testa datus var atjaunot ar vienu komandu.

> **Svarīgi:** migrations un seeds parasti ir **alternatīva** 2. un 3. solim, nevis papildinājums tiem.
>
> Ja tu jau izveidoji tabulas ar `CREATE TABLE`, tad `migrate:latest` mēģinās tās izveidot vēlreiz un radīs kļūdu. Šai daļai izmanto:
>
> - vai nu **jaunu tukšu datubāzi**
> - vai arī izdzēs esošās tabulas un sāc no jauna

---

## 12) Papildini `knexfile.js`, lai Knex zina par `migrations` un `seeds`

Knex pēc noklusējuma pats meklē mapes `migrations/` un `seeds/`, bet mācību nolūkos ir labi tās norādīt skaidri.

`knexfile.js` var izskatīties šādi:

```js
module.exports = {
  client: "pg",
  connection: {
    host: "localhost",
    port: 5432,
    user: "postgres",
    password: "admin", // <-- nomaini uz savu PostgreSQL paroli
    database: "school_library",
  },
  migrations: {
    directory: "./migrations",
  },
  seeds: {
    directory: "./seeds",
  },
};
```

Tagad Knex zinās:

- kur glabāt tabulu struktūras failus
- kur glabāt sākuma datu failus

---

## 13) Izveido pirmo migration failu

Terminālī projekta mapē izpildi:

```bash
npx knex migrate:make create_library_tables
```

Knex izveidos failu mapē `migrations/` ar nosaukumu apmēram šādā stilā:

```text
migrations/20260331120000_create_library_tables.js
```

Atver šo failu un ieliec šādu saturu:

```js
exports.up = async function (knex) {
  await knex.schema.createTable("authors", (table) => {
    table.increments("id").primary();
    table.text("name").notNullable();
    table.text("country");
  });

  await knex.schema.createTable("books", (table) => {
    table.increments("id").primary();
    table.text("title").notNullable();
    table.integer("author_id").references("id").inTable("authors");
    table.integer("published_year");
  });

  await knex.schema.createTable("students", (table) => {
    table.increments("id").primary();
    table.text("name").notNullable();
    table.text("email").notNullable().unique();
    table.integer("grade");
  });

  await knex.schema.createTable("borrowings", (table) => {
    table.increments("id").primary();
    table.integer("student_id").references("id").inTable("students");
    table.integer("book_id").references("id").inTable("books");
    table.timestamp("borrowed_at").defaultTo(knex.fn.now());
    table.timestamp("returned_at").nullable();
  });
};

exports.down = async function (knex) {
  await knex.schema.dropTableIfExists("borrowings");
  await knex.schema.dropTableIfExists("students");
  await knex.schema.dropTableIfExists("books");
  await knex.schema.dropTableIfExists("authors");
};
```

### Ko nozīmē `up` un `down`?

- **`exports.up`** – ko darīt, kad migration tiek palaists uz priekšu
- **`exports.down`** – ko darīt, kad gribam šīs izmaiņas atcelt

Tātad:

- `up` sadaļā mēs **izveidojam tabulas**
- `down` sadaļā mēs **tās dzēšam apgrieztā secībā**

> `borrowings` jādzēš vispirms, jo tā izmanto ārējās atslēgas uz `students` un `books`.

---

## 14) Palaiž migrations

Kad migration fails ir gatavs, izpildi:

```bash
npx knex migrate:latest
```

Kas notiks:

1. Knex izveidos tabulas pēc `exports.up`.
2. Datubāzē automātiski parādīsies arī palīgtabulas:
   - `knex_migrations`
   - `knex_migrations_lock`
3. Knex atzīmēs, ka šī migration jau ir izpildīta.

Ja gribi atcelt pēdējo migration:

```bash
npx knex migrate:rollback
```

Ja pēc tam gribi to palaist vēlreiz:

```bash
npx knex migrate:latest
```

Tā ir liela migrations priekšrocība: tu vari ne tikai izveidot struktūru, bet arī droši pārbaudīt izmaiņas un vajadzības gadījumā tās atcelt.

---

## 15) Izveido otru migration, kas maina jau esošu tabulu

Līdz šim mēs izmantojām migration, lai **izveidotu tabulas no nulles**.

Taču reālos projektos migrations ļoti bieži izmanto arī tam, lai **mainītu jau esošu datubāzes struktūru**. Piemēram:

- pievienot jaunu kolonnu
- izdzēst vecu kolonnu
- pievienot `UNIQUE`
- nomainīt datu tipu

Pieņemsim, ka vēlāk mēs izdomājam glabāt arī skolēna telefona numuru.

Terminālī izpildi:

```bash
npx knex migrate:make add_phone_to_students
```

Knex izveidos vēl vienu failu mapē `migrations/`, piemēram:

```text
migrations/20260331121000_add_phone_to_students.js
```

Atver šo failu un ieliec šādu saturu:

```js
exports.up = async function (knex) {
  await knex.schema.alterTable("students", (table) => {
    table.text("phone");
  });
};

exports.down = async function (knex) {
  await knex.schema.alterTable("students", (table) => {
    table.dropColumn("phone");
  });
};
```

### Kāpēc šeit ir `alterTable(...)`, nevis `createTable(...)`?

- **`createTable(...)`** lieto tad, kad tabula vēl neeksistē.
- **`alterTable(...)`** lieto tad, kad tabula jau eksistē un tu gribi to izmainīt.

Šajā piemērā:

- pirmais migration fails izveido `students` tabulu
- otrais migration fails tai pievieno jaunu kolonnu `phone`

Kolonna `phone` ir **neobligāta**, jo mēs nelietojam `.notNullable()`.

Tas ir ērti mācību piemēram, jo:

1. nav jāmaina esošie seed dati
2. nav jāievada telefona numurs katram skolēnam
3. var skaidri redzēt, kā migrations palīdz attīstīt shēmu pa soļiem

Kad fails ir gatavs, palaid vēlreiz:

```bash
npx knex migrate:latest
```

Šoreiz Knex:

1. nepalaidīs pirmo migration vēlreiz
2. atradīs tikai jauno, vēl neizpildīto migration failu
3. pievienos `phone` kolonnu tabulai `students`

Tieši tā migrations strādā reālos projektos:

- sākumā viens fails izveido sākotnējo struktūru
- vēlāk citi faili pakāpeniski maina esošo struktūru
- `migrate:latest` izpilda tikai to, kas vēl nav izpildīts

Ja gribi šo izmaiņu atcelt, vari lietot:

```bash
npx knex migrate:rollback
```

Tad tiks atcelts **pēdējais** migration, tas ir, `phone` kolonna tiks noņemta.

---

## 16) Izveido seed failu testa datiem

Tagad izveidosim failu, kas ieliek datubāzē mūsu bibliotēkas sākuma datus.

Terminālī izpildi:

```bash
npx knex seed:make library_data
```

Tas izveidos failu mapē `seeds/`, piemēram:

```text
seeds/library_data.js
```

Atver šo failu un ieliec šādu saturu:

```js
exports.seed = async function (knex) {
  await knex.raw(
    "TRUNCATE TABLE borrowings, books, students, authors RESTART IDENTITY CASCADE",
  );

  await knex("authors").insert([
    { name: "Rainis", country: "Latvija" },
    { name: "Aspazija", country: "Latvija" },
    { name: "Rudolfs Blaumanis", country: "Latvija" },
    { name: "Vilis Lacis", country: "Latvija" },
  ]);

  await knex("books").insert([
    { title: "Uguns un nakts", author_id: 1, published_year: 1905 },
    { title: "Zelta zirgs", author_id: 1, published_year: 1909 },
    { title: "Aspazijas dzejoli", author_id: 2, published_year: 1894 },
    { title: "Naves ena", author_id: 3, published_year: 1899 },
    { title: "Zvejnieka dels", author_id: 4, published_year: 1933 },
    { title: "Pazudusais dels", author_id: 3, published_year: 1893 },
  ]);

  await knex("students").insert([
    { name: "Anna Berzina", email: "anna@skola.lv", grade: 11 },
    { name: "Karlis Ozols", email: "karlis@skola.lv", grade: 11 },
    { name: "Elina Kalnina", email: "elina@skola.lv", grade: 10 },
    { name: "Martins Liepa", email: "martins@skola.lv", grade: 12 },
  ]);

  await knex("borrowings").insert([
    {
      student_id: 1,
      book_id: 1,
      borrowed_at: "2025-09-01",
      returned_at: "2025-09-15",
    },
    { student_id: 1, book_id: 4, borrowed_at: "2025-10-01", returned_at: null },
    { student_id: 2, book_id: 2, borrowed_at: "2025-10-05", returned_at: null },
    {
      student_id: 3,
      book_id: 5,
      borrowed_at: "2025-09-20",
      returned_at: "2025-10-01",
    },
    { student_id: 4, book_id: 3, borrowed_at: "2025-11-01", returned_at: null },
  ]);
};
```

### Kāpēc te ir `TRUNCATE ... RESTART IDENTITY CASCADE`?

Šī rinda:

1. iztīra visas četras tabulas
2. atiestata `id` skaitītājus atpakaļ uz 1
3. ļauj seed failu palaist atkārtoti bez konflikta ar vecajiem datiem

Tas ir īpaši noderīgi mācību projektā, kur mēs gribam vienmēr atgriezties pie viena un tā paša sākuma stāvokļa.

---

## 17) Palaiž seeds

Kad tabulas jau ir izveidotas ar migration, ieliec datus ar komandu:

```bash
npx knex seed:run
```

Pēc tam vari pārbaudīt rezultātu:

```bash
curl http://localhost:5000/authors
```

vai arī PostgreSQL konsolē:

```sql
SELECT * FROM authors;
SELECT * FROM books;
SELECT * FROM students;
SELECT * FROM borrowings;
```

Ja gribi pilnu darba plūsmu no tukšas datubāzes līdz gataviem testa datiem, tad bieži pietiek ar šīm divām komandām:

```bash
npx knex migrate:latest
npx knex seed:run
```

---

## 18) Kopsavilkums: kad lietot ko?

- Ja tu mācies SQL pamatus, ir labi sākumā rakstīt `CREATE TABLE` un `INSERT INTO` ar roku.
- Ja tu būvē īstu projektu ar Node.js un Knex, ērtāk ir lietot **migrations** un **seeds**.
- **Migrations** atbild par tabulu struktūru un tās izmaiņām laika gaitā.
- **Seeds** atbild par sākuma vai testa datiem.
- Ar migrations tu vari ne tikai izveidot tabulas, bet arī vēlāk pievienot jaunas kolonnas vai citādi mainīt esošās tabulas.

Pēc migrations un seeds pievienošanas projekta struktūra var izskatīties šādi:

```text
express-with-knex/
├── index.js
├── db.js
├── knexfile.js
├── migrations/
│   ├── 20260331120000_create_library_tables.js
│   └── 20260331121000_add_phone_to_students.js
├── seeds/
│   └── library_data.js
├── package.json
└── node_modules/
```

Ja tu šo daļu saproti, tad nākamais solis jau ir ļoti praktisks: veidot jaunus API maršrutus (`GET`, `POST`, `PUT`, `DELETE`) un ar Knex palīdzību lasīt un mainīt datus datubāzē.
