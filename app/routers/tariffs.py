from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud import create_tariff
from ..database import get_db
from ..schemas import TariffCreate, TariffResponse

router = APIRouter()


@router.post("/tariffs/", response_model=TariffResponse)
def upload_tariff(tariff: TariffCreate, db: Session = Depends(get_db)):
    return create_tariff(db, tariff)
