const page = async () => {
  const response = await fetch("https://dummyjson.com/c/ccc2-e210-45a8-abb1");
  const data = await response.json();

  return <div className="p-5 grid grid-cols-2 gap-3">players</div>;
};

export default page;
