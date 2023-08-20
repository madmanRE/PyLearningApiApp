from fastapi import APIRouter, status, Depends, HTTPException, Request
from database import SessionLocal, engine

from models import models
from schemas import schemas

from config import SUPERPASSWORD

admin_router = APIRouter(
    prefix='/admin',
    tags=['Admin'],
)

session = SessionLocal(bind=engine)


@admin_router.delete("/del/course/")
async def delete_course(course_id: int, superpassword: str):
    if superpassword == SUPERPASSWORD:
        course = session.query(models.Course).filter(models.Course.id == course_id).first()
        session.detele(course)
        session.commit()
        return {"message": "Course has been deleted"}
    else:
        raise HTTPException(status_code=403, detail="Have no permission")


@admin_router.delete("/del/user/")
async def delete_user(user_id: int, superpassword: str):
    if superpassword == SUPERPASSWORD:
        user = session.query(models.User).filter(models.User.id == user_id).first()
        session.detele(user)
        session.commit()
        return {"message": "User has been deleted"}
    else:
        raise HTTPException(status_code=403, detail="Have no permission")


@admin_router.delete("/del/author/")
async def delete_user(author_id: int, superpassword: str):
    if superpassword == SUPERPASSWORD:
        author = session.query(models.Author).filter(models.Author.id == author_id).first()
        session.detele(author)
        session.commit()
        return {"message": "Author has been deleted"}
    else:
        raise HTTPException(status_code=403, detail="Have no permission")
