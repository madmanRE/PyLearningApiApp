from fastapi import FastAPI, Request, HTTPException

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from sqladmin import Admin, ModelView
from database import engine
from models.models import Author, Course, Module, Lesson, User, user_course
from models.models import Admin as MyAdmin

from routers import auth_routers, author_routers, courses_routers, users_routers

from config import SUPERPASSWORD


app = FastAPI()
admin = Admin(app, engine)


class AuthorAdmin(ModelView, model=Author):
    column_list = [Author.id, Author.name, Author.email, Author.courses]
    name = "Author"
    name_plural = "Authors"
    icon = "fa-solid fa-check-circle"


class CourseAdmin(ModelView, model=Course):
    column_list = [Course.id, Course.title, Course.slug, Course.price, Course.is_active, Course.modules]
    name = "Course"
    name_plural = "Courses"
    icon = "fa-solid fa-book"


class ModuleAdmin(ModelView, model=Module):
    column_list = [Module.id, Module.title, Module.slug, Module.difficulty, Module.course_id, Module.lessons]
    name = "Module"
    name_plural = "Modules"
    icon = "fa-solid fa-folder-open"


class LessonAdmin(ModelView, model=Lesson):
    column_list = [Lesson.id, Lesson.title, Lesson.duration, Lesson.module_id]
    name = "Lesson"
    name_plural = "Lessons"
    icon = "fa-solid fa-graduation-cap"


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, ]
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class MyAdminAdmin(ModelView, model=MyAdmin):
    column_list = [MyAdmin.id, MyAdmin.name, ]
    name = "Admin"
    name_plural = "Admins"
    icon = "fa-solid fa-star"


admin.add_view(AuthorAdmin)
admin.add_view(CourseAdmin)
admin.add_view(ModuleAdmin)
admin.add_view(LessonAdmin)
admin.add_view(UserAdmin)
admin.add_view(MyAdminAdmin)

app.include_router(auth_routers.auth_router)
app.include_router(author_routers.author_router)
app.include_router(courses_routers.courses_router)
app.include_router(users_routers.users_router)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


async def secret_key_for_admin(key: str, request: Request):
    if request.url.path.startswith('/admin/'):
        if key != SUPERPASSWORD:
            raise HTTPException(status_code=403, detail="Forbidden")
    return request.url.path
