from sqlalchemy import Column, Integer, String, Float, Date

from .database import Base


class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    cargo_type = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    effective_date = Column(Date, nullable=False)
