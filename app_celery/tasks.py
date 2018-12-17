import os
from celery import Celery


CELERY_CONNECTION = os.environ.get('CELERY_CONNECTION')


app = Celery('tasks', broker=CELERY_CONNECTION)


@app.task(bind=True, default_retry_delay=10)
def task_hello(task, *args, **kwargs):
    print('!!!!!')


@app.task(bind=True,default_retry_delay=10)
def task_world(task, *args, **kwargs):
    print('??????')
