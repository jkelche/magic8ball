FROM python:alpine

COPY . /app
WORKDIR /app


COPY magic8ball.py /opt/magic8ball.py
CMD python ./magic8ball.py