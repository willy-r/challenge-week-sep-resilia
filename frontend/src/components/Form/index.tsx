import { toast } from "react-toastify";

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

    toast.promise(
      createStudentService({ studentName, classTag, age }),
      {
        pending: "Salvando estudante no banco de dados...",
        success: "Estudante salvo com sucesso!",
        error: {
          render({ data }) {
            return data.message;
          },
        },
      },
      {
        autoClose: 3000,
        hideProgressBar: true,
        theme: "dark",
      }
    );
  };

  return (
    <div className="form-wrapper">
      <form className="main-form" onSubmit={saveStudent}>
        <input
          name="studentName"
          type="text"
          placeholder="Nome do Estudante"
          required
          max="255"
        />
        <input
          name="classTag"
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
