# Expense Tracker Frontend

This is the React (Vite) frontend for the Expense Tracker app.

## Features
- User authentication (signup, login, JWT)
- Dashboard: list, filter, add expenses
- Reports: monthly and category charts
- Clean UI with navigation and conditional rendering

## Setup Instructions

1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the frontend:
   ```bash
   npm run dev
   ```
3. The app runs at `http://localhost:5173` (default Vite port).

## Backend Setup
- Make sure the FastAPI backend is running at `http://127.0.0.1:8000`
- See backend README for details

## Tech Stack
- React (Vite)
- Axios
- React Router DOM
- Recharts

## Folder Structure
```
frontend/
  src/
    api/
      axios.js
    pages/
      Login.jsx
      Signup.jsx
      Dashboard.jsx
      Reports.jsx
    components/
      ExpenseForm.jsx
      ExpenseList.jsx
    App.jsx
    main.jsx
```
