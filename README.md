# micro_task_backend
 a structured learning path of backend with exercise 
>starter:=
Fast Api frame work
# task1== Quick_start
question:= 
implement app.py with:=
1. GET /health--> returns
    {"status":"ok"}
2. POST /items--> 
    accepts JSON {"name":str,"price":float} and return same object plus id:<int>(auto increment)
3. Add one test (use simple curl or httpie) 
  that shows posting one item and getting an id=1
----constraints----
  1. keep all in app.py
  2. dont use db use in-memory list
  3. no external libraries beyond FastAPI(uvicorn/pytest)
-------- resource------

read:= quick start, path, request body from documentation
resource:== https://fastapi.tiangolo.com/tutorial/first-steps/
outcome=:Backend fundamental--HTTP+FastAPI endpoints+local testing
-----------------------------------------------
#               task2
# ---------------------------------------------
...