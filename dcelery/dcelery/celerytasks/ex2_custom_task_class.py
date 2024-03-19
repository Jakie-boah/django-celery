from dcelery.celery_config import app
import logging
from celery import Task
logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(actime)s %(levelname)s %(message)s')


class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error('Connection error occurred - admin notified')
        else:
            print('{0!r} failed: {1!r}'.format(task_id, exc))


app.Task = CustomTask


@app.task(queue='tasks')
def my_task():
    try:
        raise ConnectionError("Connection error Occurred...")

    except ConnectionError:
        logging.error('Connection error occurred....')
        raise ConnectionError()
