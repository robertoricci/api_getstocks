from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Div,Ticker, session
from get_dados_stinv import Dados

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/div/{ticker}")
async def get_div(ticker: str):
    
    div_query = session.query(Div)
    div = div_query.filter(Div.ticker==ticker)
    
    return div.first()
    
@app.get("/ticker/{ticker}")
async def get_div(ticker: str):
    
    tic = session.query(Ticker)
    
    return tic.all()

@app.get("/dividendos/{ticker}")
async def get_divid(ticker: str):
     
     dados = Dados()
     
     return dados.getProventos(ticker)
     

###uvicorn app:app --reload
##https://fastapi.tiangolo.com/#example