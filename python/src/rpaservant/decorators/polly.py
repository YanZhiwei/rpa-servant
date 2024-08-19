from functools import wraps
from rpaservant.exceptions.pollyBreakException import PollyBreakException
from rpaservant.exceptions.pollyContinueException import PollyContinueException
import time


def Polly(func, name: str = "", retry_count: int = 3):
    """函数重试decorator

    Args:
        func (_type_): _description_

    Returns:
        _type_: _description_
    """

    def wrapper(*args, **kwargs):
        for i in range(retry_count):
            start_time = time.time()
            try:
                return func(*args, **kwargs)
            except PollyBreakException as e:
                break
            except PollyContinueException as e:
                continue
            except Exception as e:
                pass

    return wrapper
