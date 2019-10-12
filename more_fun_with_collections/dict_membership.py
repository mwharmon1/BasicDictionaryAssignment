"""
Author: Michael Harmon
Date: 10/11/2019
Description: This program will check to see if a value exists within a dictionary.
"""


def in_dict(this_dict, this_value):
    """
    check to see if element is in dictionary
    :param this_dict: dictionary
    :param this_value: value to search for
    :return: true if found, false if not found
    """
    if this_value in this_dict:
        return True
    return False


if __name__ == '__main__':
    my_dict = {'2': 4, '6': 8, '10': 12, '14': 16}
    my_value = '6'
    print(in_dict(my_dict, my_value))