from time import sleep
from typing_extensions import Self
import datetime as dt
from packages.thread import Thread
import pyttsx3

global speech_engine
speech_engine = pyttsx3.init()

def calc_duration(end_time: dt.time, start_time: dt.time):
    return (end_time.hour - start_time.hour) * 60 * 60 +\
                (end_time.minute - start_time.minute) * 60 +\
                    (end_time.second - start_time.second)

class Alarm(Thread):
    def __init__(self, id: int, end_time: dt.time):
        def cb(duration):
            for o in range(duration):
                sleep(1)
            else:
                for _ in range(3):
                    speech_engine.say("ALARM")
                    speech_engine.runAndWait()
                self.stop()
        super().__init__(cb)
        self.end_time = end_time
        self.id = id

    def activate(self: Self) -> None:
        self.args = [self.duration]
        self.start()
    def deactivate(self: Self) -> None:
        self.stop()
    @property
    def duration(self: Self) -> int:
        start_time = dt.datetime.now().time()
        return calc_duration(self.end_time, start_time)
    @property
    def end_time(self: Self) -> dt.time:
        return self._end_time
    @end_time.setter
    def end_time(self: Self, new: dt.time) -> None:
        if new < dt.datetime.now().time():
            raise ValueError()
        self._end_time = new