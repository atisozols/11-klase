import Link from "next/link";

const page = async () => {
  const res = await fetch("http://localhost:5000/artists");
  const artists = await res.json();

  return (
    <div className="flex flex-col">
      <div className="bg-gray-400 w-full">
        <Link href="/artists">Artists</Link>
      </div>

      {artists.map((artist) => (
        <Link href={`/artists/${artist.id}`} key={artist.id}>
          {artist.name}
        </Link>
      ))}
    </div>
  );
};

export default page;
