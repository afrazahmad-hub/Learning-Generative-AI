from fastapi import FastAPI, Depends
from typing import Annotated

# dummy database
development_db = ["DB for development"]

# function to return db
def get_db_session():
    return development_db

# fastapi instance
app: FastAPI = FastAPI()

@app.get("/add-items")
def add_item(item: str, db : Annotated[list, Depends(get_db_session)]):
    db.append(item)
    return {"item": item} # "All items in db": db