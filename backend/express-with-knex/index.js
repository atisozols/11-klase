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
    const studentId = Number(req.params.studentId);
    const active = req.query.active === "true"; // /borrowings/1?active=true

    if (!Number.isInteger(studentId) || studentId <= 0) {
      return res.status(400).json({ error: "Nekorekts studentId" });
    }

    const query = knex("borrowings")
      .select(
        "borrowings.id",
        "borrowings.book_id",
        "books.title",
        "authors.name as author",
        "borrowings.borrowed_at",
        "borrowings.returned_at",
      )
      .innerJoin("books", "borrowings.book_id", "books.id")
      .innerJoin("authors", "books.author_id", "authors.id")
      .where("borrowings.student_id", studentId)
      .orderBy("borrowings.borrowed_at", "desc");

    if (active) query.whereNull("borrowings.returned_at");

    const studentBorrowings = await query;

    res.json(studentBorrowings);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt izsniegtās grāmatas" });
  }
});

app.post("/borrowings", async (req, res) => {
  try {
    const studentId = Number(req.body.student_id);
    const bookId = Number(req.body.book_id);

    if (!Number.isInteger(studentId) || studentId <= 0) {
      return res.status(400).json({ error: "student_id jābūt pozitīvam skaitlim" });
    }

    if (!Number.isInteger(bookId) || bookId <= 0) {
      return res.status(400).json({ error: "book_id jābūt pozitīvam skaitlim" });
    }

    const student = await knex("students")
      .select("id")
      .where({ id: studentId })
      .first();

    if (!student) {
      return res.status(404).json({ error: "Skolēns nav atrasts" });
    }

    const book = await knex("books").select("id").where({ id: bookId }).first();

    if (!book) {
      return res.status(404).json({ error: "Grāmata nav atrasta" });
    }

    const alreadyBorrowed = await knex("borrowings")
      .select("id")
      .where({ book_id: bookId })
      .whereNull("returned_at")
      .first();

    if (alreadyBorrowed) {
      return res.status(409).json({ error: "Grāmata jau ir izsniegta" });
    }

    const [createdBorrowing] = await knex("borrowings")
      .insert({
        student_id: studentId,
        book_id: bookId,
      })
      .returning(["id", "student_id", "book_id", "borrowed_at", "returned_at"]);

    res.status(201).json(createdBorrowing);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās izsniegt grāmatu" });
  }
});

app.put("/borrowings/:id/return", async (req, res) => {
  try {
    const borrowingId = Number(req.params.id);

    if (!Number.isInteger(borrowingId) || borrowingId <= 0) {
      return res.status(400).json({ error: "Nekorekts borrowing id" });
    }

    const borrowing = await knex("borrowings")
      .select("id", "returned_at")
      .where({ id: borrowingId })
      .first();

    if (!borrowing) {
      return res.status(404).json({ error: "Aizņemšanās ieraksts nav atrasts" });
    }

    if (borrowing.returned_at) {
      return res.status(400).json({ error: "Grāmata jau ir atgriezta" });
    }

    const [updatedBorrowing] = await knex("borrowings")
      .where({ id: borrowingId })
      .update({ returned_at: knex.fn.now() })
      .returning(["id", "student_id", "book_id", "borrowed_at", "returned_at"]);

    res.json(updatedBorrowing);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās atzīmēt grāmatu kā atgrieztu" });
  }
});

app.get("/books/:id/availability", async (req, res) => {
  try {
    const bookId = Number(req.params.id);

    if (!Number.isInteger(bookId) || bookId <= 0) {
      return res.status(400).json({ error: "Nekorekts book id" });
    }

    const book = await knex("books")
      .select("id", "title", "author_id", "published_year")
      .where({ id: bookId })
      .first();

    if (!book) {
      return res.status(404).json({ error: "Grāmata nav atrasta" });
    }

    const activeBorrowing = await knex("borrowings")
      .select("id", "student_id", "borrowed_at")
      .where({ book_id: bookId })
      .whereNull("returned_at")
      .first();

    res.json({
      book,
      is_available: !activeBorrowing,
      active_borrowing: activeBorrowing ?? null,
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt pieejamības informāciju" });
  }
});

app.get("/books/:id/history", async (req, res) => {
  try {
    const bookId = Number(req.params.id);

    if (!Number.isInteger(bookId) || bookId <= 0) {
      return res.status(400).json({ error: "Nekorekts book id" });
    }

    const book = await knex("books")
      .select("id", "title", "author_id", "published_year")
      .where({ id: bookId })
      .first();

    if (!book) {
      return res.status(404).json({ error: "Grāmata nav atrasta" });
    }

    const history = await knex("borrowings")
      .select(
        "borrowings.id",
        "borrowings.student_id",
        "students.name as student_name",
        "students.email as student_email",
        "borrowings.borrowed_at",
        "borrowings.returned_at",
      )
      .innerJoin("students", "borrowings.student_id", "students.id")
      .where("borrowings.book_id", bookId)
      .orderBy("borrowings.borrowed_at", "asc");

    res.json({
      book,
      history,
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt grāmatas vēsturi" });
  }
});

// TODO: Pievienot `POST /authors`, lai varētu izveidot jaunu autoru (name, country).
// TODO: Pievienot `POST /books`, lai varētu pievienot jaunu grāmatu ar pārbaudi, ka `author_id` eksistē.
// TODO: Pievienot `POST /students`, lai varētu pievienot jaunu skolēnu (name, email, grade).
// TODO: Pievienot `PUT /students/:id`, lai varētu atjaunināt skolēna datus.
// TODO: Pievienot `DELETE /students/:id`, atļaujot dzēšanu tikai tad, ja nav aktīvu aizņēmumu.

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
