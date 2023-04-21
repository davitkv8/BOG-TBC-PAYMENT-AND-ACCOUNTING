from app import celery_app
from .tbc_api import TbcApiExternal

tbc_api = TbcApiExternal()


@celery_app.task
def update_balance_data():
    return tbc_api.get_balance()


@celery_app.task
def get_movements_data():
    return tbc_api.get_movements()
