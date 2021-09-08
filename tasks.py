import time
from celery import Celery

from script.tasks.start_app import (
    _subscriber
)

app = Celery(
    'start_app',
    broker='amqp://localhost//',
)


@app.task
def __subscriber(server_configure):
    _subscriber(server_configure)
