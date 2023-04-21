import socket
import uvicorn
import time

from celery import Celery
from fastapi import FastAPI

app = FastAPI()

celery_app = Celery(
    'tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0'
)

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
