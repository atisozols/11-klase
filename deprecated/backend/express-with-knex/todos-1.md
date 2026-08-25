# TODO uzdevumi — 1. daļa

## 1. `GET /books/search` — Grāmatu meklēšana

Izveido endpoint, kas ļauj meklēt grāmatas pēc nosaukuma vai autora vārda.

- Query parametrs: `?q=...` (piemēram, `/books/search?q=Harry`)
- Meklē gan grāmatas nosaukumā, gan autora vārdā (case-insensitive — reģistram nav nozīmes)
  - Izmanto `.whereILike('books.title', q)` un `.orWhereILike('authors.name', q)` — Knex iebūvētās funkcijas case-insensitive meklēšanai
- Atgriež masīvu ar atrastajām grāmatām, katrā — `id`, `title`, `published_year`, `author_name`
  - Lai iegūtu `author_name`, izmanto `.join('authors', 'books.author_id', 'authors.id')` un `.select('authors.name as author_name')`
- Ja `q` parametrs nav norādīts, atgriež kļūdu `400`
- Izmanto `.join()`, `.select()`, `.whereILike()`, `.orWhereILike()`

---

## 2. `GET /borrowings/overdue` — Kavētie aizņēmumi

Izveido endpoint, kas atgriež visus aizņēmumus, kas nav atgriezti un ir vecāki par 14 dienām.

- Nav nepieciešami parametri
- Atgriež masīvu ar kavētajiem aizņēmumiem, katrā — `borrowing_id`, `student_name`, `book_title`, `borrowed_at`, `days_overdue`
- `days_overdue` aprēķina kā starpību starp šodienu un `borrowed_at`
- Lai filtrētu kavētos aizņēmumus, aprēķini datumu pirms 14 dienām JavaScript pusē:
  ```js
  const fourteenDaysAgo = new Date();
  fourteenDaysAgo.setDate(fourteenDaysAgo.getDate() - 14);
  ```
  Tad izmanto `.where('borrowings.borrowed_at', '<', fourteenDaysAgo)` — atgriež tikai tos aizņēmumus, kas ir vecāki par 14 dienām
- Izmanto `.join()` lai pievienotu `students` un `books` tabulas, `.whereNull('returned_at')` neatgrieztajiem aizņēmumiem
