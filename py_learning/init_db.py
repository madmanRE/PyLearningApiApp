from database import engine, Base
from models.models import Author, Course, Module, Lesson, User, user_course, Admin

Base.metadata.create_all(bind=engine)
