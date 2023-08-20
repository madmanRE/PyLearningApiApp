import smtplib
from email.message import EmailMessage

from celery import Celery
from config import SMTP_HOST_USER, SMTP_HOST_PASSWORD, SMTP_HOST, SMTP_PORT

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_message(username: str, email_to: str):
    email = EmailMessage()
    email['Subject'] = 'PyLearning'
    email['From'] = SMTP_HOST_USER
    email['To'] = email_to

    email.set_content(
        '<div>'
        '<h1 style="color:red">Message from PyLearning</h1>'
        f'Hellow {username.capitalize()}!'
        '</div>',
        subtype='html'
    )

    return email


@celery.task()
def send_email_report(username: str, email: str):
    email_msg = get_email_message(username, email)
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_HOST_USER, SMTP_HOST_PASSWORD)
        server.send_message(email_msg)

