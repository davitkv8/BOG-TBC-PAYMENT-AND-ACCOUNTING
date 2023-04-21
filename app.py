import socket
import uvicorn
import time
import os

from fastapi_sqlalchemy import DBSessionMiddleware
from BOG import router as bog_router
from TBC import router as tbc_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(bog_router)
app.include_router(tbc_router)

app.add_middleware(
    DBSessionMiddleware,
    db_url=f'postgresql://{os.environ.get("POSTGRES_USER")}:'
           f'{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_HOST")}/'
           f'{os.environ.get("POSTGRES_NAME")}'
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
