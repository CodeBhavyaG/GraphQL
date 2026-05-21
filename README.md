# GraphQL FastAPI Example

A minimal GraphQL API built with FastAPI, Strawberry, and SQLite. This project demonstrates a simple `Item` type with queries and a mutation to create items — useful for learning GraphQL + Python or for a quick demo.

## Features
- GraphQL endpoint powered by Strawberry and FastAPI
- SQLite persistence (`item.db`)
- Example queries: list items, fetch single item
- Mutation to create new items
- Very small, easy-to-read codebase

## Repository Files
- `main.py` — app entrypoint (runs uvicorn)
- `app/app.py` — FastAPI app, Strawberry schema, GraphQL router
- `app/db.py` — SQLite connection and initial seed data
- `requirments.txt` — list of dependencies
- `item.db` — SQLite database file (created at runtime)

## Requirements
- Python 3.8+
- Install dependencies from `requirments.txt`

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirments.txt
