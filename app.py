#1 start server 
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
class Item(BaseModel):
    name:str
    price:float
# create app
app=FastAPI() # FastAPI object 
# home check:=
@app.get('/')
def home():
    return 'server started\n'
# micro task::=
#1. GET /health--> returns
    #{"status":"ok"}
@app.get('/health')
def health():
    return {"status":"ok"}

#2. POST /items--> 
#    accepts JSON {"name":str,"price":float} and 
#return same object plus id:<int>(auto increment)

## concept ki baat
## playload: type of input handle inputed data
# 
#-----XXXX---
item_list=[]
id_track=1
@app.post('/items')
def items(playload:Item):
    global id_track
    global item_list
    
    d={"id":id_track,
       "name":playload.name,
       "price":playload.price
    }
    id_track+=1

    item_list.append(d)
    return d
@app.get('/lis')
def bill():
    global item_list
    return item_list 
    
# app run
uvicorn.run(app)

