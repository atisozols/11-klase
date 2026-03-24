const knex = require("../../db");
const express = require("express");
const router = express.Router();

// Atgriež skolēna aizņēmumus; ar `?active=true` tikai aktīvos.
router.route("/borrowings/:studentId").get(async (req, res) => {
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

// Izveido jaunu aizņēmumu, ja skolēns un grāmata eksistē un grāmata nav izsniegta.
router.route("/borrowings").post(async (req, res) => {
  try {
    const studentId = Number(req.body.student_id);
    const bookId = Number(req.body.book_id);

    if (!Number.isInteger(studentId) || studentId <= 0) {
      return res
        .status(400)
        .json({ error: "student_id jābūt pozitīvam skaitlim" });
    }

    if (!Number.isInteger(bookId) || bookId <= 0) {
      return res
        .status(400)
        .json({ error: "book_id jābūt pozitīvam skaitlim" });
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

// Atzīmē aizņēmumu kā atgrieztu, uzstādot `returned_at` laiku.
router.route("/borrowings/:id/return").put(async (req, res) => {
  try {
    const borrowingId = Number(req.params.id);

    if (!Number.isInteger(borrowingId) || borrowingId <= 0) {
      return res.status(400).json({ error: "Nekorekts borrowing id" });
    }

    const borrowing = await knex("borrowings") // SELECT id, returned_at FROM borrowings WHERE id=borrowingId LIMIT 1;
      .select("id", "returned_at")
      .where({ id: borrowingId })
      .first();

    if (!borrowing) {
      return res
        .status(404)
        .json({ error: "Aizņemšanās ieraksts nav atrasts" });
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

module.exports = router;
