from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from fastapi import HTTPException
from typing import Optional

import api.models.sales as sales_model
import api.models.stocks as stocks_model
import api.schemas.sales as sales_schema

async def create_sale(db: AsyncSession, sale_body: sales_schema.SaleBase) -> sales_schema.SaleBase:
    # Find the stock by name
    result = await db.execute(select(stocks_model.Stock).where(stocks_model.Stock.name == sale_body.name))
    existing_stock = result.scalars().first()

    # Check if the stock exists
    if existing_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")

    # Decrease the amount of the stock
    existing_stock.amount -= sale_body.amount

    # Check if the stock has enough quantity
    if existing_stock.amount < 0:
        raise HTTPException(status_code=400, detail="Insufficient stock quantity. Could not process sale.")

    # Create a sale record
    sale = sales_model.Sale(
        stock_id=existing_stock.id,
        amount=sale_body.amount,
        price=sale_body.price,
        total_price=sale_body.price * sale_body.amount
    )

    # Add the stock and sale to the database
    db.add(existing_stock)
    db.add(sale)
    await db.commit()
    await db.refresh(existing_stock)
    await db.refresh(sale)

    return sales_schema.SaleBase(
        name=existing_stock.name,
        amount=sale.amount,
        price=sale.price,
        total_price=sale.total_price
    )

async def check_sale(db: AsyncSession) -> sales_schema.SaleCheck:
    result = await db.execute(select(func.sum(sales_model.Sale.total_price)))
    sum = result.scalar()
    return sales_schema.SaleCheck(sales=sum)