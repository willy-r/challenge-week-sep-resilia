import { useEffect, useState } from "react";

import Loading from "../Loading";
import NoData from "../NoData";
import { getStudents } from "../../services/students.api";

import Table from "./Table";

import "./styles.css";

function Data() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    getStudents()
      .then((r) => r.json())
      .then((data) => setStudents(data))
      .catch((err) => console.log(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return <Loading />;
  }

  if (!students.length) {
    return <NoData />;
  }

  return (
    <section className="main-data">
      <Table data={students} />
      <div>Testing</div>
    </section>
  );
}

export default Data;
