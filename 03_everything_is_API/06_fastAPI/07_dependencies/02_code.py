from fastapi import FastAPI, Query, Depends
from typing import Annotated


app: FastAPI = FastAPI()

# if we will not add name, we will get exception "internal server error"
def user_login(username: str = Query(None), passward: str = Query(None)):
    if not username:
        raise

# when the function do not have to return a value, 
# in this ccase user_login not returning the value,
# We can pass the depend as query parameters, as following.
@app.get("/login", dependencies=[Depends(user_login)])
def get_user():
    return True