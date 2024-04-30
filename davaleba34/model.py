from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker

HOST = 'localhost'
PORT = 5432
DATABASE = 'products'
USER = 'postgres'
PASSWORD = 'nat2nat'

engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'

    product_id = Column("product_id", Integer, primary_key=True, autoincrement=True)
    product_name = Column("product_name", String(40))
    product_price = Column("product_price", Float)
    stock_quantity = Column("stock_quantity", Integer)
    category_id = Column("category_id", Integer, ForeignKey('categories.category_id'))


class Categories(Base):
    __tablename__ = 'categories'

    category_id = Column("category_id", Integer, primary_key=True, autoincrement=True)
    category_name = Column("category_name", String(40))


class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column("order_id", Integer, primary_key=True, autoincrement=True)
    product_id = Column("product_id", Integer, ForeignKey('products.product_id'))
    quantity = Column("quantity", Integer)
    order_date = Column("order_date", DateTime)
    status = Column("status", String(20))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
