from core.celery import app

@app.task
def task_one():
    print(" task one called and worker is running good")
    return "success"


@app.task
def task_two(data, *args, **kwargs):
    print(
        f" task two called with the argument {data} and worker is running good")
    return "success"
