from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from fastapi import HTTPException
from typing import Optional, Dict
from sqlalchemy.engine import Result
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import api.models.stocks as stocks_model
import api.models.sales as sales_model
import api.schemas.stocks as stocks_schema

async def create_stock(db: AsyncSession, stocks_body: stocks_schema.StockBase) -> stocks_model.Stock:
    result = await db.execute(select(stocks_model.Stock).filter(stocks_model.Stock.name == stocks_body.name))
    existing_stock = result.scalars().first()

    if existing_stock:
        existing_stock.amount += stocks_body.amount
        db.add(existing_stock)
        await db.commit()
        await db.refresh(existing_stock)
    else:
        new_stock = stocks_model.Stock(**stocks_body.dict())
        db.add(new_stock)
        await db.commit()
        await db.refresh(new_stock)

    return stocks_body

async def check_stock(db: AsyncSession, product_name: Optional[str] = None) -> stocks_model.Stock or Dict[str, str]:
    if product_name:
        result = await db.execute(select(stocks_model.Stock).filter(stocks_model.Stock.name == product_name))
        stock = result.scalars().first()
        if not stock:
            raise HTTPException(status_code=404, detail="Product not found")

        return stock
    else:
        result = await db.execute(select(stocks_model.Stock).order_by(stocks_model.Stock.name))
        stocks = result.scalars().all()
        if not stocks:
            raise HTTPException(status_code=404, detail="No products found")
    
        return {stock.name: stock.amount for stock in stocks if stock.amount > 0}

async def delete_all(db: AsyncSession) -> Dict[str, str]:
    await db.execute(delete(sales_model.Sale))
    await db.execute(delete(stocks_model.Stock))
    await db.commit()

    return JSONResponse(
        status_code=200,
        content=jsonable_encoder({"message": "All stocks and sales have been deleted"})
    )
