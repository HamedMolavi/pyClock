<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Clock</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)

</div>

---

<p align="center"> This program lets you have alarms and timers both together. It's like a clock application of your smart phone.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Packages](#packages)
- [Project.py](project)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

The purpose of writing this program was working and exercising with [threading](#threading) in python along with what we've learned in [CS50p](#CS50p). The program uses multi-threads to engage with time and set timers and alarms to warn the user at specified time.

The usage of this program is simple and even though it runs in a [command line enviroment](#command_line_enviroment), I tried to make it user friendly and easy to work with.
There is still bugs and errors in the program obviously, but I tried to minimize the amount of those and handle them with error exceptions.

## 🏁 Prerequisites <a name = "prerequisites"></a>

Every module you need to have installed to run this program, will be installed automatically by typing this command in your command-line window. Note that you should be in the program root directory.

```
pip install -r requirements.txt
```

## 🎈 Usage <a name="usage"></a>

To use the program is simple, just run project.py in a command-line enviroment in your Mac or windows as below.
```
python project.py
```

## 🚀 Packages <a name = "packages"></a>

In the packages directory, there are some python files used in the main project file.

### thread.py

This file contains a class called 'Thread'. This class inherits from 'Thread' object of built-in 'threading' module. Initilizing parameters of this class are as below:
- @cb: A callback function which fires in a new thread created.
- @agrs: A list of arguments defaulted to an empty list passed to the callback function when it's called.
- @kwargs: A key value dictionary defaulted to an empty dict passed to the callback function when it's called.
- @name: An optional name for the new thread. If not passed, a random name would be generated.

### alarm.py

This file also contains a class called 'Alarm'. It inherits from 'Thread' class from thread.py all of it's functionality.Initilizing parameters of this class are as below:
- @id: An id of the new alarm object.
- @end_time: A time at which the new alarm object invokes its callback function.

The callback funciton of an alarm object is pre-assigned. It's purpose is to alarm the user by saying the 'alarm' word for several times.

### timer.py

This file also contains a class called 'Timer'. This class is similar to 'Alarm' class. It inherits from 'Thread' and its callback function would warn the user after a specified time using pyttsx3 module. Initilizing parameter of this class are as below:
- @timer: A timedelta to be used in callback function. After this timer, the callback function would be invoked and warn the user.

### function.py

In this file, I wrote and classified my needed functions that are used in several places in the project. A brief explanation of each function is as below:

- inp: This function controls the prompting process and customize the input user entered.
  - @convert: This parameter accepts a function to convert entered input to a desired value and returns that value.
  - @key: This parameter also accepts a function to chek the entered input. The passed function sould return a boolean value.
- clear: This function just clears the command-line terminal.
- clean_exit: This function terminates all of the alarm threads before exiting the program, otherwise the program wont be exited. The clean_exit function is invoked when ever the user presses Ctrl+C in prompting process.
- print_alarms: This function just prints existing alarms to the user.

## ⛏️ Project.py <a name = "project"></a>

The main file or the executable file of this project is project.py. The 'main' function in this file just takes a command from the user and based on that command creates related objects and invokes their funcitonality.

In this file there is also three more functions each of which is:
- convert_clock: A function to convert the inputed string of a clock time into a datetime.time object.
- convert_timer: A function to convert the inputed string of a timer into a datetime.timedelta object.
- calc_duration: A function to calculate time difference between to clocks in one day. It returns this difference in seconds as an int object.

## ✍️ Authors <a name = "authors"></a>

- [@HamedMolavi](https://github.com/HamedMolavi) - Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- CS50p course, Harvard University
- Inspired from Jessica Wilkins, <a href='https://www.freecodecamp.org/news/python-projects-for-beginners/'>This post.</a>
