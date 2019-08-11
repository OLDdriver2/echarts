from __future__ import with_statement  # Required in 2.5
import threading
import time
import signal
from contextlib import contextmanager


def time_limited(timer):
    '''
    一个规定函数执行时间的装饰器
    :param timer:
    :return:
    '''

    def wrapper(func):
        def __wrapper(params):
            start_time = time.time()
            # 通过设置守护线程强制规定函数的运行时间
            t = threading.Thread(target=func, args=params)
            t.setDaemon(True)
            t.start()
            time.sleep(timer)
            if t.is_alive():
                # 若在规定的运行时间未结束守护进程，则主动抛出异常
                raise Exception('Function execution timeout')
            # print time.time()-start_time

        return __wrapper

    return wrapper


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise Exception

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
