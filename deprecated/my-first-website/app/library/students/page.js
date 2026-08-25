export default async function StudentsPage() {
  const res = await fetch("http://localhost:5001/students");
  const students = await res.json();
  console.log(students);

  return (
    <div>
      {students.map((student) => (
        <div key={student.id}>
          <p>
            {student.name} {student.email}
          </p>
        </div>
      ))}
    </div>
  );
}
