import sys
import math
import random
import threading
import time

class Square:
    #constructor
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width
    #getter function
    @property
    def height(self):
        print("Retrieving the height")
        return self.__height
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")
    @property
    def width(self):
        print("retrieving width")
        return self.__width
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for height")


    def getArea(self):
        return int(self.__width) * int(self.__height)

square = Square()
square.height = "10"
square.width  = "10"
print("Area", square.getArea())
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118

import sys
import math
import random
import threading
import time
from functools import reduce

# ----- INTRO -----
# Python files end with the extension .py
# Print to the console
# Python statements terminate with a newline
print("Hello World")

# Accept user input and store it in a variable
# name = input("What is your name ")
# print("Hi ", name)

# If you want to extend a statement to multiple
# lines you can use parentheses or \
v1 = (
        1 + 2
        + 3
)
v1 = 1 + 2 \
     + 3

# Put multiple statements on 1 line
v1 = 5;
v1 = v1 - 1

"""
Multi-line
Comment
"""

# ----- VARIABLES -----
# Variables are names assigned to values
# The 1st character must be _ or a letter
# Then you can use letters, numbers or _
# Variable names are type sensitive
v2 = 1
V2 = 2  # v1 is different from V1

# You can assign multiple variables
v3 = v4 = 20

# ----- DATA TYPES -----
# Data in Python is dynamically typed and that
# data type can change
# All data is an object which I cover later
# The basic types are integers, floats,
# complex numbers, strings, booleans
# Python doesn't have a character type

# How to get the type
print(type(10))

# There is no limit to the size of integers
# This is a way to get a practical max size
print(sys.maxsize)

# Floats are values with decimal values
# This is how to get a max float
print(sys.float_info.max)

# But, they are accurate to 15 digits
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print(f3)

# Complex numbers are [real part]+[imaginary part]
cn1 = 5 + 6j

# Booleans are either True or False
b1 = True

# Strings are surrounded by ' or "
str1 = "Escape Sequences \' \t \" \\ and \n"

str2 = '''Triple quoted strings can contain ' and "'''

# You can cast to different types with int, float,
# str, chr
print("Cast ", type(int(5.4)))  # to int
print("Cast 2 ", type(str(5.4)))  # to string
print("Cast 3 ", type(chr(97)))  # to string
print("Cast 4 ", type(ord('a')))  # to int

# ----- OUTPUT -----
# You can define a separator for print
print(12, 21, 1974, sep='/')

# Eliminate newline
print("No Newline", end='')

# String formatting %e for exponent
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, 'A'))

# ----- MATH -----
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

# Shortcuts
i1 = 2
i1 += 1
print("i1 ", i1)

# Math Functions
print("abs(-1) ", abs(-1))
print("max(5, 4) ", max(5, 4))
print("min(5, 4) ", min(5, 4))
print("pow(2, 2) ", pow(2, 2))
print("ceil(4.5) ", math.ceil(4.5))
print("floor(4.5) ", math.floor(4.5))
print("round(4.5) ", round(4.5))
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0) ", math.radians(0))
print("degrees(pi) ", math.degrees(math.pi))

# Generate a random int
print("Random", random.randint(1, 101))

# ----- NaN & inf -----
# inf is infinity
print(math.inf > 0)

# NaN is used to represent a number that can't
# be defined
print(math.inf - math.inf)

# ----- CONDITIONALS -----
# Comparison Operators : < > <= >= == !=

# if, else & elif execute different code depending
# on conditions
age = 30
if age > 21:
    # Python uses indentation to define all the
    # code that executes if the above is true
    print("You can drive a tractor trailer")
elif age >= 16:
    print("You can drive a car")
else:
    print("You can't drive")

# Make more complex conditionals with logical operators
# Logical Operators : and or not
if age < 5:
    print("Stay Home")
elif (age >= 5) and (age <= 6):
    print("Kindergarten")
elif (age > 6) and (age <= 17):
    print("Grade %d", (age - 5))
else:
    print("College")

# Ternary operator in Python
# condition_true if condition else condition_false
canVote = True if age >= 18 else False

# ----- STRINGS -----
# Raw strings ignore escape sequences
print(r"I'll be ignored \n")

# Combine strings with +
print("Hello " + "You")

# Get string length
str3 = "Hello You"
print("Length ", len(str3))

# Character at index
print("1st ", str3[0])

# Last character
print("Last ", str3[-1])

# 1st 3 chrs
print("1st 3 ", str3[0:3])  # Start, up to not including

# Get every other character
print("Every Other ", str3[0:-1:2])  # Last is a step

# You can't change an index value like this
# str3[0] = "a" because strings are immutable
# (Can't Change)
# You could do this
str3 = str3.replace("Hello", "Goodbye")
print(str3)

# You could also slice front and back and replace
# what you want to change
str3 = str3[:8] + "y" + str3[9:]
print(str3)

# Test if string in string
print("you" in str3)

# Test if not in
print("you" not in str3)

# Find first index for match or -1
print("You Index ", str3.find("you"))

# Trim white space from right and left
# also lstrip and rstrip
print("    Hello    ".strip())

# Convert a list into a string and separate with
# spaces
print(" ".join(["Some", "Words"]))

# Convert string into a list with a defined separator
# or delimiter
print("A, string".split(", "))

# Formatted output with f-string
int1 = int2 = 5
print(f'{int1} + {int2} = {int1 + int2}')

# To lower and upper case
print("A String".lower())
print("A String".upper())

# Is letter or number
print("abc123".isalnum())

# Is characters
print("abc".isalpha())

# Is numbers
print("abc".isdigit())

# ----- LISTS -----
# Lists can contain mutable pieces of data of
# varying data types or even functions
l1 = [1, 3.14, "Derek", True]

# Get length
print("Length ", len(l1))

# Get value at index
print("1st", l1[0])
print("Last", l1[-1])

# Change value
l1[0] = 2

# Change multiple values
l1[2:4] = ["Bob", False]

# Insert at index without deleting
# Also l1.insert(2, "Paul")
l1[2:2] = ["Paul", 9]

# Add to end (Also l1.extend([5, 6]))
l2 = l1 + ["Egg", 4]

# Remove a value
l2.remove("Paul")

# Remove at index
l2.pop(0)
print("l2", l2)

# Add to beginning (Also l1.append([5, 6]))
l2 = ["Egg", 4] + l1

# Multidimensional list
l3 = [[1, 2], [3, 4]]
print("[1, 1]", l3[1][1])

# Does value exist
print("1 Exists", (1 in l1))

# Min & Max
print("Min ", min([1, 2, 3]))
print("Max ", max([1, 2, 3]))

# Slice out parts
print("1st 2", l1[0:2])
print("Every Other ", l1[0:-1:2])
print("Reverse ", l1[::-1])

# ----- LOOPS -----
# While : Execute while condition is True
w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1

w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        w2 += 1
        # Skips to the next iteration of the loop
        continue
    w2 += 1

# Cycle through list
l4 = [1, 3.14, "Derek", True]
while len(l4):
    print(l4.pop(0))

# For Loop
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
# end="" eliminates newline
for x in range(0, 10):
    print(x, ' ', end="")
print('\n')

# Cycle through list
l4 = [1, 3.14, "Derek", True]
for x in l4:
    print(x)

# You can also define a list of numbers to
# cycle through
for x in [2, 4, 6]:
    print(x)

# You can double up for loops to cycle through lists
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

# ----- ITERATORS -----
# You can pass an object to iter() which returns
# an iterator which allows you to cycle
l5 = [6, 9, 12]
itr = iter(l5)
print(next(itr))  # Grab next value

# ----- RANGES -----
# The range() function creates integer iterables
print(list(range(0, 5)))

# You can define step
print(list(range(0, 10, 2)))

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# ----- TUPLES -----
# Tuples are just like lists except they are
# immutable
t1 = (1, 3.14, "Derek", False)

# Get length
print("Length ", len(t1))

# Get value / values
print("1st", t1[0])
print("Last", t1[-1])
print("1st 2", t1[0:2])
print("Every Other ", t1[0:-1:2])
print("Reverse ", t1[::-1])

# Everything you can do with lists you can do with
# tuples as long as you don't change values

# ----- DICTIONARIES -----
# Dictionaries are lists of key / value pairs
# Keys and values can use any data type
# Duplicate keys aren't allowed
heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne"
}

villains = dict([
    ("Lex Luthor", "Lex Luthor"),
    ("Loki", "Loki")
])

print("Length", len(heroes))

# Get value by key
# Also heroes.get("Superman")
print(heroes["Superman"])

# Add more
heroes["Flash"] = "Barry Allan"

# Change a value
heroes["Flash"] = "Barry Allen"

# Get list of tuples
print(list(heroes.items()))

# Get list of keys and values
print(list(heroes.keys()))
print(list(heroes.values()))

# Delete
del heroes["Flash"]

# Remove a key and return it
print(heroes.pop("Batman"))

# Search for key
print("Superman" in heroes)

# Cycle through a dictionary
for k in heroes:
    print(k)

for v in heroes.values():
    print(v)

# Formatted print with dictionary mapping
d1 = {"name": "Bread", "price": .88}
print("%(name)s costs $%(price).2f" % d1)

# ----- SETS -----
# Sets are lists that are unordered, unique
# and while values can change those values
# must be immutable
s1 = set(["Derek", 1])

s2 = {"Paul", 1}

# Size
print("Length", len(s2))

# Join sets
s3 = s1 | s2
print(s3)

# Add value
s3.add("Doug")

# Remove value
s3.discard("Derek")

# Remove random value
print("Random", s3.pop())

# Add values in s2 to s3
s3 |= s2

# Return common values (You can include multiple
# sets as attributes)
print(s1.intersection(s2))

# All unique values
print(s1.symmetric_difference(s2))

# Values in s1 but not in s2
print(s1.difference(s2))

# Clear values
s3.clear()

# Frozen sets can't be edited
s4 = frozenset(["Paul", 7])


# ----- FUNCTIONS -----
# Functions provide code reuse, organization
# and much more
# Add 2 values using 1 as default
# You can define the data type using function
# annotations
def get_sum(num1: int = 1, num2: int = 1):
    return num1 + num2


print(get_sum(5, 4))


# Accept multiple values
def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(get_sum2(1, 2, 3, 4))


# Return multiple values
def next_2(num):
    return num + 1, num + 2


i1, i2 = next_2(5)
print(i1, i2)


# A function that makes a function that
# multiplies by the given value
def mult_by(num):
    # You can create anonymous (unnamed functions)
    # with lambda
    return lambda x: x * num


print("3 * 5 =", (mult_by(3)(5)))


# Pass a function to a function
def mult_list(list, func):
    for x in list:
        print(func(x))


mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)

# Create list of functions
power_list = [lambda x: x ** 2,
              lambda x: x ** 3,
              lambda x: x ** 4]

# ----- MAP -----
# Map is used to execute a function on a list
one_to_4 = range(1, 5)
times2 = lambda x: x * 2
print(list(map(times2, one_to_4)))

# ----- FILTER -----
# Filter selects items based on a function
# Print out the even values from a list
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# ----- REDUCE -----
# Reduce receives a list and returns a single
# result
# Add up the values in a list
print(reduce((lambda x, y: x + y), range(1, 6)))

# ----- EXCEPTION HANDLING -----
# You can handle errors that would otherwise
# crash your program
# By giving the while a value of True it will
# cycle until a break is reached
while True:

    # If we expect an error can occur surround
    # potential error with try
    try:
        number = int(input("Please enter a number : "))
        break

    # The code in the except block provides
    # an error message to set things right
    # We can either target a specific error
    # like ValueError
    except ValueError:
        print("You didn't enter a number")

    # We can target all other errors with a
    # default
    except:
        print("An unknown error occurred")

print("Thank you for entering a number")

# ----- FILE IO -----
# We can save and read data from files
# We start the code with with which guarantees
# the file will be closed if the program crashes
# mode w overwrites file
# mode a appends
with open("mydata.txt", mode="w", encoding="utf-8") \
        as myFile:
    # You can write to the file with write
    # It doesn't add a newline
    myFile.write("Some random text\nMore random text\nAnd some more")

# Open a file for reading
with open("mydata.txt", encoding="utf-8") as myFile:
    # Use read() to get everything at once
    print(myFile.read())

# Find out if the file is closed
print(myFile.closed)


# ----- CLASSES OBJECTS -----
# Real world objects have
# attributes : height, weight
# capabilities : run, eat

# Classes are blueprints for creating objects
class Square:
    # init is used to set values for each Square
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is the getter
    # self is used to refer to an object that
    # we don't possess a name for
    @property
    def height(self):
        print("Retrieving the height")

        # Put a __ before this private field
        return self.__height

    # This is the setter
    @height.setter
    def height(self, value):

        # We protect the height from receiving
        # a bad value
        if value.isdigit():

            # Put a __ before this private field
            self.__height = value
        else:
            print("Please only enter numbers for height")

    # This is the getter
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def get_area(self):
        return int(self.__width) * int(self.__height)


# Create a Square object
square = Square()
square.height = "10"
square.width = "10"
print("Area", square.get_area())


# ----- INHERITANCE & POLYMORPHISM-----
# When a class inherits from another it gets all
# its fields and methods and can change as needed
class Animal:
    def __init__(self, name="unknown", weight=0):
        self.__name = name
        self.__weight = weight

    @property
    def name(self, name):
        self.__name = name

    def make_noise(self):
        return "Grrrrr"

    # Used to cast to a string type
    def __str__(self):
        return "{} is a {} and says {}".format(self.__name, type(self).__name__, self.make_noise())

    # Magic methods are used for operator
    # overloading
    # Here I'll define how to evaluate greater
    # than between 2 Animal objects
    def __gt__(self, animal2):
        if self.__weight > animal2.__weight:
            return True
        else:
            return False

    # Other Magic Methods
    # __eq__ : Equal
    # __ne__ : Not Equal
    # __lt__ : Less Than
    # __gt__ : Greater Than
    # __le__ : Less Than or Equal
    # __ge__ : Greater Than or Equal
    # __add__ : Addition
    # __sub__ : Subtraction
    # __mul__ : Multiplication
    # __div__ : Division
    # __mod__ : Modulus

# inehrit animal
class Dog(Animal):
    #constructor
    def __init__(self, name="unknown", owner="unknown", weight=0):
        # pass value to the parent class
        Animal.__init__(self, name, weight)
        self.__owner = owner
        #super allow to call the main function
    def __str__(self):
        return super().__str__() + "and is owned by " + \
            self.__owner

animal = Animal("Spot", 100)
print(animal)
dog = Dog("Bowser", "Bob", 150)
print(dog)
print(animal > dog)



