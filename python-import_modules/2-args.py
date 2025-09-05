#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1  # number of arguments

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    # both ways work
    # i = 1
    # while i <= argc:
    #     print(f"{i}: {sys.argv[i]}")
    #     i += 1

    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"{i}: {arg}")
