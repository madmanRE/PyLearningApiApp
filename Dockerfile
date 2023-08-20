FROM python:3.11.3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY py_learning /app/py_learning

WORKDIR /app/py_learning

