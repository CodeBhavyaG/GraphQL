import sqlite3
import strawberry
from typing import List
from fastapi import FastAPI
from app.db import conn
from strawberry.fastapi import GraphQLRouter

app = FastAPI()
@strawberry.type
class Item:
    id: int
    name: str
    price: float

@strawberry.type
class Query:
    @strawberry.field
    def items(self) -> List[Item]:
        c = conn.cursor()
        c.execute('SELECT id, name, price FROM items')
        rows = c.fetchall()
        return [Item(id=row[0], name=row[1], price=row[2]) for row in rows]
    
    @strawberry.field
    def item(self, id: int) -> Item:
        c = conn.cursor()
        row = c.execute('SELECT id, name, price FROM items WHERE id = ?', (id,)).fetchone()
        return Item(id=row[0], name=row[1], price=row[2]) if row else None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, name: str, price: float) -> Item:
        c = conn.cursor()
        c.execute('INSERT INTO items (name, price) VALUES (?, ?)', (name, price))
        conn.commit()
        return Item(id=c.lastrowid, name=name, price=price)
    

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)


app.include_router(graphql_app, prefix="/graphql")