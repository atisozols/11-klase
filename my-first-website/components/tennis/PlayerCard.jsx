import Image from "next/image";

export default function PlayerCard({ name, bio, image, imageDesc }) {
  return (
    <div className="p-5 m-5 flex gap-5 justify-around border border-amber-400 rounded-3xl">
      <div className="rounded-tl-3xl overflow-hidden">
        <Image
          src={image}
          alt={name}
          width={2116}
          height={1858}
          className="w-[450px]"
        />
        <p>{imageDesc}</p>
      </div>
      <div>
        <p>
          <span className="font-bold">{name} </span>
          {bio}
        </p>
      </div>
    </div>
  );
}
