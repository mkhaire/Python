#!/usr/bin/env python3.8
import time

start_time=time.localtime()

print(f"Current time is {time.strftime('%X', start_time)}")
input("Hit enter to stop timer")

stop_time=time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime ('%X', stop_time )}")
print(f"Total time: {difference} seconds")

