import Link from "next/link";

export default async function AuthorsPage() {
  const res = await fetch("http://localhost:5001/authors");
  const authors = await res.json();
  console.log(authors);

  return (
    <div>
      {authors.map((author) => (
        <div key={author.id}>
          <Link href={`/library/authors/${author.id}`}>{author.name}</Link>
        </div>
      ))}
    </div>
  );
}
