import BlogAuthor from "@/components/BlogAuthor";
import BlogCommentList from "@/components/BlogCommentList";
import BlogContent from "@/components/BlogContent";

const BlogPost = ({ post }) => {
  return (
    <div className="p-5 rounded-lg bg-white">
      <h2 className="text-xl font-bold py-2">{post.title}</h2>
      <BlogAuthor post={post} />
      <BlogContent post={post} />
      <BlogCommentList post={post} />
    </div>
  );
};

export default BlogPost;
