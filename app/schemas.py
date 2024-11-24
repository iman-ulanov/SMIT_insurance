from datetime import date

from pydantic import BaseModel


class TariffCreate(BaseModel):
    cargo_type: str
    rate: float
    effective_date: date


class TariffUpdate(BaseModel):
    rate: float


class TariffResponse(BaseModel):
    id: int
    cargo_type: str
    rate: float
    effective_date: date

    class Config:
        orm_mode = True


class TariffOut(TariffResponse):
    # Можно добавить дополнительные поля, если нужно
    pass
