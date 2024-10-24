from typing import Any, Optional
import redis  # Import the Redis exception class if you're using the Redis library


from redis_db import get_redis
from config import get_settings

settings = get_settings()


def store_reset_token(key: str, sub: str = '', mapping: dict[str, Any] = {}) -> Optional[int]:
    """
    Add a reset token to the Redis database.

    Args:
        key (str): The Redis key for the token.
        mapping (dict[str, Any]): A dictionary containing token data.

    Returns:
        Optional[int]: 1 if a new field is created, 0 if the field existed and was updated.
                       None if an error occurs.

    Raises:
        redis.RedisError: If there's an issue interacting with the Redis database.
    """
    redis_db = get_redis()
    store_mapping = {
        'sub': sub,
        **mapping
    }
    try:
        new_token = redis_db.hset(key, mapping=store_mapping)
        redis_db.expire(key, settings.reset_token_expiry_seconds)
        return new_token
    except redis.RedisError as e:
        # Raise the original Redis exception with a custom message for more context
        raise redis.RedisError(f"Failed to add reset token for key '{key}': {e}")


def get_reset_token(key: str) -> Optional[str]:
    """
    Retrieve a reset token from the Redis database.

    Args:
        name (str): The Redis key for the token.

    Returns:
        Optional[str]: The token if found, or None if the token is not found.

    Raises:
        redis.RedisError: If there's an issue interacting with the Redis database.
    """
    redis_db = get_redis()
    try:
        saved_token = redis_db.hgetall(key)
        if saved_token is None:
            raise ValueError(f"No token found for key '{key}'")
        return saved_token
    except redis.RedisError as e:
        # Raise the original Redis exception with a custom message for more context
        raise redis.RedisError(f"Failed to retrieve reset token for key '{key}': {e}")
