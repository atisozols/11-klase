export default function BusinessCard({
  name = "Jānis Paraudziņš",
  phone = "29123456",
}) {
  return (
    <div className="bg-gray-300 text-black p-6 m-2 rounded-3xl border flex justify-between border-blue-600">
      <p className="font-bold">{name}</p>
      <p>{phone}</p>
    </div>
  );
}
