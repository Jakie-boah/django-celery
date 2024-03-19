from dcelery.celery_config import app
from time import sleep
import sys
import json

"""
from dcelery.celerytasks.ex8_handle_error import run_task
long_running_task()
"""


@app.task(queue='tasks')
def long_running_task():
    raise ValueError('Ебаный пиздец ошибка')


@app.task(queue='tasks')
def process_task_result(result):
    sys.stdout.write(result)
    sys.stdout.write("process task results")
    sys.stdout.flush()


@app.task(queue='tasks')
def error_handler(task_id, exc, traceback):
    sys.stdout.write(">>>>")
    sys.stdout.write(exc)
    sys.stdout.write(">>>>")
    sys.stdout.flush()


def run_task():
    long_running_task.apply_async(link=[process_task_result.s(), ], link_error=[error_handler.s()])
