# Copyright 2022 Fe-Ti aka Kravchenko
from sys import stdin
from math import floor

# Splay Tree. A 30% copy from Binary Tree.
# There can be some inconsistency in this piece of s... pardon, code.

PLACEHOLDER = '_' # Here could something like nullptr or pointer to empty vertex

"""
Command syntax reference:

add KEY VALUE   - adds a node with KEY and VALUE, raises error when KEY exists
set KEY VALUE   - sets new VALUE to the KEY, raises error when KEY doesn't exist
del KEY         - deletes a node with KEY
search KEY      - returns a tuple (1, VALUE) or (0, None)
print           - prints the whole tree
min             - finds min
max             - finds max
"""


# Some constants
ERROR_MSG = 'error'
ADD_CMD = 'add'
SET_CMD = 'set'
DEL_CMD = 'delete'
SEARCH_CMD = 'search'
PRINT_CMD = 'print'
MIN_CMD = 'min'
MAX_CMD = 'max'
EXTRACT_CMD = 'extract'

class HeapNode:
    """
    Just a hashable node (:
    """
    def __init__(self, k, v):
        self.k = k
        self.v = v
    def __hash__(self):
        return k.__hash__()

class MinHeap:
    """
    Here the most part of magic happens.
    """
    def __init__(self):
        self.array = list()
        # According to https://wiki.python.org/moin/TimeComplexity
        # dict has average complexity O(1) for accessing single element.
        self.hyper_transport = dict()

    def __get_left__(self, node_index):
        return 2 * node_index + 1

    def __get_right__(self, node_index):
        return 2 * node_index + 2

    def __get_parent__(self, node_index):
        return floor((i - 1) / 2)

    def __sift_up__(self, node_index):
        
    def __sift_down__(self, node_index):
        

    def add_node(self, k, v):
        new_node = HeapNode
        if k in self.hyper_transport:
            raise Exception(ERROR_MSG) # Let's say elements are unique
        # If key is unique, then append the element to the array
        self.array.append(new_node)
        self.__sift_up__(-1) #
        
        self.hyper_transport[k](new_node) # Err... Not the most effective way
        
        
    def set_node(self, k, v):
    def del_node(self, k):
    def search_node(self, k):
    def get_min_node(self):
    def get_max_node(self):
        
    def heapy_print(self):
        
    def extract(self):
        

class Frontend:
    def add_node(self, k, v):
    def set_node(self, k, v):
    def del_node(self, k):
    def search_node(self, k):
    def get_min_node(self):
    def get_max_node(self):
        
    def heapy_print(self):
        
    def extract(self):
        
    def __init__(self):
        self.Heap
    def execute(self, cmd):
        # Execute commands from input strings
        try:
            if (cmd[0] == ADD_CMD and len(cmd) == 3):
                if cmd[1].isdigit():
                    self.add_node(int(cmd[1]), cmd[2])
                else:
                    raise Exception(ERROR_MSG)
            elif (cmd[0] == SET_CMD and len(cmd) == 3):
                if cmd[1].isdigit():
                    self.set_node(int(cmd[1]), cmd[2])
                else:
                    raise Exception(ERROR_MSG)
            elif (cmd[0] == DEL_CMD and len(cmd) == 2):
                if cmd[1].isdigit():
                    self.del_node(int(cmd[1]))
                else:
                    raise Exception(ERROR_MSG)
            elif (cmd[0] == SEARCH_CMD and len(cmd) == 2):
                if cmd[1].isdigit():
                    k, i, v = self.search(int(cmd[1])) # find returns a tuple
                    if v:
                        print(k, v)
                    else:
                        print(k)
                else:
                    raise Exception(ERROR_MSG)
            elif (cmd[0] == MIN_CMD and len(cmd) == 1):
                k,v = self.get_min_key()
                print(k, v)
            elif (cmd[0] == MAX_CMD and len(cmd) == 1):
                k,v = self.get_max_key()
                print(k, v)
            elif (cmd[0] == PRINT_CMD and len(cmd) == 1):
                self.heapy_print()
            elif (cmd[0] == EXTRACT_CMD and len(cmd) == 1):
                self.extract()
            else:
                raise Exception(ERROR_MSG)
        except Exception as error_msg:
            print(error_msg)

tree = Frontend()
for i in stdin:
    if i and not i.isspace():
        cmd = i.split()
        tree.execute(cmd)
