import redis
from config import get_settings

settings = get_settings()


def get_redis():

    return redis.Redis(
        host=settings.redis_host,
        port=int(settings.redis_port),
        password=settings.redis_password,
        decode_responses=True
    ) if settings.environment == 'development' else redis.Redis(
        host=settings.redis_host,
        port=int(settings.redis_port),
        decode_responses=True
    )
