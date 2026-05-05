export default async function LibraryPage() {
  const res = await fetch("http://localhost:5001/authors");
  const authors = await res.json();
  console.log(authors);

  return (
    <div>
      {authors.map((author) => (
        <div key={author.id}>
          <p>{author.name}</p>
        </div>
      ))}
    </div>
  );
}
