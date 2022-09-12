import re
from time import sleep
import datetime as dt
from packages.alarm import Alarm
from packages.timer import Timer
from packages.functions import clear, inp, print_alarms, alarms, end_times


def main():
    commands = ['alarm', 'timer', 'deactive', 'active']
    while True:
        clear()
        print_alarms()
        command = inp(f"What is your command ({', '.join(commands)})? ", convert=str.lower, key=lambda el: el in commands)
        if command == 'timer':
            time = inp("Time: ", "In format of hh:mm:ss or hh:mm\nTime: ", convert = convert_timer)
            timer = Timer(time)
            timer.start()
        elif command == 'alarm':
            clock = inp("Time: ", "In format of\nhh:mm:ss or hh:mm\nAnd not in the past\nTime: ", convert= convert_clock)
            end_times.append(clock)
            alarms.append(Alarm(len(alarms), clock))
            print(f"Alarm added with id {len(alarms) - 1}")
            sleep(2)
            alarms[-1].activate()
        elif command == 'deactive':
            id = inp("Alarm id: ", convert= int, key=lambda el: el in range(len(alarms)))
            alarms[id].deactivate()
            alarms[id] = None
            print(f"Alarm deactivated")
            sleep(1)
        elif command == 'active':
            id = inp("Alarm id: ", convert= int, key=lambda el: el in range(len(alarms)))
            try:
                alarms[id] = Alarm(id, end_times[id])
                alarms[id].activate()
            except ValueError:
                answer = inp(
                    "The time of this alarm has passed. You want to reset it or delete it? ",
                    "reset or delete",
                    convert= str.lower,
                    key=lambda el: el in ['reset', 'delete']
                )
                if answer == 'reset':
                    clock = inp("Time: ", "In format of\nhh:mm:ss or hh:mm\nAnd not in the past\nTime: ", convert= convert_clock)
                    end_times[id] = clock
                    alarms[id] = Alarm(id, end_times[id])
                    alarms[id].activate()
                else:
                    end_times.pop(id)
                    alarms.pop(id)
                    continue
            print(f"Alarm activated")
            sleep(1)


def convert_clock(s: str) -> dt.time:
    try: c = dt.datetime.strptime(s, '%H:%M:%S').time()
    except: c = dt.datetime.strptime(s + ':00', '%H:%M:%S').time()
    if c > dt.datetime.now().time():
        return c
    raise ValueError()

def convert_timer(s: str) -> dt.timedelta:
    try:
        hours, minutes, seconds = re.match(r'^(\d|\d\d):(\d|[0-5][0-9])(?::(\d|[0-5][0-9]))?$', s).groups()
        seconds = int(hours) * 60 * 60 + int(minutes) * 60 + (int(seconds) if seconds else 0)
        return dt.timedelta(seconds= seconds)
    except: raise ValueError()

def calc_duration(end_time: dt.time, start_time: dt.time):
    return (end_time.hour - start_time.hour) * 60 * 60 +\
                (end_time.minute - start_time.minute) * 60 +\
                    (end_time.second - start_time.second)



if __name__ == "__main__":
    main()