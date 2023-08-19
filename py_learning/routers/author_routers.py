from werkzeug.security import generate_password_hash, check_password_hash
from slugify import slugify

from fastapi import APIRouter, status, Depends, HTTPException, Request
from sqlalchemy.orm.exc import NoResultFound
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine

from models import models
from schemas import schemas

author_router = APIRouter(
    prefix='/author',
    tags=['Author'],
)

session = SessionLocal(bind=engine)


@author_router.post("/create/course/")
async def create_course(course: schemas.SchemaCourse):
    new_course = models.Course(
        title=course.title,
        slug=slugify(course.title),
        price=course.price,
        author_id=course.author_id,
    )

    session.add(new_course)
    session.commit()

    return {"message": f"Course {new_course.title} has been created"}


@author_router.patch("/update/course/{course_id}/")
async def update_course(course: schemas.SchemaCourse, course_id: int):
    course_for_update = session.query(models.Course).filter(models.Course.id == course_id).first()

    if course_for_update is not None:

        for key, value in course.dict().items():
            setattr(course_for_update, key, value)

        session.commit()

        return {"message": f"Course {course.title} has been updated"}

    else:
        raise HTTPException(status_code=400, detail="There are no Course with this ID")


@author_router.delete("/delete/course/")
async def delete_course(course_id: int):
    course_for_delete = session.query(models.Course).filter(models.Course.id == course_id).first()

    if course_for_delete is not None:

        session.delete(course_for_delete)
        session.commit()

        return {"message": f"Course {course_for_delete.title} has been deleted"}

    else:
        raise HTTPException(status_code=400, detail="There are no Course with this ID")


@author_router.post("/create/module/")
async def create_module(module: schemas.SchemaModule):
    new_module = models.Module(
        title=module.title,
        difficulty=module.difficulty,
        course_id=module.course_id,
    )

    session.add(new_module)
    session.commit()

    return {"message": f"Module {new_module.title} has been created"}


@author_router.patch("/update/module/{module_id}/")
async def update_module(module: schemas.SchemaModule, module_id: int):
    module_for_update = session.query(models.Module).filter(models.Module.id == module_id).first()

    if module_for_update is not None:
        for key, value in module.dict().items():
            setattr(module_for_update, key, value)

        session.commit()

        return {"message": f"Module {module.title} has been updated"}
    else:
        raise HTTPException(status_code=404, detail="Module not found")


@author_router.delete("/delete/module/")
async def delete_module(module_id: int):
    module_for_delete = session.query(models.Module).filter(models.Module.id == module_id).first()

    if module_for_delete is not None:
        session.delete(module_for_delete)
        session.commit()

        return {"message": f"Module {module_for_delete.title} has been deleted"}
    else:
        raise HTTPException(status_code=404, detail="Module not found")


@author_router.post("/create/lesson/")
async def create_lesson(lesson: schemas.SchemaLesson):
    new_lesson = models.Lesson(
        title=lesson.title,
        duration=lesson.duration,
        module_id=lesson.module_id,
    )

    session.add(new_lesson)
    session.commit()

    return {"message": f"Lesson {new_lesson.title} has been created"}


@author_router.patch("/update/lesson/{lesson_id}/")
async def update_lesson(lesson: schemas.SchemaLesson, lesson_id: int):
    lesson_for_update = session.query(models.Lesson).filter(models.Lesson.id == lesson_id).first()

    if lesson_for_update is not None:
        for key, value in lesson.dict().items():
            setattr(lesson_for_update, key, value)

        session.commit()

        return {"message": f"Lesson {lesson.title} has been updated"}
    else:
        raise HTTPException(status_code=404, detail="Lesson not found")


@author_router.delete("/delete/lesson/")
async def delete_lesson(lesson_id: int):
    lesson_for_delete = session.query(models.Lesson).filter(models.Lesson.id == lesson_id).first()

    if lesson_for_delete is not None:
        session.delete(lesson_for_delete)
        session.commit()

        return {"message": f"Lesson {lesson_for_delete.title} has been deleted"}
    else:
        raise HTTPException(status_code=404, detail="Lesson not found")
