const BlogAuthor = ({ post }) => {
  return (
    <div className="text-gray-500">
      <h3 className="font-bold text-sm">{post.author.name}</h3>
      <h3 className="text-sm">{post.author.bio}</h3>
    </div>
  );
};

export default BlogAuthor;
