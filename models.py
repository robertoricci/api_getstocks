##from dotenv import load_dotenv
import os
from dotenv import load_dotenv 


from sqlalchemy import create_engine, Column, Integer, String,Text,DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get("DB_CONN")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Div(Base):
    __tablename__ = "dividendos"
    id = Column(Integer,primary_key=True)
    ticker = Column(String(10))
    json = Column(Text)
    data = Column(DateTime)
    
    
class Ticker(Base):
        __tablename__ = "ticker"
        id = Column(Integer,primary_key=True)
        ticker = Column(String(10))
        json = Column(Text)
        data = Column(DateTime)

Base.metadata.create_all(engine)