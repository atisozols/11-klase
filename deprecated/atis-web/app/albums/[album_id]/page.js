import Link from "next/link";

const page = async ({ params }) => {
  const { album_id } = await params;
  const res = await fetch(`http://localhost:5000/albums/${album_id}`);
  const album = await res.json();

  const resArtist = await fetch(`http://localhost:5000/artists/${album.artist_id}`);
  const artist = await resArtist.json();

  return (
    <div>
      <div className="bg-gray-400 w-full">
        <Link href={"/artists"}>Artists</Link> &gt;{" "}
        <Link href={`/artists/${artist.id}`}>{artist.name}</Link> &gt;{" "}
        <Link href={`/albums/${album.id}`}>{album.title}</Link>
      </div>

      {album.songs.map((song) => (
        <h2 key={song.id}>{song.title}</h2>
      ))}
    </div>
  );
};

export default page;
