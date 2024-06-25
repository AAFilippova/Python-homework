import uuid

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
)

AuthorIdType = int


class AuthorBase(BaseModel):
    username: str
    firstname: str
    lastname: str
    middlename: str
    email: EmailStr



class AuthorRead(AuthorBase):
    id: AuthorIdType = Field(
        ...,
        description="The id of the author",
        example=123,
    )


class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: AuthorIdType

class AuthorDelete(BaseModel):
    author_id: int