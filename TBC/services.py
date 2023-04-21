from typing import TYPE_CHECKING, List

import database as _database
import models as _models
# import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
