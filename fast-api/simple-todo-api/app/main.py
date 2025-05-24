from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel

# Create a constant for the tasks
TASKS = [
    {'id': '1','title': 'Task One', 'description': 'Description One', 'priority': 'high'},
    {'id': '2','title': 'Task Two', 'description': 'Description Two', 'priority': 'medium'},
    {'id': '3','title': 'Task Three', 'description': 'Description Three', 'priority': 'low'},
    {'id': '4','title': 'Task Four', 'description': 'Description Four', 'priority': 'high'},
    {'id': '5','title': 'Task Five', 'description': 'Description Five', 'priority': 'medium'},
    {'id': '6','title': 'Task Six', 'description': 'Description Two', 'priority': 'low'}
]

# Create a FastAPI instance and set the router prefix
app = FastAPI()
# router = APIRouter(prefix="/api/v1/tasks")
# app.include_router(router)

class Task(BaseModel):
    id: str
    title: str
    description: str
    priority: str

# Create api endpoint
@app.get("/Tasks")
async def get_all_tasks() -> dict:
    if not TASKS:
        raise HTTPException(status_code=404, detail="No tasks found")
    return TASKS

@app.get("/Tasks/{task_id}")
async def get_task_by_id(task_id: str) -> dict:
    if not TASKS:
        raise HTTPException(status_code=404, detail="No tasks found")
    
    for task in TASKS:
        if task['id'] == task_id:
            return task
    
    raise HTTPException(status_code=404, detail="Task not found")

# #  Query params:
# @app.get("/Tasks/")
# async def get_tasks_by_priority(task_id: str, priority: str) -> dict:
#     tasks_by_priority = []
#     for task in TASKS:
#         if task_id == task['id'] and task['priority'].lower() == priority.lower():
#             tasks_by_priority.append(task)
#     return tasks_by_priority

@app.post("/Tasks/")
async def create_task(task: Task) -> dict:
    if not task:
        raise HTTPException(status_code=400, detail="Task not found")
    TASKS.append(task.model_dump())
    return task

@app.put("/Tasks/{task_id}")
async def update_task(task_id: str, task: Task) -> dict:
    if not task:
        raise HTTPException(status_code=400, detail="Task not found")
    for task in TASKS:
        if task['id'] == task_id:
            task['title'] = task.title
            task['description'] = task.description
            task['priority'] = task.priority
            return task    

@app.delete("/Tasks/{task_id}")
async def delete_task(task_id: str) -> dict:
    for task in TASKS:
        if task_id == task['id']:
            TASKS.remove(task)
            return task
    raise HTTPException(status_code=404, detail="Task not found")


