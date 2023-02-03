
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_todo(todo_text, is_done=False):
    global todo_id
    todo ={ 
        "id": {todo_id},
        "todoText": {todo_text}, 
        "isDone": {is_done}
    }
    todo_id += 1
    return todo

todo_list = []

@app.post("/todos")
async def create_todo(request: Request):
    todo = await request.json()
    todo_list.append(todo)
    return todo

@app.get("/todos")
async def get_all_todos():
  return todo_list

@app.patch("/todos/{id}")
async def update_todo_by_id(id: int, request: Request):
    updated_todo = await request.json()
    for todo in todo_list:
        if todo["id"] == id:
            todo.update(updated_todo)
            return todo
    return {"error": "Todo not found"}, 404

@app.delete("/todos/{id}")
async def delete_todo_by_id(id: int):
    todo = [t for t in todo_list if t['id'] == id]
    if todo:
        todo_list.remove(todo[0])
        return {"message": "Todo successfully deleted."}
    else:
        return {"message": "Todo not found."}, 404