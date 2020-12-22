import sys
import math
import random
import threading
import time

def execute_thread(i):
    print("Thread {} sleeps at {}".format(i, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
    rand_sleep_time = random.randint(1, 5)
    time.sleep(rand_sleep_time)
    print("Thread {} stops sleeping at {}".format(i, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))

# create thread
for i in range(0, 5):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()
    print("Active Thread:",threading.activeCount())
    print("Thread Objects:", threading.enumerate())
