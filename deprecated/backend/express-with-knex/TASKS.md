# Uzdevumi: 5 vienkārši Knex lietošanas piemēri (ar esošo DB struktūru)

Šie uzdevumi ir balstīti uz datubāzi **`school_library`** ar tabulām:

- `authors` (id, name, country)
- `books` (id, title, author_id, published_year)
- `students` (id, name, email, grade)
- `borrowings` (id, student_id, book_id, borrowed_at, returned_at)

Ideja: katram uzdevumam pievieno jaunu maršrutu savā `index.js` un uzraksti Knex vaicājumu.

---

## 1) Filtrēšana + kārtošana + limit

Izveido maršrutu, kas atgriež grāmatas, kas publicētas **no norādītā gada**, sakārtotas pēc publicēšanas gada dilstoši.

### Maršruts

`GET /books?fromYear=1900&limit=10`

### Ko vajag izdarīt

- Izlasi `fromYear` un `limit` no `req.query`.
- Ja `fromYear` nav norādīts, pieņem `0`.
- Ja `limit` nav norādīts, pieņem `20`.

### Knex piemērs

```js
app.get("/books", async (req, res) => {
  try {
    const fromYear = Number(req.query.fromYear ?? 0);
    const limit = Number(req.query.limit ?? 20);

    const books = await knex("books")
      .select("id", "title", "author_id", "published_year")
      .where("published_year", ">=", fromYear)
      .orderBy("published_year", "desc")
      .limit(limit);

    res.json(books);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt grāmatas" });
  }
});
```

### SQL analogs

```sql
SELECT id, title, author_id, published_year
FROM books
WHERE published_year >= 1900
ORDER BY published_year DESC
LIMIT 10;
```

---

## 2) JOIN: grāmatas kopā ar autora vārdu

Izveido maršrutu, kas atgriež grāmatas ar autora vārdu (`author_name`).

### Maršruts

`GET /books-with-authors`

### Knex piemērs

```js
app.get("/books-with-authors", async (req, res) => {
  try {
    const rows = await knex("books")
      .join("authors", "books.author_id", "authors.id")
      .select(
        "books.id",
        "books.title",
        "books.published_year",
        "authors.name as author_name",
      )
      .orderBy("books.title", "asc");

    res.json(rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt grāmatas ar autoriem" });
  }
});
```

### SQL analogs

```sql
SELECT
  books.id,
  books.title,
  books.published_year,
  authors.name AS author_name
FROM books
JOIN authors ON books.author_id = authors.id
ORDER BY books.title ASC;
```

---

## 3) INSERT: pievieno jaunu skolēnu

Izveido maršrutu, kas pievieno jaunu skolēnu tabulā `students`.

### Maršruts

`POST /students`

### Body piemērs

```json
{
  "name": "Ieva Liepa",
  "email": "ieva@skola.lv",
  "grade": 11
}
```

### Ko vajag izdarīt

- Pārbaudi, ka `name` un `email` ir ievadīti.
- Ievieto ierakstu DB.
- Atgriez izveidoto skolēnu.

### Knex piemērs

```js
app.post("/students", async (req, res) => {
  try {
    const { name, email, grade } = req.body;

    if (!name || !email) {
      return res.status(400).json({ error: "name un email ir obligāti" });
    }

    const [created] = await knex("students")
      .insert({ name, email, grade })
      .returning(["id", "name", "email", "grade"]);

    res.status(201).json(created);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās izveidot skolēnu" });
  }
});
```

### SQL analogs

```sql
INSERT INTO students (name, email, grade)
VALUES ('Ieva Liepa', 'ieva@skola.lv', 11)
RETURNING id, name, email, grade;
```

---

## 4) UPDATE: atzīmē izsniegšanu kā atgrieztu

Izveido maršrutu, kas `borrowings` ierakstam uzliek `returned_at = now()`.

### Maršruts

`PATCH /borrowings/:id/return`

### Ko vajag izdarīt

- Paņem `id` no `req.params`.
- Atjaunini `returned_at` tikai tam ierakstam.
- Atgriez atjaunināto ierakstu.

### Knex piemērs

```js
app.patch("/borrowings/:id/return", async (req, res) => {
  try {
    const id = Number(req.params.id);

    const [updated] = await knex("borrowings")
      .where({ id })
      .update({ returned_at: knex.fn.now() })
      .returning(["id", "student_id", "book_id", "borrowed_at", "returned_at"]);

    if (!updated) {
      return res.status(404).json({ error: "Borrowing nav atrasts" });
    }

    res.json(updated);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās atjaunināt borrowing" });
  }
});
```

### SQL analogs

```sql
UPDATE borrowings
SET returned_at = now()
WHERE id = 123
RETURNING id, student_id, book_id, borrowed_at, returned_at;
```

---

## 5) Grupēšana (GROUP BY): cik aktīvi aizņēmumi katram skolēnam

Izveido maršrutu, kas parāda skolēnus un to, cik **neatgrieztas** grāmatas katram šobrīd ir (`returned_at IS NULL`).

### Maršruts

`GET /students/active-borrowings`

### Knex piemērs

```js
app.get("/students/active-borrowings", async (req, res) => {
  try {
    const rows = await knex("students")
      .leftJoin("borrowings", function () {
        this.on("students.id", "=", "borrowings.student_id").andOnNull(
          "borrowings.returned_at",
        );
      })
      .groupBy("students.id")
      .select(
        "students.id",
        "students.name",
        "students.email",
        "students.grade",
      )
      .count("borrowings.id as active_borrowings")
      .orderBy("active_borrowings", "desc");

    res.json(rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt statistiku" });
  }
});
```

### SQL analogs

```sql
SELECT
  students.id,
  students.name,
  students.email,
  students.grade,
  COUNT(borrowings.id) AS active_borrowings
FROM students
LEFT JOIN borrowings
  ON students.id = borrowings.student_id
 AND borrowings.returned_at IS NULL
GROUP BY students.id
ORDER BY active_borrowings DESC;
```

---

## Testēšana (ieteikums)

Kad esi pievienojis maršrutus, palaid serveri:

```bash
npm run dev
```

Piemēri ar `curl`:

```bash
curl "http://localhost:5001/books?fromYear=1890&limit=5"
curl "http://localhost:5001/books-with-authors"
curl -X POST "http://localhost:5001/students" -H "Content-Type: application/json" -d '{"name":"Ieva Liepa","email":"ieva@skola.lv","grade":11}'
curl -X PATCH "http://localhost:5001/borrowings/2/return"
curl "http://localhost:5001/students/active-borrowings"
```
