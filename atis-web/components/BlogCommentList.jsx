const BlogCommentList = ({ post }) => {
  return (
    <div>
      <h3 className="text-xl font-bold">Comments</h3>
      {post.comments.map((comment) => (
        <div className="flex gap-5" key={comment.id}>
          <span className="font-bold">{comment.author}:</span>
          <span>{comment.text}</span>
        </div>
      ))}
    </div>
  );
};

export default BlogCommentList;
