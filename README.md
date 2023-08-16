# Django-PostGres-Docker

This project is a web application built with Django 4, Celery, Redis, PostgreSQL, and Gunicorn. It is designed to provide a robust and scalable platform for handling background tasks and processing as well as serving Django web application requests. By utilizing Docker Compose, the project ensures a streamlined and easy deployment process.

## Technologies Used

- Django 4
- Celery
- Redis
- PostgreSQL
- Gunicorn
- Docker Compose

## Prerequisites

Before running the project, you need to have the following installed on your machine:

- Docker ([Installation Guide](https://docs.docker.com/get-docker/))
- Docker Compose ([Installation Guide](https://docs.docker.com/compose/install/))
- Django ([First Steps](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwie3cypq6qAAxWm0QIHHda1BUYQjBB6BAgiEAE&url=https%3A%2F%2Fdocs.djangoproject.com%2F&usg=AOvVaw2hahrprdfnBm4XSyAwII_q&opi=89978449))

## Getting Started

Follow the instructions below to get the project up and running on your local machine.

Clone the repository:

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

Create a `.env` file in the project root directory and define the environment variables needed for the Django settings and database configuration. Here's a sample `.env` file:

```yaml
# Django settings
SECRET_KEY=your_secret_key_here
DEBUG=True
# Database
SQL_DATABASE=your_postgres_db
SQL_USER=your_postgres_user
SQL_PASSWORD=your_postgres_password
SQL_HOST=host.docker.internal # this url is for local use with external postgres intance
SQL_PORT=5432      # port of your PostrgreSQL instance >= 11
DATABASE=postgres
# Celery settings
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

Build and run the containers:

```yaml
docker-compose up -d --build
```

This command will build the Docker images and start the containers in the background (`-d` flag). It may take a few minutes to download the required images and set up the services.

Access the application:

After the containers are up and running, you can access the Django application in your web browser at `http://localhost/`.

## Usage

Explain how to use the application or any additional functionalities. If there are specific configurations that the user can change, mention them here.

## Stopping the Application

To stop and remove the containers, use the following command:

```yaml
docker-compose down
```

This will stop the running services and remove the containers while keeping the database data (thanks to the named volumes defined in `docker-compose.yml`).

## Contributing

If you want to contribute to this project, feel free to create a pull request.

## Acknowledgments

**[Docker compose with Django 4, Celery, Redis and Postgres](https://saasitive.com/tutorial/django-celery-redis-postgres-docker-compose/)**

---

Happy coding !!!
