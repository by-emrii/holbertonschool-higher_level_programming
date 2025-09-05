#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for x in range(len(names)):
        if (names[x][0] != '_' or names[x][1] != '_'):
            print(names[x])
