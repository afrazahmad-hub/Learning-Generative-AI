from fastapi import FastAPI, Header

app: FastAPI = FastAPI()

@app.post("/agent")
def index(user_agent: str = Header()):
    print(user_agent)
    return {"user_agent": user_agent}