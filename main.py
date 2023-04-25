from fastapi import FastAPI, HTTPException, Query
import requests
import json
import datetime

app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1, "syntaxHighlight.theme": "arta"})

@app.get("/task1/", tags=["tasks"])
def task1(code: str = "USD", date: str = str(datetime.date.today())):
    try:
        date_time = datetime.datetime.strptime(date, "%Y-%m-%d")    # checks if the date format is correct
        date = date_time.strftime("%Y-%m-%d")   # ensures dates without 2 digits provided for days and months will work
    except:
        raise HTTPException(status_code=500, detail="Date should follow YYYY-MM-DD")
    if(len(code)!=3):
         raise HTTPException(status_code=500, detail="Currency codes consist of three letters.")
    elif(date_time.weekday()==5 and date_time.weekday()==6):
        return
    else:
        req = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/?format=json")
        try:
            codes = json.dumps(req.json())
        except json.JSONDecodeError:
            codes = {}
        if("\"code\": \""+code+"\"" in codes):
            req = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/"+code+"/"+date+"/?format=json")
            try:
                dict = req.json()
            except:
                return
            list = dict.get('rates', {})
            mid = list[0]['mid']
            return mid
        else:
            raise HTTPException(status_code=500, detail="Provided wrong currency code.")
    
@app.get("/task2/", tags=["tasks"])
def task2(code: str = "USD", N: int = 255):
    if(len(code)!=3):
         raise HTTPException(status_code=500, detail="Currency codes consist of three letters.")
    elif(N>=0 and N<=255):
        if N==0:
            return
        req = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/?format=json")
        try:
            code_npb = json.dumps(req.json())
        except json.JSONDecodeError:
            code_npb = {}
        if("\"code\": \""+code+"\"" in code_npb):
            value = []
            minmax = []
            req = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/"+code+"/last/"+str(N)+"/?format=json")
            dict = req.json()
            list = dict.get('rates', {})
            for r in list:
                value.append(r['mid'])
            value.sort()
            minmax.append(value[0])
            minmax.append(value[N-1])
            return minmax
        else:
            raise HTTPException(status_code=500, detail="Provided wrong currency code.")
    else:
        raise HTTPException(status_code=500, detail="Quotations should be in range 0-255.")

@app.get("/task3/", tags=["tasks"])
def task3(code: str = "USD", N: int = 255):
    if(len(code)!=3):
         raise HTTPException(status_code=500, detail="Currency codes consist of three letters.")
    elif(N>=0 and N<=255):
        if N==0:
            return
        req = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/?format=json")
        try:
            code_npb = json.dumps(req.json())
        except json.JSONDecodeError:
            code_npb = {}
        if("\"code\": \""+code+"\"" in code_npb):
            value = []
            req = requests.get("http://api.nbp.pl/api/exchangerates/rates/C/"+code+"/last/"+str(N)+"/?format=json")
            dict = req.json()
            list = dict.get('rates', {})
            for r in list:
                value.append(r['ask']-r['bid'])
            value.sort()
            return value[N-1]
        else:
            raise HTTPException(status_code=500, detail="Provided wrong currency code.")
    else:
        raise HTTPException(status_code=500, detail="Quotations should be in range 0-255.")