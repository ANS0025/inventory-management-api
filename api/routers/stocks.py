from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
from typing import Optional, Any

import api.cruds.stocks as stocks_crud
import api.schemas.stocks as stocks_schema

router = APIRouter(
    prefix="/v1/stocks"
)

@router.post("", response_model=stocks_schema.StockBase)
async def create_stock(
    stock_body: stocks_schema.StockBase, db: AsyncSession = Depends(get_db)
):
    return await stocks_crud.create_stock(db, stock_body)

@router.get("", response_model=Any)
async def check_stock(
     product_name: Optional[str] = None, db: AsyncSession = Depends(get_db)
):
    return await stocks_crud.check_stock(db, product_name)

@router.delete("", response_model=None)
async def delete_all(
    db: AsyncSession = Depends(get_db)
):
    return await stocks_crud.delete_all(db)