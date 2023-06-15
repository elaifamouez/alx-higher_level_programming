#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        return {k: 2 * v for k, v in a_dictionary.items()}
