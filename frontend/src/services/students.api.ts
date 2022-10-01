const API_URL = import.meta.env.VITE_API_URL;

export async function createStudentService(student: {
  studentName: string;
  classTag: string;
  age: number;
}): Promise<void> {
  await fetch(`${API_URL}/students`, {
    method: "POST",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      student_name: student.studentName,
      class_tag: student.classTag,
      age: student.age,
    }),
  });
}
