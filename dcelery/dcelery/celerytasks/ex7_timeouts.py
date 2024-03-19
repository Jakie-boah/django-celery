from dcelery.celery_config import app
from time import sleep
import sys

"""
from dcelery.celerytasks.ex7_timeouts import long_running_task
long_running_task()

from dcelery.celerytasks.ex7_timeouts import execute_task_examples
execute_task_examples()
"""


@app.task(queue='tasks', time_limit=10)
def long_running_task():
    sleep(6)
    return "Task completed - 1"


def execute_task_examples():
    result = long_running_task.delay()
    try:
        task_result = result.get(timeout=4)
    except TimeoutError:
        print("Task timed out")

    task = long_running_task.delay()
    task.revoke(terminate=True)