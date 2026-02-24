const express = require("express");
const knex = require("./db.js");

const app = express();
const PORT = 5001;

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

app.get("/books", async (req, res) => {
  try {
    const books = await knex("books").select("*");
    res.json(books);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt grāmatas" });
  }
});

app.get("/students", async (req, res) => {
  try {
    const students = await knex("students").select("name", "email");
    res.json(students);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt skolēnus" });
  }
});

app.get("/students/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const student = await knex("students")
      .select("name", "email")
      .where({ id: id })
      .first();

    if (!student) {
      return res.status(404).json({ error: "Skolēns nav atrasts" });
    }

    res.json(student);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt skolēnu" });
  }
});

app.get("/borrowings/:studentId", async (req, res) => {
  try {
    const studentId = req.params.studentId;

    const studentBorrowings = await knex("borrowings")
      .select("books.title", "authors.name as author")
      .innerJoin("books", "borrowings.book_id", "books.id")
      .innerJoin("authors", "books.author_id", "authors.id")
      .where("borrowings.student_id", studentId);

    res.json(studentBorrowings);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt izsniegtās grāmatas" });
  }
});

app.get("/borrowings/:studentId/active", async (req, res) => {
  try {
    const studentId = req.params.studentId;

    const activeBorrowings = await knex("borrowings")
      .select(
        "books.title",
        "authors.name as author",
        "borrowings.borrowed_date",
      )
      .innerJoin("books", "borrowings.book_id", "books.id")
      .innerJoin("authors", "books.author_id", "authors.id")
      .where("borrowings.student_id", studentId)
      .whereNull("borrowings.returned_date");

    res.json(activeBorrowings);
  } catch (err) {
    console.error(err);
    res
      .status(500)
      .json({ error: "Neizdevās iegūt aktīvās aizņemtās grāmatas" });
  }
});

// TODO: Uzdevumi turpmākai izstrādei:
// 1. Izveidot POST /borrowings endpoint, kas ļauj izsniegt grāmatu skolēnam (pievieno jaunu ierakstu borrowings tabulā)
// 2. Izveidot PUT /borrowings/:id/return endpoint, kas atzīmē grāmatu kā atgrieztu (atjaunina returned_date lauku)
// 3. Pievienot validāciju - pārbaudīt vai grāmata jau ir izsniegta pirms jaunas izsniegšanas
// 4. Izveidot GET /books/:id/availability endpoint, kas parāda vai grāmata ir pieejama aizņemšanai
// 5. Pievienot pagināciju GET /students un GET /books endpoint'iem (limit un offset parametri)

const server = app.listen(PORT, () => {
  console.log(`Serveris darbojas adresē http://localhost:${PORT}`);
});

server.on("error", (err) => {
  if (err && err.code === "EADDRINUSE") {
    console.error(
      `Ports ${PORT} jau tiek izmantots. Pamēģini palaist ar citu portu, piemēram: PORT=5001 npm run dev`,
    );
  } else {
    console.error(err);
  }
  process.exit(1);
});
