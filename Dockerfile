# Change the escape character for Windows
# escape=` (backtick)

# Built off of Python3.8-alpine
FROM python:3.8-alpine

COPY requirements.txt /etc/conf/requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add build-base libressl-dev
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers
RUN pip install -r /etc/conf/requirements.txt
RUN apk del .tmp
RUN apk del .build-deps

RUN apk add --no-cache git
RUN git clone https://github.com/RohitKochhar/FTU-Django-Dashboard.git
RUN apk del git

WORKDIR FTU-Django-Dashboard/TestGUI/
RUN python manage.py makemigrations
RUN python manage.py migrate --run-syncdb

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000

