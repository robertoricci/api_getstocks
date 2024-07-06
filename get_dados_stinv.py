import requests as req
#import json

class Dados():

    def montar_header(ticker):

        headers = {
                'authority': 'statusinvest.com.br',
                'method': 'POST',
                'path': '/acao/indicatorhistoricallist',
                'scheme': 'https',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cookie':'application/x-www-form-urlencoded; charset=UTF-8_adasys=374e7bb3-8374-4c0a-a336-e81a42532aa2; _gcl_au=1.1.1048260460.1714067943; _fbp=fb.2.1714067943357.411340654; _ga=GA1.1.903527474.1714067944; hubspotutk=c8b28af7f2f1c4d455fb5ce8de0be650; suno_checkout_userid=7f07291c-ae52-4ae1-973d-e3a725de860c; _hjSessionUser_1931042=eyJpZCI6IjllMzMwMmQxLWI5ZGItNWE2Mi1hYmUzLTZjMWFjMjJiMjkyNiIsImNyZWF0ZWQiOjE3MTQwNjc5NDM0MDYsImV4aXN0aW5nIjp0cnVlfQ==; messagesUtk=da70c439dcf6458e9677b4484986a3a0; _cc_id=5a83c310b82d53beb95a8c35a0f9eeab; G_ENABLED_IDPS=google; denakop_freq={}; panoramaId_expiry=1720713642630; panoramaId=cc8fcc20670066ce47c54a14d813185ca02c6ab293b8314a323f906c8ae48893; panoramaIdType=panoDevice; cf_clearance=lTMpxyvxqQOy_clwDQz_we37XU_HcIGiYlWL0h0rITg-1720210700-1.0.1.1-wEYC5tfCob_MPSD_niQS6_rNRUCB7v1lAEkIv.Py9myuOH1pRCIDi3UTGrNzJ8AYc2uX7oEOpdA0Lru5b1cfOA; .StatusAdThin=1; _clck=f122j4%7C2%7Cfn7%7C0%7C1576; _hjSession_1931042=eyJpZCI6IjFkNmYwZjVkLTAwMjYtNGZjNy04ZDEyLTk4ZGJkYzc2OTE3NCIsImMiOjE3MjAyMTA3MDA5NTIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __gads=ID=daf6b6a16bca6a40:T=1714067965:RT=1720210703:S=ALNI_MaPqr3ICBVIf7gojU4SYbkoo77nZw; __gpi=UID=00000a21c858e651:T=1714067965:RT=1720210703:S=ALNI_MasU35Z6aszEhn-gKRt047a0PlbsQ; __eoi=ID=8f2f59c19ecd33e2:T=1714067965:RT=1720210703:S=AA-AfjZQVLM3E9VkdmKXvcKvBM-N; __hstc=176625274.c8b28af7f2f1c4d455fb5ce8de0be650.1714067950368.1720108847612.1720210742636.40; __hssrc=1; _clsk=1qioep8%7C1720210758790%7C3%7C1%7Co.clarity.ms%2Fcollect; FCNEC=%5B%5B%22AKsRol-BCyF3DzZdshM6BW5k0-ifLoVluT1dFiWVuZIdbcop0EtnNqu_gM1O7KDcjjPz5A4Y_HKnqxMvndCxqj9lFsOalRoJe2gXT6azglhCUgQ6Gq7Ikq4_dedqOekZm7UZ9mf7qt3CtFWSauXt0Py2TnsyeYoqrg%3D%3D%22%5D%5D; __hssc=176625274.2.1720210742636; _ga_69GS6KP6TJ=GS1.1.1720210700.42.1.1720210800.21.0.0',
                'Origin':'https://statusinvest.com.br',
                'referer': 'https://statusinvest.com.br/acoes/'+ticker,
                'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
                'x-requested-with': 'XMLHttpRequest'
            }
        return headers
    
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
    

    def postIndicatorHist(self, ticker: str):
        
        headers = Dados.montar_header(ticker)
        
        url=f'https://statusinvest.com.br/acao/indicatorhistoricallist?codes={ticker}&time=5&futureData=false'
        
        resp = req.post(url,headers=headers)


        # parse json data
        json_data = resp.json()

        # return historical values for each indicator
        return {
            data["key"]: {
                rank_data["rank"]: rank_data["value"]
                for rank_data in data["ranks"]
                if "rank" in rank_data and "value" in rank_data
            }
            for data in list(json_data["data"].values())[0]
        }