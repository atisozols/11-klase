const express = require("express");
const knex = require("./db/knex");
const app = express();

// iekļaujot šo, ir iespējams piekļūt request body
app.use(express.json());

// veicot GET pieprasījumu uz mūsu servera "/" adresi, tiks atgriezts { message: "Hello World" }
app.get("/", (req, res) => {
  res.json({ message: "Hello World!" });
});

// veicot POST, varam nosūtīt informāciju no Front-end, izmantojot fetch, pievienojot JS objektu iekš request body
app.post("/", (req, res) => {
  const data = req.body; // piekļūstam request body
  console.log(data);
  const message = "Hello, " + data.name + "!";

  res.json({ message });
});

// veicot GET uz "/album/123", tiks iegūta albumId vērtība
app.get("/albums/:albumId", async (req, res) => {
  const aId = req.params.albumId;
  const album = await knex.select("*").from("album").where({ id: aId }).first();

  const songs = await knex.select("*").from("song").where({ album_id: aId });

  res.json({ ...album, songs });
});

app.get("/albums", async (req, res) => {
  const albums = await knex.select("*").from("album");
  res.json(albums);
});

app.post("/albums", async (req, res) => {
  const albumData = req.body;

  if (
    !albumData.id ||
    !albumData.title ||
    !albumData.release ||
    !albumData.artist_id
  ) {
    res.status(400).json({ message: "Trūkst nepieciešamie lauki!" });
  }

  await knex("album").insert(albumData);

  res.json(albumData);
});

app.get("/artists", async (req, res) => {
  const artists = await knex.select("*").from("artist");
  res.json(artists);
});

app.get("/artists/:artistId", async (req, res) => {
  const aId = req.params.artistId;

  const artist = await knex
    .select("*")
    .from("artist")
    .where({ id: aId })
    .first();

  const artist_albums = await knex
    .select("*")
    .from("album")
    .where({ artist_id: aId });

  res.json({ ...artist, artist_albums });
});

const server = app.listen(5000, () => {
  console.log("Server running on 5000");
});

process.on("SIGTERM", () => {
  server.close(() => {
    console.log("Server closed gracefully!");
    process.exit(0);
  });
});
