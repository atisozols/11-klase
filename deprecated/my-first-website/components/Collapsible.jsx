"use client";
import { useState } from "react";

export default function Collapsible() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="my-3 border border-blue-400 rounded-xl">
      <div className="flex justify-between p-3">
        <span>Šis ir atverams component</span>
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="underline cursor-pointer"
        >
          Atvērt
        </button>
      </div>
      {isOpen && (
        <div className="border-t border-blue-400 p-3">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus
            ex enim quas veritatis, inventore perspiciatis assumenda facere
            officiis illo aspernatur necessitatibus quidem consectetur,
            blanditiis illum.
          </p>
        </div>
      )}
    </div>
  );
}
