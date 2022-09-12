import ctypes
from string import ascii_lowercase
import threading
from types import FunctionType
import random


class Thread(threading.Thread):
    def __init__(self, cb: FunctionType, args: list = [], kwargs: dict = {}, name: str = ''.join(random.choices(ascii_lowercase, k = 5))):
        threading.Thread.__init__(self)
        self.name = name
        self.cb = cb
        self.args = args
        self.kwargs = kwargs
    def run(self):
        try:
            self.cb(*self.args, **self.kwargs)
        finally:
            pass
    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
    def stop(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        self.join()