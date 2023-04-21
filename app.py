import socket
import uvicorn
import time

from fastapi import FastAPI

app = FastAPI()

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
