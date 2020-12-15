#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        if type(my_list) is list:
            for x in range(0, len(my_list)):
                print("{:d}".format(my_list[x]))
