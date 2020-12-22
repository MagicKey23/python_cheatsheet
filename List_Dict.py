import sys
import math
import random
import threading
import time
from functools import reduce

list1 = [1, 3.14, "Kaney", True]
print("Length", len(list1))
print("1st", list[0])
print("Last", list[-1])

list1[0] = 2
# Replace value in array
list1[2:4] = ["Bob", False]
print(list1)
list1[2:2] = ["Paul", 9]
print(list1)

# copy list and append new vale
list2 = list1 + ["Egg", 4]
list2.remove("Paul")
list2.pop(0)
print("list2", list2)

list2 = ["Egg", 4] + list1
# 2D dimensional
list3 = [[1, 2], [3, 4]]

# Access List
print("1 Exists", (1 in list1))
print("Min", min([1, 2, 3]))
print("Max", max([1, 2, 3]))
print("1 index to 2", list1[0:2])
print("Every Other", list1[0:2])
print("Reverse", list1[::-1])

w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1

w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        break
    else:
        w2 += 1
        continue
    w2 += 1

list4 = [1, 3.14 , "Kaney"]
# 0 is auto false
while len(list4):
    print(list4.pop(0))

# for loop

for x in range(0, 10):
    print(x, ' ', end="")
print()

for x in list4:
    print(x)


for x in [2, 4, 6]:
    print(x)

# iterator
list5 = [6, 9, 12]
iterator = iter(list5)
# print next value in the iterator
print(next(iterator))

print(list(range(1, 5)))
print(list(range(1, 10, 2)))
num_list = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# Turpes

# like list but can't be change, immutable list
t1 = (1, 3.14, "Kaney")
print("Length", len(t1))
print("1st", t1[0])
print("last", t1[-1])
print("1st 2", t1[0:2])
print("every other", t1[0:-1:2])


# Dictionary
heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne"
}
print("length", len(heroes))

print(heroes["Superman"])
heroes["Flash"] = "Barry Allen"
# return an array using that dictionary
print(list(heroes.items()))
# return keys
print(list(heroes.keys()))
# return values
print(list(heroes.values()))

# delete
del heroes["Flash"]
print(heroes.pop("Batman"))
print("Superman" in heroes)
for k in heroes:
    print(k)
for v in heroes.values():
    print(v)

d1 = {"name": "Bread", "price": 0.88}
# mapping
print("%(name)s costs $%(price).2f" % d1)


# SET
s1 = set(["Kaney", 1])
s2 = {"Paul", 1}
print("Length", len(s2))
s3 = s1 | s2
print(s3)
s3.add("Marey")
s3.discard("Marey")
print("Random", s3.pop())
s3 |= s2
# return value that is in s1 and s2
print(s1.intersection(s2))
# return
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
s3.clear()
# set can't be change
s4 = frozenset(["Paul", 7])


