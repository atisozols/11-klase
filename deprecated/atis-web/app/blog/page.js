import BlogHeader from "@/components/BlogHeader";
import BlogPostList from "@/components/BlogPostList";

const page = () => {
  const blogData = [
    {
      id: 1,
      title: "The Future of Web Development",
      content:
        "Web development is constantly evolving, with new frameworks, tools, and best practices emerging every year...",
      author: {
        name: "John Doe",
        bio: "Full-stack developer with a passion for modern web technologies.",
      },
      comments: [
        {
          id: 1,
          author: "Alice",
          text: "Great insights, John! I agree that keeping up with trends is crucial.",
        },
        {
          id: 2,
          author: "Bob",
          text: "Thanks for sharing! Do you have any recommendations on which framework to focus on?",
        },
      ],
    },
    {
      id: 2,
      title: "10 Tips for Better Remote Work",
      content:
        "With remote work becoming the new norm, it’s essential to develop habits that ensure productivity and work-life balance...",
      author: {
        name: "Jane Smith",
        bio: "Remote work expert and lifestyle coach, helping people thrive while working from home.",
      },
      comments: [
        {
          id: 1,
          author: "Charlie",
          text: "These tips are lifesavers! I’ve struggled with work-life balance, so I'll definitely try some of these out.",
        },
        {
          id: 2,
          author: "Dave",
          text: "Thanks, Jane! The point about setting boundaries really hit home.",
        },
      ],
    },
    {
      id: 3,
      title: "Why JavaScript is Still Dominating",
      content:
        "Despite the rise of new languages and frameworks, JavaScript continues to be the dominant programming language...",
      author: {
        name: "Emily Johnson",
        bio: "Senior software engineer specializing in front-end development and JavaScript frameworks.",
      },
      comments: [
        {
          id: 1,
          author: "Frank",
          text: "JavaScript has been around for decades, and it's amazing how it's still relevant!",
        },
        {
          id: 2,
          author: "Grace",
          text: "I believe the ecosystem around JS is a big reason for its continued success.",
        },
      ],
    },
  ];

  return (
    <div className="bg-gray-100 min-h-screen">
      <BlogHeader />
      <BlogPostList posts={blogData} />
    </div>
  );
};

export default page;
