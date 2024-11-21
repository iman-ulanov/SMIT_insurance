from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from .models import Tariff
from .schemas import TariffCreate, TariffUpdate


def create_tariff(db: Session, tariff: TariffCreate):
    """
    Создать новый тариф.
    """
    db_tariff = Tariff(**tariff.dict())
    db.add(db_tariff)
    db.commit()
    db.refresh(db_tariff)
    return db_tariff


def get_rate_by_cargo_and_date(db: Session, cargo_type: str, date: str):
    """
    Получить актуальный тариф для указанного типа груза и даты.
    """
    return db.query(Tariff).filter(
        Tariff.cargo_type == cargo_type,
        Tariff.effective_date <= date
    ).order_by(Tariff.effective_date.desc()).first()


def update_tariff(db: Session, tariff_id: int, tariff_data: TariffUpdate):
    """
    Обновить существующий тариф по ID.
    """
    try:
        tariff = db.query(Tariff).filter(Tariff.id == tariff_id).one()
        for key, value in tariff_data.dict(exclude_unset=True).items():
            setattr(tariff, key, value)
        db.commit()
        db.refresh(tariff)
        return tariff
    except NoResultFound:
        return None


def delete_tariff(db: Session, tariff_id: int):
    """
    Удалить тариф по ID.
    """
    try:
        tariff = db.query(Tariff).filter(Tariff.id == tariff_id).one()
        db.delete(tariff)
        db.commit()
        return tariff
    except NoResultFound:
        return None


def get_tariff_by_id(db: Session, tariff_id: int):
    """
    Получить тариф по ID.
    """
    return db.query(Tariff).filter(Tariff.id == tariff_id).first()


def get_all_tariffs(db: Session):
    """
    Получить список всех тарифов.
    """
    return db.query(Tariff).all()
