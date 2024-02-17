from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/hi")
def say_hi() -> dict:
    return {"message": "Say Hi to World"}

# pass arguments in url
@app.get("/in/{pname}")
def profile(pname: str) -> dict:
    return {"Message" : f"Hi {pname}"}

# passing multiple arguments
@app.get("/{city}/loc/{pname}")
def address(city : str, pname: str) -> dict:
    return {"Address" : f"City Name: {city}. Name: {pname}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello_arg:app", port=8000, reload=True)