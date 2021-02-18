FROM python:3
RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt /code/
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/