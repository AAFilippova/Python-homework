from fastapi import (
    APIRouter,
    status,
    HTTPException,
)

from views.authors.schemas import (
    AuthorRead,
    AuthorCreate,
    AuthorDelete,
)

from .crud import storage

router = APIRouter(prefix="/authors",tags=["author"],)


@router.get("/",response_model=list[AuthorRead],
)
def get_author_list():
    return storage.get()


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=AuthorRead,
)
def create_author(author_in: AuthorCreate,):
    return storage.create(author_in=author_in)

@router.delete("/{author_id}",status_code=status.HTTP_200_OK, response_model=AuthorDelete)
def delete_author(author_id: int):
    author = storage.get_by_id(author_id)
    if author:
        del storage.users[author_id]
        return {"author_id":author_id}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author_id #{author_id} not found",
    )
