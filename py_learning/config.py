import os
from dotenv import load_dotenv

load_dotenv()

SUPERPASSWORD = os.environ.get("SUPERPASSWORD")

DB_NAME = os.environ.get("DB_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
