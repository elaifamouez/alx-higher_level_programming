#!/usr/bin/python3
""" Module to print status code """

import sys

class Magic:
    """ Class to generate instances with a dictionary and size """
    
    def __init__(self):
        """ Initializes the Magic instance """
        self.dic = {}  # Dictionary to store status codes and their counts
        self.size = 0  # Total file size
        
    def init_dic(self):
        """ Initializes the dictionary with default status codes """
        self.dic['200'] = 0
        self.dic['301'] = 0
        self.dic['400'] = 0
        self.dic['401'] = 0
        self.dic['403'] = 0
        self.dic['404'] = 0
        self.dic['405'] = 0
        self.dic['500'] = 0
    
    def add_status_code(self, status):
        """ Adds 1 to the count of the given status code """
        if status in self.dic:
            self.dic[status] += 1
    
    def print_info(self, sig=0, frame=0):
        """ Prints the file size and status code counts """
        print("File size: {:d}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] != 0:
                print("{}: {:d}".format(key, self.dic[key]))

if __name__ == "__main__":
    magic = Magic()  # Create an instance of the Magic class
    magic.init_dic()  # Initialize the dictionary with default status codes
    nlines = 0  # Line counter

    try:
        for line in sys.stdin:
            if nlines % 10 == 0 and nlines != 0:
                magic.print_info()  # Print the status code counts

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                magic.add_status_code(list_line[-2])  # Extract the status code and add it to the count
                magic.size += int(list_line[-1].strip("\n"))  # Add the file size to the total
            except:
                pass
            nlines += 1
    except KeyboardInterrupt:
        magic.print_info()  # Print the final status code counts on keyboard interruption
        raise
    magic.print_info()  # Print the final status code counts
