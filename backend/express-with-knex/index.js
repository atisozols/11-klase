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
    const students = await knex("students")
      .select("name", "email")
      .where({ id: id });
    res.json(students);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt skolēnus" });
  }
});

// izveidot GET /borrowings/:studentId
app.get("/borrowings/:studentId", async (req, res) => {
  try {
    const studentId = req.params.studentId;

    const studentBorrowings = await knex("borrowings")
      .select("*")
      .innerJoin("books", "borrowings.book_id", "books.id"); // INNER JOIN books ON borrowings.book_id = books.id

    res.json(studentBorrowings);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt izsniegtās grāmatas" });
  }
});

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
