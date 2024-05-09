from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Message" : "Hello World"}

@app.get("/about")
def about():
    return {"Message" : "About Page"}