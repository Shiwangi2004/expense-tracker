import React, { useState } from 'react';

function ExpenseForm({ onAdd }) {
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');
  const [note, setNote] = useState('');
  const [date, setDate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onAdd({ amount: parseFloat(amount), category, note, date });
    setAmount('');
    setCategory('');
    setNote('');
    setDate('');
  };

  return (
    <form className="expense-form" onSubmit={handleSubmit}>
      <input type="number" step="0.01" placeholder="Amount" value={amount} onChange={e => setAmount(e.target.value)} required />
      <input type="text" placeholder="Category" value={category} onChange={e => setCategory(e.target.value)} required />
      <input type="text" placeholder="Note" value={note} onChange={e => setNote(e.target.value)} />
      <input type="date" value={date} onChange={e => setDate(e.target.value)} required />
      <button type="submit">Add Expense</button>
    </form>
  );
}

export default ExpenseForm;
