from sqlalchemy.orm import Session

from .models import Tariff
from .schemas import TariffCreate


def create_tariff(db: Session, tariff: TariffCreate):
    db_tariff = Tariff(**tariff.dict())
    db.add(db_tariff)
    db.commit()
    db.refresh(db_tariff)
    return db_tariff


def get_rate_by_cargo_and_date(db: Session, cargo_type: str, date: str):
    return db.query(Tariff).filter(
        Tariff.cargo_type == cargo_type,
        Tariff.effective_date <= date
    ).order_by(Tariff.effective_date.desc()).first()
