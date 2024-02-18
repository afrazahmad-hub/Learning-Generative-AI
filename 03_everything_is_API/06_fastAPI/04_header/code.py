from fastapi import FastAPI, Header

app: FastAPI = FastAPI()

# use following command to shoe hader details
# http -v localhost:8000/who who:Afraz
@app.post("/who")
def index(who: str = Header()):
    return f'Hello {who}'