const Profile = ({ name, isMorning }) => {
  // nosacijums ? ja nosacijums ir true : ja nosac ir false
  // nosacijums && ja nosacijums ir true

  return (
    <div className="text-center p-5 bg-zinc-500">
      <p>
        Good {isMorning ? "morning" : "evening"}, {name}!
      </p>
      {isMorning && <p>Have a great day!</p>}
    </div>
  );
};

export default Profile;
