from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from utils.security import get_current_user
import app.crud as crud, app.models as models, app.schemas as schemas

router = APIRouter()

@router.get("/monthly", response_model=List[schemas.MonthlyReport])
def get_monthly_report(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_monthly_report(db=db, user_id=current_user.id)

@router.get("/categories", response_model=List[schemas.CategoryReport])
def get_category_report(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_category_report(db=db, user_id=current_user.id)