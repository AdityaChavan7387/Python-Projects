import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";
import { useAuth } from "../auth/AuthContext";

const Register = () => {
  const [form, setForm] = useState({
    username: "",
    password: "",
    role: "user",
  });

  const { login } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async () => {
    const res = await api.post("/auth/register", form);
    login(res.data.user, res.data.access_token);
    navigate("/departments");
  };

  return (
    <>
      <h2>Register</h2>

      <input name="username" onChange={handleChange} placeholder="Username" />
      <input
        type="password"
        name="password"
        onChange={handleChange}
        placeholder="Password"
      />

      <select name="role" onChange={handleChange}>
        <option value="user">User</option>
        <option value="admin">Admin</option>
      </select>

      <button onClick={handleSubmit}>Register</button>
    </>
  );
};

export default Register;