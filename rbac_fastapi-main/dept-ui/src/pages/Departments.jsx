import { useEffect, useState } from "react";
import api from "../api/api";
import { useAuth } from "../auth/AuthContext";

const Departments = () => {
  const { user } = useAuth();
  const [departments, setDepartments] = useState([]);
  const [name, setName] = useState("");

  const loadDepartments = async () => {
    const res = await api.get("/departments");
    setDepartments(res.data);
  };

  const createDepartment = async () => {
    await api.post("/departments", { name });
    setName("");
    loadDepartments();
  };

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadDepartments();
  }, []);

  return (
    <>
      <h2>Departments</h2>

      {user.role === "admin" && (
        <>
          <input
            placeholder="New Department"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <button onClick={createDepartment}>Add</button>
        </>
      )}

      <ul>
        {departments.map((d) => (
          <li key={d.id}>{d.name}</li>
        ))}
      </ul>
    </>
  );
};

export default Departments;