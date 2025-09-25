import React from 'react';

function ExpenseList({ expenses, total, page, setPage, limit }) {
  const totalPages = Math.ceil(total / limit) || 1;

  return (
    <div className="expense-list">
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Amount</th>
            <th>Category</th>
            <th>Note</th>
          </tr>
        </thead>
        <tbody>
          {expenses.map(exp => (
            <tr key={exp.id}>
              <td>{exp.date}</td>
              <td>{exp.amount}</td>
              <td>{exp.category}</td>
              <td>{exp.note}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="pagination">
        <button onClick={() => setPage(page - 1)} disabled={page <= 1}>Prev</button>
        <span>Page {page} of {totalPages}</span>
        <button onClick={() => setPage(page + 1)} disabled={page >= totalPages}>Next</button>
      </div>
    </div>
  );
}

export default ExpenseList;
