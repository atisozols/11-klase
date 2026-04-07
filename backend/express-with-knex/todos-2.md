# TODO uzdevumi — 2. daļa

## 3. `DELETE /books/:id` — Grāmatas dzēšana

Izveido endpoint, kas ļauj dzēst grāmatu tikai tad, ja tā šobrīd nav aizņemta.

- Pārbauda, vai grāmata ar doto `id` eksistē — ja nē, atgriež `404`
- Pārbauda, vai grāmatai ir aktīvs aizņēmums (`returned_at IS NULL`) — ja ir, atgriež `409`
- Ja grāmata nav aizņemta, dzēš to un atgriež apstiprinājuma ziņojumu
- Ievēro to pašu loģiku kā `DELETE /students/:id`

---

## 4. `GET /students/:id/stats` — Skolēna statistika

Izveido endpoint, kas atgriež aizņēmumu statistiku konkrētam skolēnam.

- Pārbauda, vai skolēns eksistē — ja nē, atgriež `404`
- Atgriež objektu ar šādiem laukiem:
  - `student_name` — skolēna vārds
  - `total_borrowed` — kopējais aizņemto grāmatu skaits
  - `currently_active` — šobrīd neatgriezto grāmatu skaits
  - `returned` — atgriezto grāmatu skaits
- Izmanto `.count()` un `.where()` / `.whereNull()` / `.whereNotNull()`
