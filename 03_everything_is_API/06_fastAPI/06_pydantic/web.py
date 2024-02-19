from fastapi import FastAPI
from data import _family
from model import Ahmad_family

app: FastAPI = FastAPI()

@app.get("/family")
def get_family() -> list[Ahmad_family]:
    return _family


# Output
# [{"name":"Afraz Ahmad","age":34,"phone":32158,"education":"P.Graduate","currently_residing":"Islamabad","aka":"Afraz"},
#  {"name":"Fahad Ahmad","age":28,"phone":32177,"education":"Diploma","currently_residing":"France","aka":"Fahad"},
#  {"name":"Hammad Ahmad","age":22,"phone":31258,"education":"HSC","currently_residing":"Gujrat","aka":"Hammad"}]