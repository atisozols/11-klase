import BlogPost from "@/components/BlogPost";

const BlogPostList = ({ posts }) => {
  return (
    <div className="flex flex-col gap-5 p-5">
      {posts.map((post) => (
        <BlogPost post={post} key={post.id} />
      ))}
    </div>
  );
};

export default BlogPostList;
