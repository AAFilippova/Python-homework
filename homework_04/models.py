"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from os import (
    getenv,
    environ,
)
from sqlalchemy import MetaData
from sqlalchemy import (
    String,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
    relationship,
)

PG_CONN_URI = environ.get(
    'SQLALCHEMY_PG_CONN_URI'
) or "postgresql+asyncpg://postgres:password@localhost:5432/postgres"
DB_ECHO = getenv("DB_ECHO", True)

engine = create_async_engine(
    url=PG_CONN_URI,
    echo=DB_ECHO,
)

session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autocommit=False,
)
class Base(DeclarativeBase):
    metadata = MetaData()

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"
    id: Mapped[int] = mapped_column(primary_key=True,unique=True, autoincrement=True, nullable=False)


class User(Base):
    username: Mapped[str] = mapped_column(String(38), unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column(default="", server_default="")

    posts: Mapped[list["Post"]] = relationship(back_populates="author")

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"email={self.email!r},"
            f"name={self.name!r}"
            ")"
        )


class Post(Base):
    title: Mapped[str] = mapped_column(String(100), unique=True)
    body: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    author: Mapped["User"] = relationship(back_populates="posts")

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"title={self.body!r}, "
            f"user_id={self.user_id!r}"
            ")"
        )
