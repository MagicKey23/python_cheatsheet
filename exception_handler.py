import sys
import math
import random
import threading
import time

while True:
    try:
        number = int(input("Please enter a number"))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error occurred")
print("Thank You")

