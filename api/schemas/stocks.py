from typing import Optional
from pydantic import BaseModel, Field

class StockBase(BaseModel):
    name: str 
    amount: Optional[int] = Field(default=1)
