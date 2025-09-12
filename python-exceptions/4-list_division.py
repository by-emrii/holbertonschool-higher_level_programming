#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        result = 0
        try:
            if (isinstance(my_list_1[i], (int, float)) and
                    isinstance(my_list_2[i], (int, float))):
                result = my_list_1[i] / my_list_2[i]
            else:
                print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)
    return result_list
