FROM python:3.8.3-alpine

ENV BASE_DIR=/home/deals

# set work directory
RUN mkdir -p $BASE_DIR
RUN mkdir -p $BASE_DIR/static

# where the code lives
WORKDIR $BASE_DIR

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy project
COPY . $BASE_DIR
RUN pip install -r requirements.txt
