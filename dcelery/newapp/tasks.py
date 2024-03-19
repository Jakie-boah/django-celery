from celery import shared_task
import time
from django.core.management import call_command


@shared_task(task_rate_limit='1/m')
def management_command(queue='tasks'):
    call_command('test_command')


# @shared_task
# def tp2(queue='celery:1'):
#     time.sleep(3)
#     return
#
#
# @shared_task
# def tp3(queue='celery:2'):
#     time.sleep(3)
#     return
#
#
# @shared_task
# def tp4(queue='celery:3'):
#     time.sleep(3)
#     return

