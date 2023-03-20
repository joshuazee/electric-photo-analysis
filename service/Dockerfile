FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
MAINTAINER sss
COPY ./app /app
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt