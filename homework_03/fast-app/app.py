from fastapi import FastAPI
from views.articles import router as articles_router
from view import router as view_router
from views.authors import router as authors_router

app = FastAPI()
app.include_router(articles_router)
app.include_router(view_router)
app.include_router(authors_router)

@app.get("/", tags=["hello"])
def hello_root():
    return {
        "message": "Добро пожаловать в красивый и прекрасный мир бабочек ",
    }
