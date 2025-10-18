Credit to NeuralNine on YouTube
**"FastAPI Full Crash Course - Python’s Fastest Web Framework"**
https://www.youtube.com/watch?v=rvFsGRvj9jo&t=4s

# FastAPI Todo Application

## Overview
This repository provides a **basic FastAPI RESTful API** for managing a simple in-memory Todo list. It demonstrates CRUD (Create, Read, Update, Delete) operations, Pydantic model validation, and enum-based priority handling.

The application serves as a minimal example for learning FastAPI, API modeling with Pydantic, and endpoint structuring.

---


## Features
- **GET** `/todos` – Retrieve all todos or the first *N* todos.  
- **GET** `/todos/{todo_id}` – Retrieve a todo item by its unique ID.  
- **POST** `/todos` – Create a new todo entry.  
- **PUT** `/todos/{todo_id}` – Update an existing todo entry by ID.  
- **DELETE** `/todos/{todo_id}` – Remove a todo entry by ID.

## Installation and Setup

### 1. Prerequisites
Ensure the following are installed:
- **Python 3.9+**
- **pip** (Python package manager)
- (Optional for VS Code users) **Pylance** and **Python** extensions

### 2. Create a Virtual Environment
From your project directory:

```bash
python -m venv .venv

Each Todo item includes:
- `todo_id`: Unique integer identifier  
- `todo_name`: Task name (3–512 characters)  
- `todo_description`: Task description  
- `priority`: Task priority (`LOW`, `MEDIUM`, or `HIGH`)  

---

## API Models

### Priority (Enum)
```python
class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1
