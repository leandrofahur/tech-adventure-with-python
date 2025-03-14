from fastapi import FastAPI
app = FastAPI()

TODOS = [
  {
    "id": 1,
    "description": "Buy groceries",
    "completed": False
  },
  {
    "id": 2,
    "description": "Walk the dog",
    "completed": False
  },
  {
    "id": 3,
    "description": "Pet the cat",
    "completed": False
  }
]


@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API. Use /docs to see the API documentation and /redoc to see the API documentation in a different format."}

@app.get("/todos")
async def get_all_todos():
  return {    
    "todos": TODOS
  }
  
@app.get("/todos/{todo_id}")
async def get_todo_by_id(todo_id: int):
  for todo in TODOS:
    if(todo["id"] == todo_id):
      return {        
        "todo": todo
      }    
    



