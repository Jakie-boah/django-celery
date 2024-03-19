from datetime import timedelta

import dcelery.celerytasks.ex11_schedule
from dcelery.celery_config import app

app.conf.beat_schedule = {
    "task1": {
        'task': "dcelery.celerytasks.ex11_schedule.task1",
        'schedule': timedelta(seconds=5),
    },
    "task2": {
        'task': "dcelery.celerytasks.ex11_schedule.task2",
        'schedule': timedelta(seconds=10),
    }
}


@app.task(queue='tasks')
def task1():
    print('running task1')


@app.task(queue='tasks')
def task2():
    print('running task2')


@app.task(queue='tasks')
def task3():
    print('running task3')
