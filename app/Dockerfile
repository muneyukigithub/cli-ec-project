FROM python:latest
WORKDIR /code
COPY ./requirements.txt /code
RUN pip install --upgrade pip setuptools
RUN pip install -r /code/requirements.txt