from typing import Optional
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from utils.security import get_current_user
import app.crud as crud, app.models as models, app.schemas as schemas
import math

router = APIRouter()

@router.post("/", response_model=schemas.Expense)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_expense(db=db, expense=expense, user_id=current_user.id)

@router.get("/", response_model=schemas.ExpenseList)
def read_expenses(
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    skip = (page - 1) * limit
    expenses, total = crud.get_expenses(
        db, current_user.id, category, start_date, end_date, skip, limit
    )
    total_pages = math.ceil(total / limit) if total > 0 else 1
    
    return schemas.ExpenseList(
        expenses=expenses,
        total=total,
        page=page,
        limit=limit,
        total_pages=total_pages
    )

@router.get("/{expense_id}", response_model=schemas.Expense)
def read_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_expense = crud.get_expense(db, expense_id=expense_id)
    if db_expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    if db_expense.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this expense")
    return db_expense

@router.put("/{expense_id}", response_model=schemas.Expense)
def update_expense(
    expense_id: int,
    expense: schemas.ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_expense = crud.get_expense(db, expense_id=expense_id)
    if db_expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    if db_expense.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this expense")
    
    return crud.update_expense(db=db, expense_id=expense_id, expense=expense)

@router.delete("/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_expense = crud.get_expense(db, expense_id=expense_id)
    if db_expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    if db_expense.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this expense")
    
    crud.delete_expense(db=db, expense_id=expense_id)
    return {"message": "Expense deleted successfully"}