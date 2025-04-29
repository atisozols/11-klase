"use client";
import { useState } from "react";

const ColorChangingButton = () => {
  const [color, setColor] = useState("#e4ab1f");

  const changeColor = () => {
    var letters = "0123456789ABCDEF";
    var c = "#";
    for (var i = 0; i < 6; i++) {
      c += letters[Math.floor(Math.random() * 16)];
    }
    console.log(color);
    setColor(c);
  };

  return (
    <button
      onClick={changeColor}
      className={`flex justify-center items-center rounded-full p-3 w-10 h-10 mt-5 mx-auto`}
      style={{ backgroundColor: color }}
    >
      Click
    </button>
  );
};

export default ColorChangingButton;
