import Link from "next/link";

const page = async () => {
  const res = await fetch("http://localhost:5000/albums");
  const albums = await res.json();

  return (
    <div className="flex flex-col">
      {albums.map((album) => (
        <Link href={`/albums/${album.id}`} key={album.id}>
          {album.title}
        </Link>
      ))}
    </div>
  );
};

export default page;
