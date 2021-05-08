from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def dashborad():
    return {"dashborad": "Home Page"}