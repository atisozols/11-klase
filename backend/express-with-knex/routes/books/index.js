const knex = require("../../db");
const express = require("express");
const router = express.Router();

router.route("/").get(async (req, res) => {
  try {
    const books = await knex("books").select("*");
    res.json(books);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt grāmatas" });
  }
});

router.route("/").post(async (req, res) => {
  try {
    const { title, authorId, publishedYear } = req.body;

    if (!title || !authorId || !publishedYear) {
      return res.status(400).json({ error: "Trūkst grāmatas dati" });
    }

    const author = await knex("authors")
      .select("id")
      .where({ id: authorId })
      .first();

    if (!author) {
      return res.status(404).json({ error: "Autors nav atrasts" });
    }

    const [createdBook] = await knex("books")
      .insert({
        title: title,
        author_id: authorId,
        published_year: publishedYear,
      })
      .returning(["title", "author_id", "published_year"]);

    res.status(201).json(createdBook);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās izveidot autoru" });
  }
});

router.route("/:id/availability").get(async (req, res) => {
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

router.route("/:id/history").get(async (req, res) => {
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

module.exports = router;
