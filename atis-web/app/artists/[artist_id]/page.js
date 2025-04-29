import Link from "next/link";

const page = async ({ params }) => {
  const { artist_id } = await params;
  const res = await fetch(`http://localhost:5000/artists/${artist_id}`);
  const artist = await res.json();

  return (
    <div>
      <div className="bg-gray-400 w-full">
        <Link href={"/artists"}>Artists</Link> &gt;{" "}
        <Link href={`/artists/${artist_id}`}>{artist.name}</Link>
      </div>

      <div className="flex flex-col">
        {artist.artist_albums.map((album) => (
          <Link href={`/albums/${album.id}`} key={album.id}>
            {album.title}
          </Link>
        ))}
      </div>
    </div>
  );
};

export default page;
