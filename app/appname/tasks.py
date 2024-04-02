from core.celery import app

@app.task
def task_one():
    print(" task one called and worker is running good")
    return "success"