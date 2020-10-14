#Practice python file for alteration with Git.
import os
import datetime

today = datetime.datetime.now()
def write_to_log(event):
    log_event = event + " " + "[" + str(today) + "]\n"
    with open("log.txt","a") as appender:
        appender.write(log_event)

write_to_log("log test")