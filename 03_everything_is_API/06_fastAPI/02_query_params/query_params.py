from fastapi import FastAPI

app: FastAPI = FastAPI()

# we can add string parameters by adding ? after the url (key value pairs)
@app.get("/notifications")
def get_notifications(filter : str) -> dict:
    return {"message": f"Notifications for {filter}"}


