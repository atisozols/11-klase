const Product = ({ item }) => {
  return (
    <div className="border border-black rounded-3xl p-3">
      <span className="text-4xl font-black">${item.price}</span>
      <h3 className="font-bold">{item.name}</h3>
      <p className="text-sm">{item.description}</p>
    </div>
  );
};

export default Product;
