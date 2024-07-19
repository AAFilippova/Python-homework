"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import logging
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str, params: dict | None = None) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, ssl=False) as response:
            return await response.json()


async def fetch_user_data() -> dict:
    async with aiohttp.ClientSession() as session:
        res = await fetch_json(USERS_DATA_URL)
        return res


async def fetch_post_data() -> dict:
    async with aiohttp.ClientSession() as session:
        res = await fetch_json(POSTS_DATA_URL)
        return res

