import React, { useEffect, useState } from 'react';
import ExpenseList from '../components/ExpenseList';
import ExpenseForm from '../components/ExpenseForm';
import api from '../api/axios';

function Dashboard() {
  const [expenses, setExpenses] = useState([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [limit] = useState(10);
  const [category, setCategory] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const fetchExpenses = async () => {
    const params = {
      page,
      limit,
      category: category || undefined,
      start_date: startDate || undefined,
      end_date: endDate || undefined,
    };
    const res = await api.get('/expenses/', { params });
    setExpenses(res.data.expenses);
    setTotal(res.data.total);
  };

  useEffect(() => {
    fetchExpenses();
  }, [page, category, startDate, endDate]);

  const handleAddExpense = async (expense) => {
    await api.post('/expenses/', expense);
    fetchExpenses();
  };

  return (
    <div className="dashboard-container">
      <h2>Dashboard</h2>
      <ExpenseForm onAdd={handleAddExpense} />
      <div className="filters">
        <input type="text" placeholder="Category" value={category} onChange={e => setCategory(e.target.value)} />
        <input type="date" value={startDate} onChange={e => setStartDate(e.target.value)} />
        <input type="date" value={endDate} onChange={e => setEndDate(e.target.value)} />
      </div>
      <ExpenseList expenses={expenses} total={total} page={page} setPage={setPage} limit={limit} />
    </div>
  );
}

export default Dashboard;
