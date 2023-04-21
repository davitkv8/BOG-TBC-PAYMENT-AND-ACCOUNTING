import socket
import uvicorn
import time
import os

from pytz import timezone
from fastapi import FastAPI
from celery import Celery
from fastapi_sqlalchemy import DBSessionMiddleware

from BOG import router as bog_router
from TBC import router as tbc_router

Tbilisi_timezone = timezone('Asia/Tbilisi')

app = FastAPI()
app.include_router(bog_router)
app.include_router(tbc_router)

app.add_middleware(
    DBSessionMiddleware,
    db_url=f'postgresql://{os.environ.get("POSTGRES_USER")}:'
           f'{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_HOST")}/'
           f'{os.environ.get("POSTGRES_NAME")}'
)

celery_app = Celery(
    'tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0'
)

import TBC.tasks

celery_app.conf.timezone = Tbilisi_timezone

celery_app.conf.beat_schedule = {

    'scheduled_task_1': {
        'task': 'TBC_API.tasks.update_balance_data',
        'schedule': 1800
    },

    'scheduled_task_2': {
        'task': 'TBC_API.tasks.get_movements_data',
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
