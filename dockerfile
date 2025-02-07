FROM python:3.10

WORKDIR /app

COPY source dest
(ex: COPY requirements.txt requirements.txt)

RUN pip install --upgrade pip
RUN pip install -r requirements.txt