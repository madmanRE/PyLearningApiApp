from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, Table
from sqlalchemy.orm import relationship

from .database import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    author = Column(Boolean, default=True)

    courses = relationship("Course", back_populates="author")


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    slug = Column(String, index=True)
    description = Column(String, default="")
    price = Column(Numeric, default=0.00)
    is_active = Column(Boolean, default=False)
    is_passed = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="courses")

    modules = relationship("Module", back_populates="course")


class Module(Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    slug = Column(String, index=True)
    description = Column(String)
    difficulty = Column(Integer, default=1)
    is_active = Column(Boolean, default=False)
    is_passed = Column(Boolean, default=False)
    course_id = Column(Integer, ForeignKey("courses.id"))

    course = relationship("Course", back_populates="modules")

    lessons = relationship("Lesson", back_populates="module")


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    duration = Column(Integer)
    is_active = Column(Boolean, default=False)
    is_passed = Column(Boolean, default=False)
    module_id = Column(Integer, ForeignKey("modules.id"))

    module = relationship("Module", back_populates="lessons")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


user_course = Table('user_course', Base.metadate,
                    Column("user_id", ForeignKey("users.id"), primary_key=True),
                    Column("course_id", ForeignKey("courses.id"), primary_key=True),
                    )

