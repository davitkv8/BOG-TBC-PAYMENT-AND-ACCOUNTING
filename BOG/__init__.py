from .router import *
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

