import Image from "next/image";

export default function PlayerCard() {
  return (
    <div className="p-5 flex justify-around">
      <div className="w-1/4 rounded-tl-3xl overflow-hidden">
        <Image src="/nadal.png" alt="Rafael Nadal" width={2116} height={1858} />
        <p>This is a placeholder description that will get replaced</p>
      </div>
      <div>
        This is another placeholder description that will also get replaced
      </div>
    </div>
  );
}
