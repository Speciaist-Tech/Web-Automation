# Todo Client

A small Python class that wraps a public test API
([jsonplaceholder](https://jsonplaceholder.typicode.com)) using `httpx`.

## Features
- `get_todo`, `list_todos` and `create_post` methods
- Error handling that catches failures and returns `None` instead of crashing

## How to run
```
pip install httpx
python todo_client.py
```

## Example
```python
api = TodoClient()
print(api.get_todo(1))
api.close()
```

## About this project
I'm learning web automation, and the projects in this repo are my practice
runs. This is Stage 1 of a larger project (a test runner and an async
version are next). I learned how GET and POST requests work and how to handle
failures, and I'm still practicing query parameters.
Feedback on my code, including anything redundant, is very welcome.
