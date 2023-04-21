import socket
import uvicorn
import time

from pytz import timezone
from celery import Celery
from fastapi import FastAPI

Tbilisi_timezone = timezone('Asia/Tbilisi')

app = FastAPI()

celery_app = Celery(
    'tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0'
)

import TBC.tasks

celery_app.conf.timezone = Tbilisi_timezone

celery_app.conf.beat_schedule = {

    'scheduled_task_1': {
        'task': 'TBC.tasks.update_balance_data',
        'schedule': 1800
    },

    'scheduled_task_2': {
        'task': 'TBC.tasks.get_movements_data',
        'schedule': 1800
    },

}


if __name__ == "__main__":
    while True:
        try:
            # uvicorn.run(bog_app, host="0.0.0.0", port=8000)
            uvicorn.run(app, host="0.0.0.0", port=8000)
        except socket.error as err:
            print(f"Socket error: {err}")
            time.sleep(5)
        else:
            break
