import BusinessCard from "@/components/BusinessCard";
import Collapsible from "@/components/Collapsible";
import PlusMinus from "@/components/PlusMinus";

export default function Home() {
  const businessPeople = [
    { name: "Atis Ozols", phone: "27804609" },
    { name: "Jānis Bērziņš", phone: "29123456" },
    { name: "Anna Kalniņa", phone: "26987654" },
    { name: "Pēteris Liepiņš", phone: "28456789" },
    { name: "Līga Ozoliņa", phone: "25321654" },
  ];

  return (
    <div>
      <PlusMinus />
      <Collapsible />
    </div>
  );
}
