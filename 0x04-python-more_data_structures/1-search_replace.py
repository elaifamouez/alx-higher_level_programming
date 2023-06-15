#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        new = []
        for w in my_list:
            if w is not search:
                new.append(w)
            else:
                new.append(replace)
        return new
