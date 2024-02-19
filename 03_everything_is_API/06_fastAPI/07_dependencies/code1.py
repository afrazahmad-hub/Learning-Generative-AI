from fastapi import FastAPI, Query, Depends
from typing import Annotated


app: FastAPI = FastAPI()

def user_login(username: str = Query(None), passward: str = Query(None)):
    if not username:
        raise

# if we will not add name, we will get exception "internal server error"
@app.get("/login", dependencies=[Depends(user_login)])
def get_user():
    return True