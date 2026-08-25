export default function TennisHeader() {
  return (
    <div className="text-blue-300">
      <div className="border-b border-b-blue-300 p-12 text-4xl font-bold  text-center">
        Tennis Legends
      </div>
      <nav>
        <ul className="flex justify-around p-2 border-b border-b-blue-300">
          <li className="border">Home</li>
          <li>Career</li>
          <li>Achievments</li>
          <li>Gallery</li>
          <li>Contact</li>
          <li className="w-1/5 text-right">Sign In</li>
        </ul>
      </nav>
    </div>
  );
}
