const express = require("express");
const knex = require("./db.js");

const app = express();
const PORT = 5001;

app.use(express.json());

// Veselības pārbaudes endpoints: ātri pārbauda, ka serveris strādā.
app.get("/", (req, res) => {
  res.json({ message: "ok" });
});

app.use("/authors", require("./routes/authors"));

app.use("/books", require("./routes/books"));

app.use("/students", require("./routes/students"));

app.use("/borrowings", require("./routes/borrowings"));

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
