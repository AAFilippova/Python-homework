from typing import Annotated
from fastapi import APIRouter,HTTPException,status
from annotated_types import Ge, Lt

router = APIRouter(
    prefix="/articles",
    tags=["articles"],)



@router.get("/")
def get_articles():
    return {"articles":
        [
            {"id": 1,
             "title": "Удивительные бабочки",
             "content": "Удивительная история и природа самых красивых насекомых.",
             },
            {"id": 2,
             "title": "Жизненный цикл бабочки",
             "content": "Развития бабочки от яйца до взрослого насекомого.",
             },
            {"id": 3,
             "title": "Бабочки и их значение в природе",
             "content": "Роль бабочек в экосистеме и их важность для растений.",
             },
        ]
    }


@router.get("/{article_id}")
def get_article(article_id: Annotated[int, Ge(1),Lt(10_000)]):
    for article in get_articles()["articles"]:
        if article["id"] == article_id:
            return article
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Article #{article_id} not found",
    )

