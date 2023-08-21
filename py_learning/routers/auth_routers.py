from werkzeug.security import generate_password_hash, check_password_hash

from fastapi import APIRouter, status, Depends, HTTPException, Request
from database import SessionLocal, engine

from models import models
from schemas import schemas

from config import SUPERPASSWORD

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)

session = SessionLocal(bind=engine)


@auth_router.post("/signup/authors/")
async def create_author(user: schemas.PersonBase):
    user_email = session.query(models.Author).filter(models.Author.email == user.email).first()

    if user_email is not None:
        raise HTTPException(status_code=400, detail="Invalid data (email is not unique)")

    new_author = models.Author(
        name=user.name,
        email=user.email,
        hashed_password=generate_password_hash(user.password)
    )

    session.add(new_author)
    session.commit()

    return {"message": f"New author {new_author.name} has been created successfully"}


@auth_router.post("/signup/users/")
async def create_user(user: schemas.PersonBase):
    user_email = session.query(models.User).filter(models.User.email == user.email).first()

    if user_email is not None:
        raise HTTPException(status_code=400, detail="Invalid data (email is not unique)")

    new_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=generate_password_hash(user.password)
    )

    session.add(new_user)
    session.commit()

    return {"message": f"New user {new_user.name} has been created successfully"}


@auth_router.post("/signup/admins/")
async def create_admin(admin: schemas.Admin):
    admin_email = session.query(models.Admin).filter(models.Admin.email == admin.email).first()

    if admin_email is not None:
        raise HTTPException(status_code=400, detail="Invalid data (email is not unique)")

    superpassword = admin.superpassword

    if superpassword == SUPERPASSWORD:
        new_admin = models.Admin(
            name=admin.name,
            email=admin.email,
            hashed_password=generate_password_hash(admin.password),
            is_admin=True,
        )
        session.add(new_admin)
        session.commit()
    else:
        raise HTTPException(status_code=403, detail="Invalid token, access denied")

    return {"message": f"New admin {new_admin.name} has been created successfully"}
