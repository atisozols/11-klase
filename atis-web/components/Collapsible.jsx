"use client";
import { useState } from "react";

const Collapsible = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleOpen = () => {
    if (isOpen) {
      setIsOpen(false);
    } else {
      setIsOpen(true);
    }
  };

  return (
    <div className="bg-slate-300 p-5 rounded-lg mt-5 mx-auto w-96 text-black">
      <button onClick={toggleOpen} className="font-bold">
        Atveramās izvēlnes virsraksts
      </button>
      {isOpen && (
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid placeat consequatur illum
          fuga eaque cumque iusto porro saepe sit sint?
        </p>
      )}
    </div>
  );
};

export default Collapsible;
