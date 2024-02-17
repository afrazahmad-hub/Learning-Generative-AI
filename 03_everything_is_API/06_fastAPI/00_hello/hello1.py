from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/")
def index() -> dict:
    return {"message" : "Hello World in File"}

# this condition to check the run of file
# we can up the server from the orignal file
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello1:app", reload=True, port=8000)