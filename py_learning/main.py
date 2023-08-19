from fastapi import FastAPI
from routers import auth_routers, author_routers, courses_routers

app = FastAPI()

app.include_router(auth_routers.auth_router)
app.include_router(author_routers.author_router)
app.include_router(courses_routers.courses_router)

