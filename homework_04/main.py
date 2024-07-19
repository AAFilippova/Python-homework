"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""


import asyncio
from typing import List
from jsonplaceholder_requests import (
    fetch_user_data,
    fetch_post_data,
)
from models import (
    engine,
    session,
    Base,
    User,
    Post,
)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_user_from_site(users_data):
    async with session() as session:
        async with session.begin():
            for user in users_data:
                username = user['username']
                name = user['name']
                email = user['email']
                user = User(username=username, name=name, email=email)
                session.add(user)
            await session.commit()


async def add_post_from_site(posts_data):
    async with session() as session:
        async with session.begin():
            for post in posts_data:
                title = post['title']
                body = post['body']
                user_id = post['userId']
                post = Post(title=title, body=body, user_id=user_id)
                session.add(post)
            await session.commit()


async def async_main():
    await create_tables()

    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_user_data(),
        fetch_post_data(),
    )

    await add_user_from_site(users_data)
    await add_post_from_site(posts_data)
    await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
