import "./styles.css";

function Form() {
  return (
    <div className="form-wrapper">
      <form className="main-form">
        <input type="text" placeholder="Nome do Estudante" />
        <input type="text" placeholder="Turma" />
        <input type="number" placeholder="Idade" />

        <button type="submit">Enviar</button>
      </form>
    </div>
  );
}

export default Form;
