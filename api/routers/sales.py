from fastapi import APIRouter, Depends
from typing import Optional
from api.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.sales as sales_schema
import api.cruds.sales as sales_crud

router = APIRouter(
    prefix="/v1/sales"
)

@router.post("/", response_model=sales_schema.SaleBase)
async def create_sale(
    sale_body: sales_schema.SaleBase, db: AsyncSession = Depends(get_db)
):
    return await sales_crud.create_sale(db, sale_body)

@router.get("/", response_model=sales_schema.SaleCheck)
async def check_sale(
    db: AsyncSession = Depends(get_db)
):
    return await sales_crud.check_sale(db)
