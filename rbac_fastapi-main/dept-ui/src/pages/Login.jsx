import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";
import { useAuth } from "../auth/AuthContext";

const Login = () => {
  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const { login } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async () => {
    const res = await api.post("/auth/login", form);
    login(res.data.user, res.data.access_token);
    navigate("/departments");
  };

  return (
    <>
      <h2>Login</h2>

      <input name="username" onChange={handleChange} placeholder="Username" />
      <input
        type="password"
        name="password"
        onChange={handleChange}
        placeholder="Password"
      />

      <button onClick={handleSubmit}>Login</button>
    </>
  );
};

export default Login;