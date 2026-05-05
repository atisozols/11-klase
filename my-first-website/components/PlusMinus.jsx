"use client";
import { useState, useEffect } from "react";

// ļauj izmantot stāvokļus, jo pretēji noklusētajam (servera puses izpildei), kods izpildīsies pārlūkā

export default function PlusMinus() {
  // const [mainigais, funkcija_kas_maina_mainigo] = useState(sakotneja_vertiba)
  const [number, setNumber] = useState(0);

  // useEffect izpildās katru reizi, kad mainās sarakstā padotie mainīgie
  useEffect(() => {
    console.log("number mainīgais pamainījās");
  }, [number]);

  return (
    <div className="p-5 flex gap-3 justify-center items-center rounded-2xl bg-blue-500">
      <button
        onClick={() => setNumber(number - 1)}
        className="p-2 bg-red-400 rounded-full w-10 h-10 hover:cursor-pointer"
      >
        -
      </button>
      <span className="p-2">{number}</span>
      <button
        onClick={() => setNumber(number + 1)}
        className="p-2 bg-green-400 rounded-full w-10 h-10 hover:cursor-pointer"
      >
        +
      </button>
    </div>
  );
}
