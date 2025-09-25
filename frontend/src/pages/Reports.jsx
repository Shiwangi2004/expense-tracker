import React, { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, PieChart, Pie, Cell, Legend, ResponsiveContainer } from 'recharts';
import api from '../api/axios';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#A28CFF', '#FF6F91'];

function Reports() {
  const [monthly, setMonthly] = useState([]);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    api.get('/reports/monthly').then(res => setMonthly(res.data));
    api.get('/reports/categories').then(res => setCategories(res.data));
  }, []);

  return (
    <div className="reports-container">
      <h2>Reports</h2>
      <div className="chart-section">
        <h3>Monthly Expenses</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={monthly}>
            <XAxis dataKey="month" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="total" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div className="chart-section">
        <h3>Category Expenses</h3>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie data={categories} dataKey="total" nameKey="category" cx="50%" cy="50%" outerRadius={100} label>
              {categories.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default Reports;
