from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()
tasks = []
next_task_id = 1
class TaskCreate(BaseModel):
    title: str

@app.get("/")
def home():
    return {"message": "我学会了第一个 API"}

@app.post("/tasks")
def create_task(task: TaskCreate):
    global next_task_id
    task_data = {
        "id": next_task_id,
        "title": task.title
    }
    tasks.append(task_data)
    next_task_id += 1
    return task_data

@app.get("/tasks")
def get_tasks(limit: int = Query(default=10, ge=1)):
    return tasks[:limit]

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskCreate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_data.title
            return task
    raise HTTPException(status_code=404, detail="Task not found")