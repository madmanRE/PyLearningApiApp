from fastapi import APIRouter, status, Depends, HTTPException, Request
from sqlalchemy.orm.exc import NoResultFound
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine

from models import models
from schemas import schemas

courses_router = APIRouter(
    prefix='/courses',
    tags=['Courses'],
)

session = SessionLocal(bind=engine)


@courses_router.get("/")
async def get_all_courses():
    return jsonable_encoder(session.query(models.Course).all())


@courses_router.get("/{author_id}/")
async def get_all_courses_by_author(author_id: int):
    courses = session.query(models.Course).filter(models.Course.author_id == author_id).all()
    if courses:
        return jsonable_encoder(list(courses))
    else:
        raise HTTPException(status_code=400, detail="There are no courses here")


@courses_router.get("/detail/course/{course_id}/")
async def get_course_detail(course_id: int):
    try:
        course = session.query(models.Course).filter(models.Course.id == course_id).first()

        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        modules = session.query(models.Module).filter(models.Module.course_id == course.id).all()

        result = {"course": {
            "id": course.id,
            "title": course.title,
            "price": course.price,
        }, "modules": []}

        for module in modules:
            module_data = {
                "id": module.id,
                "title": module.title,
                "difficulty": module.difficulty,
                "lessons": []
            }

            lessons = session.query(models.Lesson).filter(models.Lesson.module_id == module.id).all()
            for lesson in lessons:
                lesson_data = {
                    "id": lesson.id,
                    "title": lesson.title,
                    "duration": lesson.duration,
                }
                module_data["lessons"].append(lesson_data)

            result["modules"].append(module_data)

        return jsonable_encoder(result)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Course not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")


@courses_router.get("/{course_id}/modules/")
async def get_all_modules(course_id: int):
    modules = session.query(models.Module).filter(models.Module.course_id == course_id).all()
    if modules:
        return jsonable_encoder(list(modules))
    else:
        raise HTTPException(status_code=400, detail="There are no modules here")


@courses_router.get("/detail/module/{module_id}/")
async def get_module_detail(module_id: int):
    try:
        module = session.query(models.Module).filter(models.Module.id == module_id).first()

        if not module:
            raise HTTPException(status_code=404, detail="Module not found")

        lessons = session.query(models.Lesson).filter(models.Lesson.module_id == module.id).all()

        result = {"module": {
            "id": module.id,
            "title": module.title,
            "difficulty": module.difficulty,
            "lessons": []
        }}

        for lesson in lessons:
            lesson_data = {
                "id": lesson.id,
                "title": lesson.title,
                "duration": lesson.duration,
            }
            result["module"]["lessons"].append(lesson_data)

        return jsonable_encoder(result)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Module not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")


@courses_router.get("/{module_id}/lessons")
async def get_all_lessons(module_id: int):
    lessons = session.query(models.Lesson).filter(models.Lesson.module_id == module_id).all()
    if lessons:
        return jsonable_encoder(list(lessons))
    else:
        raise HTTPException(status_code=400, detail="There are no lessons here")
