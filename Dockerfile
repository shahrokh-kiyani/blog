FROM python:latest

ENV PYTHONDONTWRITEBYTECODEBYDEFAULT=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/

# Install dependencies
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/