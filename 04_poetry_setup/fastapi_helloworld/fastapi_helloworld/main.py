from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, world!"}

@app.get("/about")
def About():
    return {"message": "This is an about page"}