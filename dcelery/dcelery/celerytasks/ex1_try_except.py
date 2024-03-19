from dcelery.celery_config import app
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(actime)s %(levelname)s %(message)s')


@app.task(queue='tasks')
def my_task():
    try:
        raise ConnectionError("Connection error Occurred...")

    except ConnectionError:
        logging.error('Connection error occurred....')
        raise ConnectionError()
