from enum import IntEnum
from typing import List, Optional


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description='Name of the todo')
    todo_description: str = Field(..., description='description of the todo')
    priority: Priority = Field(default=Priority.LOW, description='Priority of the todo')

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description='Unique identifier of the todo')

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description='Name of the todo')
    todo_description: Optional[str] = Field(None, description='description of the todo')
    priority: Optional[Priority] = Field(None, description='Priority of the todo')

all_todos = [
    Todo(todo_id=1, todo_name='Sports', todo_description='Go to the gym', priority=Priority.HIGH),
    Todo(todo_id=2, todo_name='Read', todo_description='Read 10 pages', priority=Priority.MEDIUM),
    Todo(todo_id=3, todo_name='Shop', todo_description='Go Shopping', priority=Priority.LOW),
    Todo(todo_id=4, todo_name='Study', todo_description='Study for exam', priority=Priority.MEDIUM),
    Todo(todo_id=5, todo_name='Meditate', todo_description='Meditate for 20 minutes', priority=Priority.LOW)
]

# GET, POST, PUT, DELETE

# Query example
# Open server with:
# fastapi dev main.py --port 9999
# Then type into browser: 127.0.0.1:9999/todos/1
# or 127.0.0.1:9999/todos?first_n=1 (number) to index through list
@api.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
        
    raise HTTPException(status_code=404, detail='Todo not found')


@api.get('/todos', response_model=List[Todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    

# post example
@api.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max((todo.todo_id for todo in all_todos), default=0) + 1

    new_todo = Todo(todo_id = new_todo_id,
                    todo_name = todo.todo_name,
                    todo_description = todo.todo_description,
                    priority = todo.priority)
    
    all_todos.append(new_todo)

    return new_todo

# Put example
@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')


# Delete example
@api.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail='Todo not found')

# @api.get('/calculation')
# def calculation():
#     pass
#     return ""

# @api.get('/getdata')
# def get_data_from_db():
#     # await results
#     pass
#     return
