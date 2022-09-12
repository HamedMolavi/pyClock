from types import FunctionType
from typing import Any, Optional
import os
import sys
global alarms
global end_times
alarms = []
end_times = []

def inp(prompt:str ="Enter input: ", reprompt:str ="Enter correctly: ", key:Optional[FunctionType] = None, convert:Optional[FunctionType] = None)-> Any:
    try:
        value = input(prompt)
    except KeyboardInterrupt:
        clean_exit()
    if key and convert:
        while True:
            if not value:
                try:
                    value = input(reprompt)
                except KeyboardInterrupt:
                    clean_exit()
                continue
            try:
                value = convert(value)
                try:
                    if key(value):
                        break
                    else:
                        try:
                            value = input(reprompt)
                        except KeyboardInterrupt:
                            clean_exit()
                except:
                    try:
                        value = input(reprompt)
                    except KeyboardInterrupt:
                        clean_exit()
                    continue
            except:
                try:
                    value = input(reprompt)
                except KeyboardInterrupt:
                    clean_exit()
                continue
    elif key and not convert:
        while True:
            try:
                if key(value):
                    break
                else:
                    try:
                        value = input(reprompt)
                    except KeyboardInterrupt:
                        clean_exit()
                    continue
            except:
                try:
                    value = input(reprompt)
                except KeyboardInterrupt:
                    clean_exit()
                continue
    elif convert and not key:
        while True:
            try:
                value = convert(value)
                break
            except:
                try:
                    value = input(reprompt)
                except KeyboardInterrupt:
                    clean_exit()
                continue
    return value


def clear()->None:
    if sys.platform in ['win32', 'cygwin']:
        os.system('cls')
    elif sys.platform in ['linux', 'darwin']:
        os.system('clear')


def clean_exit():
    for alarm in alarms:
        try:
            alarm.deactivate()
        except: continue
    sys.exit("Goodbye")

def print_alarms():
    i = 0
    for alarm, end_time in zip(alarms, end_times):
        if alarm: print(f"Alarm for {end_time} is active -> id = {i}")
        else: print(f"Alarm for {end_time} is deactive -> id = {i}")
        i += 1
