import { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { createItem, getItem, updateItem } from '../services/api';

const ItemForm = () => {
  const [formData, setFormData] = useState({ name: '', qty: '', rate: '' });
  const { id } = useParams(); // Automatically detects if there is an ID in the URL
  const navigate = useNavigate();

  // Load data only if we are in "Edit" mode (when ID is present)
  useEffect(() => {
    if (id) {
      getItem(id).then(res => setFormData(res.data));
    }
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (id) {
      await updateItem(id, formData); // Calls PUT
    } else {
      await createItem(formData); // Calls POST
    }
    navigate('/'); // Redirect back to Dashboard
  };

  return (
    <div style={{ maxWidth: '400px', margin: 'auto' }}>
      <h2>{id ? 'Edit Asset' : 'Add New Asset'}</h2>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        <input 
          type="text" placeholder="Item Name" required
          value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} 
        />
        <input 
          type="number" placeholder="Quantity" required
          value={formData.qty} onChange={e => setFormData({...formData, qty: e.target.value})} 
        />
        <input 
          type="number" placeholder="Rate" required
          value={formData.rate} onChange={e => setFormData({...formData, rate: e.target.value})} 
        />
        <button type="submit" style={{ padding: '10px', background: '#27ae60', color: 'white', border: 'none', cursor: 'pointer' }}>
          {id ? 'Update Asset' : 'Save Asset'}
        </button>
        <button type="button" onClick={() => navigate('/')} style={{ padding: '10px', background: '#000000', color: 'black', border: 'none', cursor: 'pointer' }}>
          Cancel
        </button>
      </form>
    </div>
  );
};

export default ItemForm;