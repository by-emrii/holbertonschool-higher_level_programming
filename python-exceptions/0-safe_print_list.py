#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count = count + 1
    except IndexError:
        pass  # ignore if i goes beyond list length
    print()
    return count
