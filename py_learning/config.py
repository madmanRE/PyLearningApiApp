import os
from dotenv import load_dotenv

load_dotenv()

SUPERPASSWORD = os.environ.get("SUPERPASSWORD")

DB_NAME = os.environ.get("DB_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

SMTP_HOST = os.environ.get("EMAIL_HOST")
SMTP_HOST_USER = os.environ.get("EMAIL_HOST_USER")
SMTP_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
SMTP_PORT = int(os.environ.get("EMAIL_PORT"))
SMTP_USE_TLS = os.environ.get("EMAIL_USE_TLS")

STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
