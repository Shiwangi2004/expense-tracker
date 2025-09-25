# 💸 Expense Tracker App

A modern, full-stack Expense Tracker built with FastAPI (Python) and React (Vite). Track your expenses, visualize reports, and enjoy a clean, minimalist UI.

## 🚀 Features

**Backend (FastAPI)**
- 🔐 JWT Authentication (Signup/Login)
- 🗄️ SQLite Database (SQLAlchemy ORM)
- 📝 CRUD APIs for Expenses
- 📊 Monthly & Category Reports
- ⚡ Alembic Migrations
- 🧰 Swagger/OpenAPI Docs

**Frontend (React + Vite)**
- 🔑 Authentication (Signup/Login)
- 📋 Dashboard: List, filter, add expenses
- 📅 Pagination, category & date filters
- 📈 Reports: Monthly (bar chart), Category (pie chart)
- 🎨 Minimalist UI with Tailwind CSS
- 🧭 React Router Navigation
- 🔗 Axios for API calls (JWT interceptor)

## 🗂️ Project Structure
```
expense-tracker/
  backend/
    app/
      main.py
      models.py
      database.py
      schemas.py
      crud.py
    routers/
      auth.py
      expenses.py
      reports.py
    utils/
      security.py
      password.py
    alembic/
      ...
    requirements.txt
  frontend/
    src/
      api/
      pages/
      components/
      App.jsx
      main.jsx
    public/
    index.html
    package.json
    README.md
```

## 🛠️ Setup Instructions

### Backend
1. `cd backend`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `alembic upgrade head`
4. Start server: `uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. Install dependencies: `npm install`
3. Start dev server: `npm run dev`
4. Visit: [http://localhost:5173](http://localhost:5173)

## 📚 API Endpoints
- `POST /auth/signup` — Register user
- `POST /auth/token` — Login (JWT)
- `POST /expenses/` — Add expense
- `GET /expenses/` — List expenses
- `PUT /expenses/{id}` — Update expense
- `DELETE /expenses/{id}` — Delete expense
- `GET /reports/monthly` — Monthly totals
- `GET /reports/categories` — Category totals

## 🖥️ Demo
- Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- React UI: [http://localhost:5173](http://localhost:5173)

## ✨ Credits
- FastAPI, React, Vite, SQLAlchemy, Alembic, Tailwind CSS, Axios, Recharts

---


