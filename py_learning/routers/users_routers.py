from werkzeug.security import generate_password_hash, check_password_hash
from fastapi import APIRouter, status, Depends, HTTPException, Request
from sqlalchemy.orm.exc import NoResultFound
from fastapi.encoders import jsonable_encoder
from sqlalchemy import update, delete

from database import SessionLocal, engine

from models import models
from schemas import schemas

from .make_order import create_payment

users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)

session = SessionLocal(bind=engine)


@users_router.get("/user/{user_id}/courses/")
async def get_my_courses(user_id: int):
    user_courses_list = session.query(models.user_course).filter(models.user_course.c.user_id == user_id).all()
    courses_id_list = [i.course_id for i in user_courses_list]

    result = session.query(models.Course).filter(models.Course.id.in_(courses_id_list)).all()

    if result:
        return jsonable_encoder(result)
    else:
        raise HTTPException(status_code=400, detail="Courses not found")


@users_router.get("/user/{user_id}/courses/passed/")
async def get_my_passed_courses(user_id: int):
    user_courses_list = session.query(models.user_course).filter(models.user_course.c.user_id == user_id).filter(
        models.user_course.c.is_passed == True).all()
    courses_id_list = [i.course_id for i in user_courses_list]

    result = session.query(models.Course).filter(models.Course.id.in_(courses_id_list)).all()

    if result:
        return jsonable_encoder(result)
    else:
        raise HTTPException(status_code=400, detail="Courses not found")


@users_router.post("/user/{user_id}/buy/")
async def buy_course(user_id: int, course_id: int):
    user_courses_list = session.query(models.user_course).filter(models.user_course.c.user_id == user_id).first()
    if user_courses_list is not None:
        raise HTTPException(status_code=402, detail="Course has been bought early")

    course = session.query(models.Course).filter(models.Course.id == course_id).first()

    # if course.price > 0:
    #     payment_result = create_payment(amount=course.price)
    #     client_secret = payment_result["client_secret"]
    #
    #     return {"message": "Payment required", "client_secret": client_secret}

    new_course = models.user_course.insert().values(
        user_id=user_id,
        course_id=course_id
    )

    session.execute(new_course)
    session.commit()

    return {"message": "Course has been bought successfully"}



@users_router.patch("/course/{course_id}/passed/")
async def pass_course(user_id: int, course_id: int):
    try:
        stmt = update(models.user_course).where(
            models.user_course.c.user_id == user_id,
            models.user_course.c.course_id == course_id
        ).values(is_passed=True)

        affected_rows = session.execute(stmt).rowcount
        session.commit()

        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Course not found")

        return {"message": "You passed course successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error '{e}'")


@users_router.delete("/course/delete/")
async def user_delete_course(user_id: int, course_id: int):
    try:
        stmt = delete(models.user_course).where(
            models.user_course.c.user_id == user_id,
            models.user_course.c.course_id == course_id
        )
        affected_rows = session.execute(stmt).rowcount
        session.commit()

        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Course not found")
        else:
            return {"message": "Course has been deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error '{e}'")


@users_router.delete("/self-delete/")
async def self_delete(user_id: int, email: str, password: str):
    user = session.query(models.User).filter(
        models.User.id == user_id
    ).filter(
        models.User.email == email
    ).first()

    if user:
        if check_password_hash(user.hashed_password, generate_password_hash(password)):
            session.delete(user)
            session.commit()
            return {"message": "User has been deleted"}
        else:
            raise HTTPException(status_code=403, detail="Have no permission")
    else:
        raise HTTPException(status_code=400, detail="No user found")
