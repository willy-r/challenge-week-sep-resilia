const API_URL = import.meta.env.VITE_API_URL;

export async function createStudentService(student: {
  studentName: string;
  classTag: string;
  age: number;
}): Promise<Response> {
  return await fetch(`${API_URL}/students`, {
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
  })
  .then(async (r) => {
    if (!r.ok) {
        const data: { detail: string } = await r.json() 
        throw new Error(data.detail);
    }
    return r
  })
}
