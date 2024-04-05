from sqlalchemy import create_engine
from api.models.stocks import Base as StockBase
from api.models.sales import Base as SaleBase

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)

def reset_database():
    # Drop all tables
    StockBase.metadata.drop_all(engine)
    SaleBase.metadata.drop_all(engine)

    # Create all tables
    StockBase.metadata.create_all(engine)
    SaleBase.metadata.create_all(engine)

if __name__ == "__main__":
    reset_database()