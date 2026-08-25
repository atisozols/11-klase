export default async function BooksPage() {
  const res = await fetch("http://localhost:5001/books");
  const books = await res.json();
  console.log(books);

  return (
    <div>
      {books.map((book) => (
        <div key={book.id}>
          <p>
            {book.name} - {book.title}
          </p>
        </div>
      ))}
    </div>
  );
}
