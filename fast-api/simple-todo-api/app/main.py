from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

TASKS = [
    {'id': '1','title': 'Task One', 'description': 'Description One', 'priority': 'high'},
    {'id': '2','title': 'Task Two', 'description': 'Description Two', 'priority': 'medium'},
    {'id': '3','title': 'Task Three', 'description': 'Description Three', 'priority': 'low'},
    {'id': '4','title': 'Task Four', 'description': 'Description Four', 'priority': 'high'},
    {'id': '5','title': 'Task Five', 'description': 'Description Five', 'priority': 'medium'},
    {'id': '6','title': 'Task Six', 'description': 'Description Two', 'priority': 'low'}
]

class Task(BaseModel):
    id: str
    title: str
    description: str
    priority: str

app = FastAPI()

@app.get("/")
async def get_all_tasks() -> dict:
    return {"Tasks": TASKS}

@app.get("/{task_id}")
async def get_task_by_id(task_id: str) -> dict:
    for task in TASKS:
        if task['id'] == task_id:
            print(task)
            return {"Tasks": task}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/")
async def create_task(task: Task) -> dict:
    if(task.id in TASKS):
        raise HTTPException(status_code=400, detail="Task already exists")
    TASKS.append(task)
    return {"Tasks": TASKS}

@app.put("/{task_id}")
async def update_task(task_id: str, updated_task: Task) -> dict:
    for task in TASKS:
        if task['id'] == task_id:            
            task['title'] = updated_task.title
            task['description'] = updated_task.description
            task['priority'] = updated_task.priority
            return {"Task": task}
    raise HTTPException(status_code=404, detail="Task not found")
    
@app.delete("/{task_id}")
async def delete_task(task_id: str) -> dict:
    for task in TASKS:
        if task['id'] == task_id:
            TASKS.remove(task)
            return {"Tasks": TASKS}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

