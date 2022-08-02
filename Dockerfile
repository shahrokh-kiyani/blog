FROM python:latest

WORKDIR /code/

# Install dependencies
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/