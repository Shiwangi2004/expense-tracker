from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, List

# User schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True

# Expense schemas
class ExpenseBase(BaseModel):
    amount: float
    category: str
    note: Optional[str] = None
    date: date

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    owner_id: int
    
    class Config:
        from_attributes = True

class ExpenseList(BaseModel):
    expenses: List[Expense]
    total: int
    page: int
    limit: int
    total_pages: int

# Auth schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Report schemas
class MonthlyReport(BaseModel):
    month: str
    total: float

class CategoryReport(BaseModel):
    category: str
    total: float