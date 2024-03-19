from sentry_sdk import capture_exception


from dcelery.celery_config import app

"""
from dcelery.celerytasks.ex10_sentry import divide_numbers
divide_numbers()
"""


@app.task(queue='tasks')
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as ex:
        raise ex

