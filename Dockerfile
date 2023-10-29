FROM python:3.9-bookworm

WORKDIR /usr/src/app
COPY . .

RUN pip3 install -r analysis/requirements.txt