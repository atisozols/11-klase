const knex = require("../../db");
const express = require("express");
const router = express.Router();

// app.get("/authors", ) -> router.route("/").get()
router.route("/").get(async (req, res) => {
  try {
    // SELECT * FROM Authors;
    const authors = await knex("authors").select("*");
    res.json(authors);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt autorus" });
  }
});

router.route("/").post(async (req, res) => {
  try {
    const { name, country = null } = req.body;

    if (!name) {
      return res.status(400).json({ error: "Trūkst autora vārds" });
    }

    const [createdAuthor] = await knex("authors")
      .insert({
        name: name,
        country: country,
      })
      .returning(["id", "name", "country"]);

    res.status(201).json(createdAuthor);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās izveidot autoru" });
  }
});

module.exports = router;
