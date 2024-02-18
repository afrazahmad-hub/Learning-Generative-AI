from fastapi import FastAPI, Body

app: FastAPI = FastAPI()

@app.post("id")
def index(name: str = Body(embed=True)):
    return {f"My name is {name}"}