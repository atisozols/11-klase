const knex = require("../../db");
const express = require("express");
const router = express.Router();

router.route("/").get(async (req, res) => {
  try {
    const students = await knex("students").select("name", "email");
    res.json(students);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās iegūt skolēnus" });
  }
});

router.route("/").post(async (req, res) => {
  try {
    const { name, email, grade } = req.body;

    if (!name || !email || !grade) {
      return res.status(400).json({ error: "Trūkst skolēna dati" });
    }

    if (!Number.isInteger(parseInt(grade)) || parseInt(grade) <= 0) {
      return res.status(400).json({ error: "Klase jābūt pozitīvam skaitlim" });
    }

    const [createdStudent] = await knex("students")
      .insert({
        name: name,
        email: email,
        grade: parseInt(grade),
      })
      .returning(["name", "email", "grade"]);

    res.status(201).json(createdStudent);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās ievietot skolēnu" });
  }
});

router.route("/:id").get(async (req, res) => {
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

// TODO: Pievienot `PUT /students/:id`, lai varētu atjaunināt skolēna datus.
router.route("/:id").put(async (req, res) => {
  try {
    const { name, email, grade } = req.body;
    const id = req.params.id;

    if (!name && !email && !grade) {
      return res.status(400).json({ error: "Trūkst jebkādi dati" });
    }

    if (grade && (!Number.isInteger(parseInt(grade)) || parseInt(grade) <= 0)) {
      return res.status(400).json({ error: "Klase jābūt pozitīvam skaitlim" });
    }

    const updateData = {
      ...(name && { name }),
      ...(email && { email }),
      ...(grade && { grade: parseInt(grade) }),
    };

    const [updatedStudent] = await knex("students")
      .where({ id: id })
      .update(updateData)
      .returning(["id", "name", "email", "grade"]);

    if (!updatedStudent) {
      return res.status(404).json({ error: "Skolēns nav atrasts" });
    }

    res.json(updatedStudent);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Neizdevās ievietot skolēnu" });
  }
});

module.exports = router;
