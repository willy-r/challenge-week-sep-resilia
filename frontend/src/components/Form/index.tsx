import { createStudentService } from "../../services/students.api";

import "./styles.css";

function Form() {
  const saveStudent = async (e: React.SyntheticEvent): Promise<void> => {
    e.preventDefault();
    const target = e.target as typeof e.target & {
      studentName: { value: string };
      classTag: { value: string };
      age: { value: number };
    };
    const studentName = target.studentName.value;
    const classTag = target.classTag.value;
    const age = target.age.value;

    await createStudentService({ studentName, classTag, age })
  };

  return (
    <div className="form-wrapper">
      <form className="main-form" onSubmit={saveStudent}>
        <input
          name="student-name"
          type="text"
          placeholder="Nome do Estudante"
          required
          max="255"
        />
        <input
          name="class-tag"
          type="text"
          placeholder="Turma"
          required
          max="5"
        />
        <input name="age" type="number" placeholder="Idade" required />

        <button type="submit">Enviar</button>
      </form>
    </div>
  );
}

export default Form;
