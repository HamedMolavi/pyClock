from time import sleep
from typing import Any
from typing_extensions import Self
import pyttsx3
import datetime as dt
from packages.functions import clear, inp
from packages.thread import Thread


class Timer:
    def __init__(self, timer: dt.timedelta) -> None:
        self.interval = timer
    def __sub__(self: Self, __other: Any) -> None:
        if isinstance(__other, int):
            self.interval =  dt.timedelta(
                seconds= self.interval - __other
            )
    def __str__(self: Self) -> str:
        return str(self.__interval)
    def __add__(self: Self, __other: Any) -> None:
        if isinstance(__other, int):
            self.interval =  dt.timedelta(
                seconds= self.interval + __other
            )
    def __bool__(self: Self) -> bool:
        return bool(self.interval)
    def __lt__(self: Self, __other: int) -> bool:
        if isinstance(__other, int):
            return self.interval < __other
        raise TypeError(f"'<' not supported between instances of 'Interval' and {str(type(__other))}")
    def __le__(self: Self, __other: int) -> bool:
        if isinstance(__other, int):
            return self.interval <= __other
        raise TypeError(f"'<=' not supported between instances of 'Interval' and {str(type(__other))}")
    def __gt__(self: Self, __other: int) -> bool:
        if isinstance(__other, int):
            return self.interval > __other
        raise TypeError(f"'>' not supported between instances of 'Interval' and {str(type(__other))}")
    def __ge__(self: Self, __other: int) -> bool:
        if isinstance(__other, int):
            return self.interval >= __other
        raise TypeError(f"'>=' not supported between instances of 'Interval' and {str(type(__other))}")
    def __eq__(self: Self, __other: int) -> bool:
        if isinstance(__other, int):
            return self.interval == __other
        raise TypeError(f"'==' not supported between instances of 'Interval' and {str(type(__other))}")
    def __ne__(self: Self, __other: int) -> bool:
        if isinstance(__other, int):
            return self.interval != __other
        raise TypeError(f"'!=' not supported between instances of 'Interval' and {str(type(__other))}")
    @property
    def interval(self: Self) -> int:
        return self.__interval.seconds
    @interval.setter
    def interval(self: Self, new: dt.timedelta) -> None:
        self.__interval = new
    def done(self: Self) -> None:
        self.interval = dt.timedelta()
        def beep():
            while True:
                try:
                    pyttsx3.speak('beep')
                    sleep(1)
                except:
                    pass
        thread = Thread(cb= beep)
        thread.start()
        if inp("Enter any character to stop!! ", "Anything but empty: ", key= lambda el: bool(el)):
            thread.stop()
    def start(self: Self) -> None:
        while self != 0:
            clear()
            try:
                print(self)
                self - 1
                sleep(0.9)
            except KeyboardInterrupt:
                answer = inp("Do you want to resume pause or cancel (r/p/c)? ", convert= str.lower, key= lambda el: el in ['r', 'p', 'c'])
                if answer == 'p':
                    if inp(
                        "Please enter 'r' to resume the alarm, or 'c' to call off the alarm.\n","",
                        convert= str.lower,
                        key= lambda el: el in ['r', 'c']
                    ) == 'r':
                        continue
                    else: break
                elif answer == 'r': continue
                else:
                    print(answer)
                    break
        else:
            self.done()
