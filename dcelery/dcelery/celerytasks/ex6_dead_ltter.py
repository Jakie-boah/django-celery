from dcelery.celery_config import app
from celery import group

app.conf.task_reject_on_worker_lost = True


@app.task(queue='tasks')
def my_task(z):
    try:
        if z == 2:
            raise ValueError('wrong number')
    except Exception as e:
        handle_failed_task.apply_async(args=(z, str(e)))


@app.task(queue='dead_letter')
def handle_failed_task(z, exception):
    return "Custom logic to process"


def runtask():
    task_group = group(
        my_task.s(1),
        my_task.s(2),
        my_task.s(3),
    )
    task_group.apply_async()