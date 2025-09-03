#!/usr/bin/python3
for i in range(100):
    if i != 99:
        print("{:02}".format(i), end=", ")  # autopads it with a 0
    else:
        print("{:02}".format(i))
