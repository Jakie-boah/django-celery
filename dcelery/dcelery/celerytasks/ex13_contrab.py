from datetime import timedelta

import dcelery.celerytasks.ex11_schedule
from dcelery.celery_config import app
from celery.schedules import crontab

app.conf.beat_schedule = {
    "task1": {
        'task': "dcelery.celerytasks.ex12_schedule_custom.task1",
        'schedule': crontab(),
        'kwargs': {'foo': 'bar'},
        'args': (1, 2),
        'options': {
            'queue': 'tasks',
            'priory': 5,
        }
    },
    "task2": {
        'task': "dcelery.celerytasks.ex12_schedule_custom.task2",
        'schedule': timedelta(seconds=10),
    }
}


@app.task(queue='tasks')
def task1(a, b, **kwargs):
    result = a + b
    print(f'running task1 -> {result}')


@app.task(queue='tasks')
def task2():
    print('running task2')


@app.task(queue='tasks')
def task3():
    print('running task3')
