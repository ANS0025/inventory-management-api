from typing import Optional
from pydantic import BaseModel, Field, condecimal

class SaleBase(BaseModel):
    name: str
    amount: Optional[int] = Field(default=1)
    price: Optional[float] = 0

class SaleCheck(BaseModel):
    sales: float = Field(gt=0)