from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..crud import get_rate_by_cargo_and_date
from ..database import get_db

router = APIRouter()


@router.get("/calculate/")
def calculate_insurance(cargo_type: str, declared_value: float, date: str, db: Session = Depends(get_db)):
    rate = get_rate_by_cargo_and_date(db, cargo_type, date)
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found for given cargo type and date")
    return {"insurance_cost": declared_value * rate.rate}
