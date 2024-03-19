from celery import chain
from dcelery.celery_config import app


@app.task(queue='tasks')
def add(x, y):
    return x + y


@app.task(queue='tasks')
def multiply(z):
    if z == 5:
        raise ValueError('Error division by zero')
    return z * 2


def run_task():
    task_chain = chain(add.s(2, 3), multiply.s())
    result = task_chain.apply_async()
    result.get()
