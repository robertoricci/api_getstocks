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
    

    def postIndicatorHist(self, ticker: str):
        
        headers={
                'authority': 'statusinvest.com.br',
                'method': 'POST',
                'path': '/acao/indicatorhistoricallist',
                'scheme': 'https',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cookie': 'adasys=374e7bb3-8374-4c0a-a336-e81a42532aa2; _gcl_au=1.1.1048260460.1714067943; _fbp=fb.2.1714067943357.411340654; _ga=GA1.1.903527474.1714067944; hubspotutk=c8b28af7f2f1c4d455fb5ce8de0be650; suno_checkout_userid=7f07291c-ae52-4ae1-973d-e3a725de860c; _hjSessionUser_1931042=eyJpZCI6IjllMzMwMmQxLWI5ZGItNWE2Mi1hYmUzLTZjMWFjMjJiMjkyNiIsImNyZWF0ZWQiOjE3MTQwNjc5NDM0MDYsImV4aXN0aW5nIjp0cnVlfQ==; messagesUtk=da70c439dcf6458e9677b4484986a3a0; cf_clearance=tsYm3L.M_iZCvsL6A0tvQMgMBqoR0XE39Ft1SaBIZ6I-1715195625-1.0.1.1-nVJgzx5Mr83bNe7uE3ZqL5a7_VWMN_7Dp_qkk5YUX7Hst6MmPdNNadDFd_J1_Fu0HZMV9wm4hU8BmuEWJg8r5g; _cc_id=5a83c310b82d53beb95a8c35a0f9eeab; panoramaId_expiry=1717504242140; panoramaId=affaacc7cd78c5aca72575b2d3ef185ca02cf605a85799dbe49ea12ea74c6b87; panoramaIdType=panoDevice; _clck=f122j4%7C2%7Cfm7%7C0%7C1576; __hssrc=1; __hstc=176625274.c8b28af7f2f1c4d455fb5ce8de0be650.1714067950368.1717101477856.1717112482134.23; hs-messages-widget-position_right={"bottom":0,"horizontal":15}; _hjSession_1931042=eyJpZCI6ImY0NTE1YTJjLTQ1N2YtNDcxMy1iN2NhLWY2Mjc1ODJlODQyYyIsImMiOjE3MTcxMTI3NjIzMjUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; __gads=ID=daf6b6a16bca6a40:T=1714067965:RT=1717112802:S=ALNI_MaPqr3ICBVIf7gojU4SYbkoo77nZw; __gpi=UID=00000a21c858e651:T=1714067965:RT=1717112802:S=ALNI_MasU35Z6aszEhn-gKRt047a0PlbsQ; __eoi=ID=8f2f59c19ecd33e2:T=1714067965:RT=1717112802:S=AA-AfjZQVLM3E9VkdmKXvcKvBM-N; cf_clearance=SeLuFykXSZZKvA_5Fgd6LJx3umKYh6H0X3lFuCHI1UE-1717112899-1.0.1.1-C_XhDNvys7sn29GYa25Scwya2ts0H2kgK0FOlSGa0Qxl2lc9CrX_MnJgoYO5LhirVn4FYIXJNFmWjn0iXIuO8g; _clsk=1pv2hf6%7C1717113016090%7C6%7C0%7Ct.clarity.ms%2Fcollect; FCNEC=%5B%5B%22AKsRol9PJCJ2-pk0hYx0Jy56CGK1AViSFn-lzz_3qQQDY-O0w7e5IQkJEDIB849Q3hEuRc9rr2B_aevOc_jpYLqw2k-9lH2Hwwq1_mREUbuENdpVPkkfKdrYo50uizuWwmyGAR2upczmQaOpdDUs3nqXlsQE1nCXDg%3D%3D%22%5D%5D; _ga_69GS6KP6TJ=GS1.1.1717112474.24.1.1717113019.51.0.0; __hssc=176625274.5.1717112482134',
                'referer': 'https://statusinvest.com.br/acoes/bbse3',
                'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
                'x-requested-with': 'XMLHttpRequest'
        }
        
        url=f'https://statusinvest.com.br/acao/indicatorhistoricallist?codes={ticker}&time=7&futureData=false'
        
        dados = req.post(url,headers=headers).json()

        dados = dados['data']
   
        return dados