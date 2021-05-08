from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def dashborad(request: Request):
    """
    ダッシュボードを表示する
    """
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.post("/stock")
def create_stock():
    """
    stockを作成し、DB登録する
    """
    return {
        "code": "success",
        "message": "stock created"
    }