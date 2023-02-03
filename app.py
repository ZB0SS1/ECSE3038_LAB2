from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app/",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database = []

@app.get("/todos")
async def get_all_todos():
  return database

@app.post("/todos")
async def create_todo(request: Request):
  todo = await request.json()
  database.append(todo)
  return todo


