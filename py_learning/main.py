from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from routers import auth_routers, author_routers, courses_routers, users_routers, admin_routers

app = FastAPI()

app.include_router(auth_routers.auth_router)
app.include_router(author_routers.author_router)
app.include_router(courses_routers.courses_router)
app.include_router(users_routers.users_router)
app.include_router(admin_routers.admin_router)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

