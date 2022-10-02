import { CompactTable } from "@table-library/react-table-library/compact";
import { useTheme } from "@table-library/react-table-library/theme";
import { usePagination } from "@table-library/react-table-library/pagination";

function Table(props: {
  data: { id: number; student_name: string; class_tag: string; age: number }[];
}) {
  const theme = useTheme({
    HeaderRow: `
      .th {
        font-weight: bold;
        border-bottom: 1px solid #a0a8ae;
      }
    `,
    Row: `
      cursor: pointer;
      .td {
        border-top: 1px solid #a0a8ae;
        border-bottom: 1px solid #a0a8ae;
      }
      &:hover .td {
        border-top: 1px solid var(--clr-yellow-900);
        border-bottom: 1px solid var(--clr-yellow-900);
      }
      &:not(:last-of-type) .td {
        border-bottom: 1px solid #a0a8ae;
      }
    `,
    BaseCell: `
      &:not(:last-of-type) {
        border-right: 1px solid #a0a8ae;
      }
      padding: 8px 16px;
    `,
  });

  const data = { nodes: props.data };
  const pagination = usePagination(data, {
    state: {
      page: 0,
      size: 10,
    },
  });
  const columns = [
    { label: "#", renderCell: (item) => item.id },
    {
      label: "Nome do Estudante",
      renderCell: (item) => item.student_name,
    },
    { label: "Turma", renderCell: (item) => item.class_tag },
    {
      label: "Idade",
      renderCell: (item) => item.age,
    },
  ];

  return (
    <div className="table-wrapper">
      <CompactTable
        columns={columns}
        data={data}
        theme={theme}
        pagination={pagination}
      />
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-around",
          padding: "10px",
        }}
      >
        <span>Total Pages: {pagination.state.getTotalPages(data.nodes)}</span>

        <span>
          Page:{" "}
          {pagination.state.getPages(data.nodes).map((_, index) => (
            <button
              key={index}
              type="button"
              style={{
                fontWeight: pagination.state.page === index ? "bold" : "normal",
              }}
              onClick={() => pagination.fns.onSetPage(index)}
            >
              {index + 1}
            </button>
          ))}
        </span>
      </div>
    </div>
  );
}

export default Table;
