import PlayerCard from "@/components/tennis/PlayerCard";
import TennisHeader from "@/components/tennis/TennisHeader";

export default function TennisPage() {
  const players = [
    {
      name: "Rafael Nadal",
      bio: "a Spanish former professional tennis player. He was ranked as the world No. 1 in men's singles by the Association of Tennis Professionals (ATP) for 209 weeks.",
      image: "/nadal.png",
      imageDesc: "Rafael Nadal playing tennis",
    },
    {
      name: "Roger Federer",
      bio: "a Swiss former professional tennis player. He was ranked as the world No. 1 in men's singles by the Association of Tennis Professionals (ATP) for 310 weeks, including a record 237 consecutive weeks.",
      image: "/federer.png",
      imageDesc: "Roger Federer playing tennis",
    },
  ];

  return (
    <div>
      <TennisHeader />
      {players.map((player) => (
        <PlayerCard
          key={player.name}
          name={player.name}
          bio={player.bio}
          image={player.image}
          imageDesc={player.imageDesc}
        />
      ))}
    </div>
  );
}
