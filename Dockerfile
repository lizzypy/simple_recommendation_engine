FROM python:3.10-bookworm

WORKDIR /usr/src/app
COPY . .

RUN pip3 install -r requirements.txt

