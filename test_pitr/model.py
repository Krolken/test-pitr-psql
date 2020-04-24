from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .base import Base


class TestData(Base):
    __tablename__ = 'testdata'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String,)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
