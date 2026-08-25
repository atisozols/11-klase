import Product from "@/components/Product";

const page = async () => {
  const response = await fetch("https://dummyjson.com/c/88a0-86d9-4480-a623");
  const data = await response.json();

  return (
    <div className="p-5 grid grid-cols-2 gap-3">
      {data.map((item) => (
        <Product key={item.id} item={item} />
      ))}
    </div>
  );
};

export default page;
