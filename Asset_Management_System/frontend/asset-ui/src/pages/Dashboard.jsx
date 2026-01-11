import { useEffect, useState } from 'react';
import { getItems, deleteItem } from '../services/api';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
  const [items, setItems] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    // eslint-disable-next-line react-hooks/immutability
    loadItems();
  }, []);

  const loadItems = async () => {
    try {
      const res = await getItems();
      setItems(res.data);
    } catch (err) {
      console.error("Error fetching items", err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm("Delete this asset?")) {
      await deleteItem(id);
      loadItems();
    }
  };

  return (
    /* Use margin: auto and a max-width to center the content area */
    <div style={{ maxWidth: '900px', margin: '40px auto', textAlign: 'center' }}>
      <h2>Asset Inventory (item_master)</h2>
      
      {/* Table with margin: auto centers it horizontally */}
      <table border="1" cellPadding="10" style={{ width: '100%', borderCollapse: 'collapse', margin: '20px auto' }}>
        <thead>
          <tr style={{ background: '#f2f2f2' }}>
            <th>ID</th>
            <th>Name</th>
            <th>Qty</th>
            <th>Rate</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {items.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.name}</td>
              <td>{item.qty}</td>
              <td>{item.rate}</td>
              <td>
                <button onClick={() => navigate(`/edit/${item.id}`)} style={{ cursor: 'pointer' }}>Edit</button>
                <button onClick={() => handleDelete(item.id)} style={{ marginLeft: '10px', color: 'red', cursor: 'pointer' }}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Dashboard;