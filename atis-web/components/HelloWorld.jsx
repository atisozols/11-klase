const HelloWorld = ({ message = "How are you?" }) => {
  const now = Date();

  return (
    <div className="text-center font-extrabold text-rose-700 p-14 bg-slate-800">
      <h1>Hello World!</h1>
      <p className="font-thin">{message}</p>
      <p className="text-xs font-thin">{now}</p>
    </div>
  );
};

export default HelloWorld;
