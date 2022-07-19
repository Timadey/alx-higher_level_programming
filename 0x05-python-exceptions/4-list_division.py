#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while (i in range(list_length)):
        try:
            result = my_list_1[i] / my_list_2[i]
            if result >= 0:
                new_list.append(result)
            else:
                new_list.append(0)
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            i += 1
    return(new_list)
