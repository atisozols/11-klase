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
  ('Rūdolfs Blaumanis', 'Latvija'),
  ('Vilis Lācis', 'Latvija');

INSERT INTO books (title, author_id, published_year) VALUES
  ('Uguns un nakts', 1, 1905),
  ('Zelta zirgs', 1, 1909),
  ('Aspazijas dzejoļi', 2, 1894),
  ('Nāves ēnā', 3, 1899),
  ('Zvejnieka dēls', 4, 1933),
  ('Pazudušais dēls', 3, 1893);

INSERT INTO students (name, email, grade) VALUES
  ('Anna Bērziņa', 'anna@skola.lv', 11),
  ('Kārlis Ozols', 'karlis@skola.lv', 11),
  ('Elīna Kalniņa', 'elina@skola.lv', 10),
  ('Mārtiņš Liepa', 'martins@skola.lv', 12);

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
