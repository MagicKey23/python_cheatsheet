import sys
import math
import random
import threading
import time
import re

if re.research("ape", "The ape at the apex"):
    print("THere is an ape")

allApes =re.findall("ape", "The ape at the apex")

for i in allApes:
    print(i)

the_str = "The ape at the apex"

for i in re.finditer("ape", the_str):
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])



