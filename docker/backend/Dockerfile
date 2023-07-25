FROM python:3.8.15-alpine

WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc g++ python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install gunicorn

RUN apk --update add libxml2-dev libxslt-dev libffi-dev musl-dev libgcc openssl-dev curl postgresql-client
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev nano
RUN pip3 install psycopg2 psycopg2-binary httpie django-cors-headers
RUN pip3 uninstall pytz tzdata
RUN pip3 install pytz==2022.2.1 tzdata==2022.2

ADD ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

ADD ./app /usr/src/app/backend
ADD ./docker /usr/src/app/docker

RUN chmod +x /usr/src/app/docker/backend/server-entrypoint.sh
RUN chmod +x /usr/src/app/docker/backend/worker-entrypoint.sh