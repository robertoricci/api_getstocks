from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Div,Ticker, session,Ativos
from get_dados_stinv import Dados
from typing import Union

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



##http://localhost:8000/ativos/?ticker=a

@app.get("/ativos/")
async def get_ativos(ticker: str ):

    if ticker:
        return {'tickerx':ticker}
    else:
        return {'ticker':ticker}
    
    # ativo_query = session.query(Ativos)
    # ativo = ativo_query.filter(Ativos.ticker==ticker)
    
    # return ativo.first()
    
@app.get("/ticker/{ticker}")
async def get_div(ticker: str):
    
    tic = session.query(Ticker)
    
    return tic.all()

@app.get("/dividendos/{ticker}")
async def get_divid(ticker: str):
     
     dados = Dados()
     
     return dados.getProventos(ticker)

@app.post("/history/{ticker}")
async def post_hist(ticker: str):
     
     dados = Dados()
     
     return dados.postIndicatorHist(ticker)
     
     

###uvicorn app:app --reload
##https://fastapi.tiangolo.com/#example