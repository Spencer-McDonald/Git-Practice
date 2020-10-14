#Practice python file for alteration with Git.
import os
import datetime

today = datetime.datetime.now()

# Function to take passed variable and log with date as an event.
def write_to_log(event):
    log_event = "[" + str(today) + "]" + event + "\n"


write_to_log("log test")