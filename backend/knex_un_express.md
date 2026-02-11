# Knex: kā tas strādā starp Express un SQL (PostgreSQL)

Tu jau:

- proti uztaisīt vienkāršu Express serveri
- proti uzrakstīt `GET` un `POST` endpointus
- zini, kas ir PostgreSQL un kā rakstīt pamata SQL (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)

Šajā materiālā mērķis ir saprast, kas ir **Knex**, kāpēc to lieto un kā tas palīdz Express aplikācijai runāt ar SQL datubāzi.

---

## 1) Kas ir Knex?

**Knex.js** ir **SQL query builder** (SQL vaicājumu būvētājs) priekš Node.js.

- Tas **nav** datubāze.
- Tas **nav** Express.

Knex palīdz:

- rakstīt SQL vaicājumus JavaScript veidā (virknējot metodes)
- drošāk padot parametrus (mazāk iespēju “SQL injection” kļūdām, ja lieto pareizi)
- uzturēt **migrācijas** (datubāzes shēmas izmaiņu vēsturi)
- veidot **seed** (testa/izstrādes datus)

Svarīgā ideja: **Knex “pārtulko” tavu JavaScript vaicājuma aprakstu uz SQL** un tad izpilda to caur datubāzes draiveri (PostgreSQL gadījumā – `pg`).

---

## 2) Kur Knex atrodas starp Express un SQL?

Tipiska datu plūsma, kad lietotājs izsauc API:

1. Klients (piem., pārlūks/React/Thunder) sūta HTTP pieprasījumu uz tavu serveri.
2. Express saņem pieprasījumu un ieiet konkrētā maršrutā (route).
3. Tavs route/handler izsauc datu piekļuves kodu (piem., “repository” vai “db” funkcijas).
4. Šajās funkcijās tu lieto **Knex**, lai:
   - uzbūvētu vaicājumu
   - iedotu parametrus
   - izpildītu vaicājumu
5. Knex izmanto `pg` (vai citu draiveri), lai nosūtītu SQL uz PostgreSQL.
6. PostgreSQL atgriež rezultātu.
7. Knex atgriež rezultātu JavaScript objektu/masīvu formā.
8. Express uztaisa JSON atbildi un nosūta to klientam.

Īsā frāze, ko atcerēties:

- **Express**: HTTP un maršrutēšana
- **Knex**: SQL vaicājumu veidošana/izpilde
- **PostgreSQL**: datu glabāšana un SQL izpilde

---

## 3) Knex salīdzinājumā ar “raw SQL” Node vidē

Ja tu nelieto Knex, tu parasti lieto `pg` un raksti SQL kā tekstu:

```js
const result = await pool.query("select * from users where id = $1", [id]);
```

Ar Knex tas pats izskatās bieži vien lasāmāk:

```js
const user = await knex("users").where({ id }).first();
```

Abos gadījumos beigās PostgreSQL saņem SQL. Atšķirība:

- `pg`: tu pats raksti SQL tekstu
- Knex: tu biežāk raksti **JavaScript ķēdes**, un Knex uzģenerē SQL

Svarīgi: Knex **nenoņem nepieciešamību saprast SQL**. Tas vienkārši padara rakstīšanu ērtāku un strukturētāku.

---

## 4) Minimālais komplekts: ko vajag, lai Knex strādātu ar Postgres?

Parasti vajag:

- `knex`
- Postgres draiveri `pg`

Instalācija (piemērs):

```bash
npm i knex pg
```

Knex konfigurācijas ideja ir šāda: tu izveido **vienu Knex instance** (savienojumu ar DB), un tad to importē tur, kur vajag.

### 4.1) Knex instance (savienojums)

Vienkāršota ideja (piemērs):

```js
import knexLib from "knex";

export const knex = knexLib({
  client: "pg",
  connection: {
    host: process.env.DB_HOST,
    port: Number(process.env.DB_PORT),
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
  },
});
```

Praktiski:

- **Savienojuma dati jāliek `ENV` mainīgajos**, nevis jāieraksta kodā.
- Instancei jābūt **vienai** (nevis jātaisa jauna katrā request).

---

## 5) Kā izskatās Knex vaicājumi (pamati)

Pieņemsim, ka tev datubāzē ir tabula `users` ar kolonnām:

- `id` (piem., `serial` / `uuid`)
- `name` (text)
- `email` (text)

### 5.1) SELECT (visi)

```js
const users = await knex("users").select("*");
```

### 5.2) SELECT ar `where`

```js
const users = await knex("users").where({ name: "Anna" }).select("*");
```

### 5.3) SELECT vienu rindu (`first`)

```js
const user = await knex("users").where({ id: userId }).first();
```

### 5.4) INSERT

```js
const [createdUser] = await knex("users")
  .insert({ name, email })
  .returning(["id", "name", "email"]);
```

`returning(...)` ir īpaši noderīgs PostgreSQL gadījumā, lai uzreiz saņemtu atpakaļ ievietoto rindu.

### 5.5) UPDATE

```js
const [updatedUser] = await knex("users")
  .where({ id: userId })
  .update({ name })
  .returning(["id", "name", "email"]);
```

### 5.6) DELETE

```js
const deletedCount = await knex("users").where({ id: userId }).del();
```

---

## 6) Kāpēc Knex ir drošāks par SQL teksta “salīmēšanu”?

Bīstami ir darīt šādi (NEIETEICAMS):

```js
const result = await knex.raw(`select * from users where email = '${email}'`);
```

Ja `email` nāk no lietotāja ievades, viņš var mēģināt ielikt ļaunprātīgu tekstu.

Pareizā ideja:

- lieto Knex query builder (`where`, `insert`, `update`)
- vai, ja lieto `raw`, tad **parametrizē**

Parametrizēts `raw` piemērs:

```js
const result = await knex.raw("select * from users where email = ?", [email]);
```

Query builder parasti pats dara šo parametrizāciju tavā vietā.

---

## 7) Knex + Express: vienkāršs piemērs ar `GET` un `POST`

Svarīga prakse: maršruti (routes) nedrīkst kļūt par “milzu failu ar visu loģiku”. Bieži atdala:

- `routes/` (HTTP slānis)
- `db/` vai `repositories/` (SQL/Knex slānis)

### 7.1) DB funkcijas (piemērs)

```js
export async function getAllUsers(knex) {
  return knex("users").select("id", "name", "email");
}

export async function createUser(knex, { name, email }) {
  const [created] = await knex("users")
    .insert({ name, email })
    .returning(["id", "name", "email"]);

  return created;
}
```

### 7.2) Express routes (piemērs)

```js
import express from "express";
import { knex } from "./db/knex.js";
import { getAllUsers, createUser } from "./db/users.js";

const app = express();
app.use(express.json());

app.get("/users", async (req, res, next) => {
  try {
    const users = await getAllUsers(knex);
    res.json(users);
  } catch (err) {
    next(err);
  }
});

app.post("/users", async (req, res, next) => {
  try {
    const { name, email } = req.body;

    if (!name || !email) {
      return res.status(400).json({ error: "Trūkst name vai email" });
    }

    const created = await createUser(knex, { name, email });
    res.status(201).json(created);
  } catch (err) {
    next(err);
  }
});

app.use((err, req, res, next) => {
  res.status(500).json({ error: "Servera kļūda" });
});

app.listen(3000);
```

Ko te ir svarīgi pamanīt:

- `knex` instance tiek izveidota vienreiz un importēta.
- Vaicājumi ir atsevišķās funkcijās.
- Kļūdas tiek apstrādātas ar `try/catch` un `next(err)`.

---

## 8) Migrācijas: kāpēc tās ir vajadzīgas?

Ja tu taisi backend projektu komandā vai vienkārši gribi sakārtotu attīstību, migrācijas ļauj:

- aprakstīt DB struktūras izmaiņas kodā
- droši uzlikt shēmu no jauna (`migrate:latest`)
- atgriezties atpakaļ (`rollback`)

Bez migrācijām bieži notiek haoss:

- “Manā datorā ir viena tabulas versija, tavā – cita.”

### 8.1) Knex migrāciju ideja

Migrācija ir fails ar 2 funkcijām:

- `up` – kā uzlikt izmaiņu
- `down` – kā atcelt izmaiņu

Piemērs (vienkāršota doma) tabulai `users`:

```js
export async function up(knex) {
  await knex.schema.createTable("users", (table) => {
    table.increments("id").primary();
    table.text("name").notNullable();
    table.text("email").notNullable().unique();
  });
}

export async function down(knex) {
  await knex.schema.dropTable("users");
}
```

---

## 9) Seed: kam tas noder?

Seed faili ļauj ātri ielikt testa datus:

- lai uzreiz var testēt `GET /users`
- lai var uztaisīt demo

Ideja: seed izpilda vairākus `insert` uz tabulām.

---

## 10) Transakcijas: kad ar vienu vaicājumu nepietiek

Transakcija vajadzīga, ja tev ir vairāki vaicājumi, kuriem jāizpildās “vai nu visi, vai neviens”.

Piemērs situācijai:

- izveido lietotāju
- izveido lietotājam profilu

Ja otrais vaicājums neizdodas, pirmais arī jāatceļ.

Knex ideja (vienkāršoti):

```js
await knex.transaction(async (trx) => {
  const [user] = await trx("users").insert({ name, email }).returning(["id"]);

  await trx("profiles").insert({ user_id: user.id, bio: "" });
});
```

Ja transakcijas iekšā notiek kļūda, Knex automātiski veic rollback.

---

## 11) Praktiska projekta struktūra (viens no variantiem)

Vienkāršs variants mazam mācību projektam:

- `src/app.js` – Express konfigurācija
- `src/db/knex.js` – Knex instance
- `src/db/users.js` – DB funkcijas priekš `users`
- `src/routes/users.js` – `/users` maršruti
- `.env` – DB pieslēguma dati

Svarīgākā doma: **nebliez visu vienā failā**.

---

## 12) Ko darīt, ja vajag “īstu SQL”?

Dažreiz query builder nav ērts (piem., ļoti sarežģīti `JOIN`, `WITH`, specifiskas Postgres funkcijas).

Tad ir 2 pieejas:

- turpināt lietot Knex, bet ar `join`, `select`, `where` utt.
- lietot `knex.raw(...)` ar parametrizāciju

Knex priekšrocība: tu joprojām paliec vienā “DB slānī” ar kopīgu savienojumu, transakcijām utt.

---

## 13) Biežākās kļūdas un padomi

- **Jauns `knex(...)` katrā request**
  - tas var radīt daudz savienojumu un sliktu veiktspēju
  - taisi vienu instance un izmanto to visur

- **Aizmirsts `await`**
  - atgriezīsies `Promise`, nevis dati

- **`returning(...)` neizmantošana, kad vajag atbildē izveidoto objektu**
  - īpaši `POST` gadījumā tas ir ērti

- **Nevalidē `req.body`**
  - DB kļūdas (piem., `not null` vai `unique`) ir normāli, bet lietotājam jāsaņem saprotama atbilde

---

## 14) Mini “špikeris” (cheat sheet)

- Visi:

```js
await knex("users").select("*");
```

- Pēc ID:

```js
await knex("users").where({ id }).first();
```

- Ievietot:

```js
await knex("users").insert({ name, email }).returning("*");
```

- Atjaunināt:

```js
await knex("users").where({ id }).update({ name }).returning("*");
```

- Dzēst:

```js
await knex("users").where({ id }).del();
```

---

## 15) Kopsavilkums

- Knex ir **SQL vaicājumu būvētājs** Node.js vidē.
- Express apstrādā HTTP, bet Knex palīdz tavām maršrutu funkcijām ērti un droši izpildīt SQL.
- Knex “pa vidu” starp Express un PostgreSQL dara 2 galvenās lietas:
  - uzģenerē SQL no JavaScript query builder ķēdēm
  - izpilda SQL caur DB draiveri un atgriež rezultātus JS formātā
