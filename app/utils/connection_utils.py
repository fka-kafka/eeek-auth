from app.database import get_db
from app.redis import get_redis


def get_connections():
    db = next(get_db())
    redis_connection = get_redis()
    try:
        yield db, redis_connection
    finally:
        db.close()
        redis_connection.close()