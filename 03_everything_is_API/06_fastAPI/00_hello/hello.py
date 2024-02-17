from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/")
def index() -> dict:
    return {"message": "Hello World !"}