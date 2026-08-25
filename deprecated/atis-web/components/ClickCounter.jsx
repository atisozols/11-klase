"use client";
import { useState } from "react";

const ClickCounter = ({ initial = 0 }) => {
  const [count, setCount] = useState(initial);

  const incrementCount = () => {
    setCount(count + 1);
  };

  return (
    <button
      onClick={incrementCount}
      className="flex justify-center items-center rounded-full p-3 w-10 h-10 mt-5 mx-auto bg-emerald-800"
    >
      {count}
    </button>
  );
};

export default ClickCounter;
