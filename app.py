#1 start server 
from fastapi import FastAPI
import uvicorn

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
global id 
id=1
#2. POST /items--> 
#    accepts JSON {"name":str,"price":float} and 
#return same object plus id:<int>(auto increment)
@app.post('/items')
def items():





# app run
uvicorn.run(app)

