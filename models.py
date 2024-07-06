##from dotenv import load_dotenv
import os
from dotenv import load_dotenv 


from sqlalchemy import create_engine, Column, Integer, String,Text,DateTime,Double
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get("DB_CONNF")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Div(Base):
    __tablename__ = "public.dividendos"
    id = Column(Integer,primary_key=True)
    ticker = Column(String(10))
    json = Column(Text)
    data = Column(DateTime)
     
class Ticker(Base):
        __tablename__ = "public.ticker"
        id = Column(Integer,primary_key=True)
        ticker = Column(String(10))
        json = Column(Text)
        data = Column(DateTime)

class Historico(Base):
        __tablename__ = "public.historico"
        id = Column(Integer,primary_key=True)
        ticker = Column(String(10))
        json = Column(Text)
        data = Column(DateTime)

class Ativos(Base):
    __tablename__ = "public.ativos"
    companyid = Column(Integer,primary_key=True)
    companyname = Column(Text)
    ticker = Column(Text)
    price  = Column(Double)
    p_l  = Column(Double)
    dy  = Column(Double)
    p_vp  = Column(Double)
    p_ebit  = Column(Double)
    p_ativo  = Column(Double)
    ev_ebit  = Column(Double)
    margembruta  = Column(Double)
    margemebit  = Column(Double)
    margemliquida  = Column(Double)
    p_sr  = Column(Double)
    p_capitalgiro  = Column(Double)
    p_ativocirculante  = Column(Double)
    giroativos  = Column(Double)
    roe  = Column(Double)
    roa  = Column(Double)
    roic  = Column(Double)
    dividaliquidapatrimonioliquido  = Column(Double)
    dividaliquidaebit  = Column(Double)
    pl_ativo  = Column(Double)
    passivo_ativo  = Column(Double)
    liquidezcorrente  = Column(Double)
    receitas_cagr5  = Column(Double)
    lucros_cagr5  = Column(Double)
    liquidezmediadiaria  = Column(Double)
    vpa  = Column(Double)
    lpa  = Column(Double)
    valormercado  = Column(Double)
    segmentid  = Column(Integer)
    sectorid  = Column(Integer)
    subsectorid  = Column(Integer)
    subsectorname  = Column(Text)
    segmentname  = Column(Text)
    sectorname  = Column(Text)
    data = Column(DateTime)

Base.metadata.create_all(engine)