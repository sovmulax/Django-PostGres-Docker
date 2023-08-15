FROM ubuntu:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update package repository and install required packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip supervisor postgresql-client postgresql-server-dev-all gcc g++ \
    curl netcat nano

# Upgrade pip and install gunicorn
RUN pip3 install --upgrade pip && pip3 install gunicorn

# Create working directory
WORKDIR /usr/src/app

# Copy requirements and install them
COPY ./requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt

# Copy your application files
COPY ./app /usr/src/app/backend
COPY ./docker /usr/src/app/docker

# Copy Supervisor configuration files
COPY ./docker/supervisor/supervisord.conf /etc/supervisor/conf.d/

# Make entrypoint scripts executable
RUN chmod +x /usr/src/app/docker/backend/server-entrypoint.sh
RUN chmod +x /usr/src/app/docker/backend/worker-entrypoint.sh
RUN chmod +x /usr/src/app/docker/backend/beat-entrypoint.sh
RUN chmod +x /usr/src/app/docker/backend/daemon-entrypoint.sh
