from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from ..crud import create_tariff, update_tariff, delete_tariff, get_all_tariffs, get_tariff_by_id
from ..database import get_db
from ..schemas import TariffCreate, TariffUpdate, TariffResponse
from app.logger import log_to_kafka

router = APIRouter()

# Эндпоинт для добавления нового тарифа
@router.post("/tariffs/", response_model=TariffResponse)
def upload_tariff(tariff: TariffCreate, db: Session = Depends(get_db)):
    """
    Эндпоинт для добавления нового тарифа.
    """
    new_tariff = create_tariff(db, tariff)

    # Логирование в Kafka
    log_to_kafka(user_id=None, action=f"Created tariff {new_tariff.id}", event_time=datetime.now())
    return new_tariff


# Эндпоинт для обновления тарифа по ID
@router.put("/tariffs/{tariff_id}/", response_model=TariffResponse)
def update_tariff_endpoint(tariff_id: int, tariff_data: TariffUpdate, db: Session = Depends(get_db)):
    """
    Эндпоинт для обновления тарифа по ID.
    """
    tariff = update_tariff(db, tariff_id, tariff_data)
    if not tariff:
        raise HTTPException(status_code=404, detail="Tariff not found")

    # Логирование в Kafka
    log_to_kafka(user_id=None, action=f"Updated tariff {tariff_id}", event_time=datetime.now())
    return tariff


# Эндпоинт для удаления тарифа по ID
@router.delete("/tariffs/{tariff_id}/", response_model=dict)
def delete_tariff_endpoint(tariff_id: int, db: Session = Depends(get_db)):
    """
    Эндпоинт для удаления тарифа по ID.
    """
    tariff = delete_tariff(db, tariff_id)
    if not tariff:
        raise HTTPException(status_code=404, detail="Tariff not found")

    # Логирование в Kafka
    log_to_kafka(user_id=None, action=f"Deleted tariff {tariff_id}", event_time=datetime.now())
    return {"detail": "Tariff deleted successfully"}


# Эндпоинт для получения всех тарифов
@router.get("/tariffs/", response_model=List[TariffResponse])
def get_all_tariffs_endpoint(db: Session = Depends(get_db)):
    """
    Эндпоинт для получения всех тарифов.
    """
    tariffs = get_all_tariffs(db)
    return tariffs


# Эндпоинт для получения тарифа по ID
@router.get("/tariffs/{tariff_id}/", response_model=TariffResponse)
def get_tariff_by_id_endpoint(tariff_id: int, db: Session = Depends(get_db)):
    """
    Эндпоинт для получения тарифа по ID.
    """
    tariff = get_tariff_by_id(db, tariff_id)
    if not tariff:
        raise HTTPException(status_code=404, detail="Tariff not found")
    return tariff
