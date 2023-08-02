import requests as req
#import json

class Dados():
    
    def getProventos(self, ticker: str):
        
        headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
                'cookie':'_adasys=a59700d9-e596-4129-bb8c-ec04c84575e9; _fbp=fb.2.1656684505268.248285651; pg_mm2_cookie_a=372f63cd-ae69-4141-a30c-4d4152f88651; __gads=ID=1824ad5ad75699ef:T=1656684512:S=ALNI_MZYZj8Nucckdwwr9Rn27RCVnD5Q_A; G_ENABLED_IDPS=google; hubspotutk=b20610f2fbf173331a796472eba46e13; _gcl_au=1.1.1058655456.1664461745; messagesUtk=104d02bc3f0647fead0755ad40f8d4df; .StatusInvest=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJBY2NvdW50SWQiOiI1MzE5OTUiLCJOYW1lIjoicm9iZXJ0byBjYXJsb3MgcmljY2kiLCJFbWFpbCI6InJvYmVydG8ucnJpY2NpQGdtYWlsLmNvbSIsIkludGVyZmFjZVR5cGUiOiJXZWIiLCJJcCI6Ijo6ZmZmZjoxMC4xMDAuMTAuMTM3IiwibmJmIjoxNjY5MzEzMTkwLCJleHAiOjE2NjkzOTk1OTAsImlhdCI6MTY2OTMxMzE5MCwiaXNzIjoiU3RhdHVzSW52ZXN0IiwiYXVkIjoiU3RhdHVzSW52ZXN0In0.N59D8eLBK0LO5KXXGp6kCkKRNRmtQOavzUFBEXLFdg1hSN1v0fY-mh5u2RtGIFKj9I8sUHkSxdSRvQrqV1wTGg; _ga=GA1.3.694036679.1656684505; _hjSessionUser_1931042=eyJpZCI6ImZiMzMxOTU1LWI2YTgtNTE0OC04ZDQwLWE5MWZkNzBhZWMxZCIsImNyZWF0ZWQiOjE2Njk4Mjk1MjA3MDMsImV4aXN0aW5nIjp0cnVlfQ==; _ga_69GS6KP6TJ=GS1.1.1669829520.9.1.1669829829.0.0.0; pg_beacon=1; __gpi=UID=0000073b6123a8e7:T=1656684512:RT=1670017640:S=ALNI_MbCTXjPIoCnHX1qO6kQpjBzVvUnEQ; FCNEC=[["AKsRol-zOGKE_cwH6l1_xCDdOIv-xFsnt1vSJXMzNNv-s7dATAYM3fyYV1q45dre99R-qA7KCvoWgzu2KxxTd0orXehZR9szLXpxjC4rASoO4QU-2v2htG3pfBcZ1Bmx8fZSOeAtznrHITNi89cCCpVK-mCtcs1cGw=="],null,[]]; _gid=GA1.3.1664468199.1671447617; .StatusAdThin=1; __hstc=176625274.b20610f2fbf173331a796472eba46e13.1657654904458.1671479311053.1671490655272.609; __hssrc=1; __hssc=176625274.13.1671490655272; _gat_UA-142136095-1=1; __cf_bm=F5hlE1nOSf8kEZpbrAAVUVyDTR1GMTiy1dY_fSbdg.Y-1671492723-0-Aaml8MPPrpNxXb3jrwUpyVrfW0nQzrkGGMMnvHr9nZwJzho5WksHD/QEuVrzdMEQnJPHpOrtKVJrQYl9ppQ793LmQdfG/rsOsqBHUGZK7LX3RxAflpNfPii/fo/Hsu+NDjRjCEzqKZk2E1Z3jF1FsJg=',   
                'referer': 'https://statusinvest.com.br/acoes/'+ticker+'',
                'x-requested-with':'XMLHttpRequest',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': "Windows",
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin'
        }
        
        url=f'https://statusinvest.com.br/acao/companytickerprovents?ticker={ticker}&chartProventsType=2'
        
        dados = req.get(url,headers=headers).json()
        ##dadosj = json.dumps(dados)
        return dados