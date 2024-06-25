"""
Create
Read
Update
Delete
"""

from pydantic import BaseModel

from .schemas import (
    Author,
    AuthorCreate,
    AuthorIdType,
)


class AuthorStorage(BaseModel):
    users: dict[AuthorIdType, Author] = {}
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create(self, user_in: AuthorCreate) -> Author:
        user = Author(
            id=self.next_id,
            **user_in.model_dump(),
        )
        self.users[user.id] = user
        return user

    def get(self) -> list[Author]:
        return list(self.users.values())

    def get_by_id(self, author_id: AuthorIdType) -> Author | None:
        return self.users.get(author_id)


storage = AuthorStorage()
storage.create(
    AuthorCreate(
        username="ivan300",
        firstname="Иван",
        lastname="Иванов",
        middlename="Иванович",
        email="ivan300@ya.com",
    ),
)
storage.create(
    AuthorCreate(
        username="coolann",
        firstname="Анна",
        lastname="Сергеева",
        middlename="Петровна",
        email="coolann@ya.com",
    ),
)
