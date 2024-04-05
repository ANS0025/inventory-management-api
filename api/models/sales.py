from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from api.db import Base
from api.models.stocks import Stock

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey(Stock.id), index=True)
    amount = Column(Integer)
    price = Column(Numeric)
    total_price = Column(Numeric)