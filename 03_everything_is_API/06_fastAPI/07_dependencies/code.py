from fastapi import FastAPI, Query, Depends
from typing import Annotated


app: FastAPI = FastAPI()

def user_login(username: str = Query(None), passward: str = Query(None)):
    if username == "admin" and passward == "admin":
        return {"message": "Login Success"}
    else:
        return {"message": "Login Failed"}
    
ann_dep = Annotated[dict, Depends(user_login)]

@app.get("/login")
def get_user(user: ann_dep):
    return user
