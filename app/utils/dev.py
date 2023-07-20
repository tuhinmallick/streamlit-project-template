from functools import wraps
from time import time

from loguru import logger


def timing(func):
    """Use timing decorator to time functions for debugging."""

    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            logger.debug(
                f"{func.__name__}:: Total execution time: {end_ if end_ > 0 else 0} ms"
            )

    return _time_it
