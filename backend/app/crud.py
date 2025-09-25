from sqlalchemy.orm import Session
from sqlalchemy import and_, extract, func
from typing import Optional, List
from datetime import date
import app.models as models, app.schemas as schemas
from utils.password import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_expenses(
    db: Session,
    user_id: int,
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    skip: int = 0,
    limit: int = 10
):
    query = db.query(models.Expense).filter(models.Expense.owner_id == user_id)
    
    if category:
        query = query.filter(models.Expense.category == category)
    if start_date:
        query = query.filter(models.Expense.date >= start_date)
    if end_date:
        query = query.filter(models.Expense.date <= end_date)
    
    total = query.count()
    expenses = query.offset(skip).limit(limit).all()
    
    return expenses, total

def get_expense(db: Session, expense_id: int):
    return db.query(models.Expense).filter(models.Expense.id == expense_id).first()

def create_expense(db: Session, expense: schemas.ExpenseCreate, user_id: int):
    db_expense = models.Expense(**expense.dict(), owner_id=user_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def update_expense(db: Session, expense_id: int, expense: schemas.ExpenseUpdate):
    db_expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if db_expense:
        for key, value in expense.dict().items():
            setattr(db_expense, key, value)
        db.commit()
        db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int):
    db_expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if db_expense:
        db.delete(db_expense)
        db.commit()
    return db_expense

def get_monthly_report(db: Session, user_id: int):
    results = db.query(
        extract('year', models.Expense.date).label('year'),
        extract('month', models.Expense.date).label('month'),
        func.sum(models.Expense.amount).label('total')
    ).filter(models.Expense.owner_id == user_id).group_by(
        extract('year', models.Expense.date),
        extract('month', models.Expense.date)
    ).all()
    
    return [
        {
            "month": f"{int(r.year)}-{int(r.month):02d}",
            "total": float(r.total)
        }
        for r in results
    ]

def get_category_report(db: Session, user_id: int):
    results = db.query(
        models.Expense.category,
        func.sum(models.Expense.amount).label('total')
    ).filter(models.Expense.owner_id == user_id).group_by(
        models.Expense.category
    ).all()
    
    return [
        {
            "category": r.category,
            "total": float(r.total)
        }
        for r in results
    ]