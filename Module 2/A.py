# Copyright 2022 Fe-Ti aka Kravchenko
from sys import stdin

from sys import setrecursionlimit
setrecursionlimit(2**30)
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

def is_number(string):
    string = string.strip()
    for i in string:
        if i != '-' and not i.isdigit:
            return False
    return True

class TreeNode: # Just a node with some functions
    left = PLACEHOLDER
    right = PLACEHOLDER
    parent = PLACEHOLDER
    key = None
    value = None

    def __init__(self, key, value, parent = PLACEHOLDER):
        self.key = key
        self.value = value
        self.parent = parent

    def is_root(self):
        if self.parent == PLACEHOLDER:
            return True
        return False

    def is_left(self):
        if not self.is_root():
            if self.parent.left == self:
                return True
            return False
        return True

    def is_right(self):
        if not self.is_root():
            if self.parent.right == self:
                return True
            return False
        return True

    def is_in_right_branch(self):
        if (self.is_right() and self.parent.is_right()):
            return True
        return False

    def is_in_left_branch(self):
        if (self.is_left() and self.parent.is_left()):
            return True
        return False

    def __str__(self):
        if self.is_root():
            return f"[{self.key} {self.value}]" # ch:{[self.left,self.right]}]"
        return f"[{self.key} {self.value} {self.parent.key}]" # ch:{[self.left,self.right]}]"

    def __repr__(self): # For debugging purposes
        return f"{self.key}"


class Frontend:
    #               .-.___.-.
    #               |       |
    #               | /\ /\ |\
    #               | \/ \/ | \
    #               |   V   |  \
    #                \_____/    \
    #                  \         \_
    #                   \_         "__
    #                     \  _  .___-"
    #                     /_/ |_\
    #   Hedwig, the white owl: I've seen some [code]...
    root = PLACEHOLDER

    def __init__(self):
        pass

    def add_node(self, node, key, value):
        if key == node.key:
            self.splay(node)
            raise Exception(ERROR_MSG)
        if key < node.key:
            if node.left == PLACEHOLDER:
                node.left = TreeNode(key, value, node)
                self.splay(node.left)
            else:
                self.add_node(node.left, key, value)
        else:
            if node.right == PLACEHOLDER:
                node.right = TreeNode(key, value, node)
                self.splay(node.right)
            else:
                self.add_node(node.right, key, value)

    def set_node(self, node, key, value):
        if key == node.key:
            node.value = value
            self.splay(node)
        elif key < node.key:
            if node.left == PLACEHOLDER:
                self.splay(node)
                raise Exception(ERROR_MSG)
            else:
                self.set_node(node.left, key, value)
        else:
            if node.right == PLACEHOLDER:
                self.splay(node)
                raise Exception(ERROR_MSG)
            else:
                self.set_node(node.right, key, value)

    def del_node(self, node, key):
        if key == node.key:
            if node.is_root() and node.left == PLACEHOLDER and node.right == PLACEHOLDER:
                self.root = PLACEHOLDER
            else:
                self.splay(node)
                if node.left != PLACEHOLDER:
                    node.left.parent = PLACEHOLDER
                else:
                    self.root = node.right
                    node.right.parent = PLACEHOLDER
                    del node
                    return
                if node.right != PLACEHOLDER:
                    node.right.parent = PLACEHOLDER
                else:
                    self.root = node.left
                    node.left.parent = PLACEHOLDER
                    del node
                    return
                successor, is_from_right_st = self.get_successor(node, 0)
                self.splay(successor)
                if not is_from_right_st:
                    if node.right != PLACEHOLDER:
                        node.right.parent = successor
                    successor.right = node.right
            del node
        elif key < node.key:
            if node.left == PLACEHOLDER:
                self.splay(node)
                raise Exception(ERROR_MSG)
            else:
                self.del_node(node.left, key)
        else:
            if node.right == PLACEHOLDER:
                self.splay(node)
                raise Exception(ERROR_MSG)
            else:
                self.del_node(node.right, key)

    def get_successor(self, node, recursion_flag):
        if recursion_flag == 0:
            if node.left == PLACEHOLDER:
                return (node.right, True)
            else:
                return self.get_successor(node.left, 1)
        else:
            if node.right == PLACEHOLDER:
                return (node, False)
            else:
                return self.get_successor(node.right, 1)

    def find(self, node, key):
        # The function returns a tuple (status, value)
        # If status is 0 then the value is None
        if key == node.key:
            self.splay(node)
            return (1,  node.value)
        elif key < node.key:
            if node.left == PLACEHOLDER:
                self.splay(node)
                return (0,None)
            else:
                return self.find(node.left, key)
        else:
            if node.right == PLACEHOLDER:
                self.splay(node)
                return (0,None)
            else:
                return self.find(node.right, key)

    def get_max_key(self, node):
        if node.right == PLACEHOLDER:
            self.splay(node)
            return (node.key, node.value)
        else:
            return self.get_max_key(node.right)

    def get_min_key(self, node):
        if node.left == PLACEHOLDER:
            self.splay(node)
            return (node.key, node.value)
        else:
            return self.get_min_key(node.left)

    def splay(self, node):
        while not node.is_root():
            if node.parent.is_root():
                # ~ print("Zigging")
                self.Zig(node)
            elif node.is_in_left_branch() or node.is_in_right_branch():
                # ~ print("ZigZigging")
                self.ZigZig(node)
            else:
                # ~ print("ZigZagging")
                self.ZigZag(node)
        self.root = node

    def Zig(self, node):
        l = node.left
        r = node.right
        p = node.parent
        g = node.parent.parent
        if g != PLACEHOLDER:
            if p.is_left():
                g.left = node
            else:
                g.right = node
        if node.is_left():
            # ~ print(f"{node} is left")
            node.right = p
            node.right.parent = node
            node.right.left = r
            if r != PLACEHOLDER:
                node.right.left.parent = p
        else:
            # ~ print(f"{node} is right")
            node.left = p
            node.left.parent = node
            node.left.right = l
            if l != PLACEHOLDER:
                node.left.right.parent = p

        node.parent = g

    def ZigZig(self, node): # Lazy programmer's decomposition
        self.Zig(node.parent)
        self.Zig(node)

    def ZigZag(self, node):
        self.Zig(node)
        self.Zig(node)

    def recursive_print(self, root_node):
        depth = self.get_tree_depth(root_node)
        for layer in range(depth):
            self.print_layer(root_node, 0, layer)   # print layer and go back
            print()                                 # then print newline and repeat

    def get_tree_depth(self, node, curr_depth = 0, max_depth = 0):
        if curr_depth > max_depth:
            max_depth = curr_depth
        if not (type(node) is str):
            max_depth = self.get_tree_depth(node.left, curr_depth + 1, max_depth)
            max_depth = self.get_tree_depth(node.right, curr_depth + 1, max_depth)
        return max_depth

    def print_layer(self, node, curr_depth, desired_layer):
        if curr_depth == desired_layer:
            print(node, end=' ')
        else:
            if node == PLACEHOLDER:
                print((PLACEHOLDER+" ")*(2**(desired_layer - curr_depth)), end='')
            else:
                self.print_layer(node.left, curr_depth + 1, desired_layer)
                self.print_layer(node.right, curr_depth + 1, desired_layer)

    def execute(self, cmd):
        # Execute commands from input strings
        if self.root != PLACEHOLDER:
            # ~ print(cmd)
            try:
                if (cmd[0] == ADD_CMD and len(cmd) == 3):
                    if is_number(cmd[1]):
                        self.add_node(self.root, int(cmd[1]), cmd[2])
                    else:
                        raise Exception(ERROR_MSG)
                elif (cmd[0] == SET_CMD and len(cmd) == 3):
                    if is_number(cmd[1]):
                        self.set_node(self.root, int(cmd[1]), cmd[2])
                    else:
                        raise Exception(ERROR_MSG)
                elif (cmd[0] == DEL_CMD and len(cmd) == 2):
                    if is_number(cmd[1]):
                        self.del_node(self.root, int(cmd[1]))
                    else:
                        raise Exception(ERROR_MSG)
                elif (cmd[0] == SEARCH_CMD and len(cmd) == 2):
                    if is_number(cmd[1]):
                        k,v = self.find(self.root, int(cmd[1])) # find returns a tuple
                        if v:
                            print(k, v)
                        else:
                            print(k)
                    else:
                        raise Exception(ERROR_MSG)
                elif (cmd[0] == MIN_CMD and len(cmd) == 1):
                    k,v = self.get_min_key(self.root)
                    print(k, v)
                elif (cmd[0] == MAX_CMD and len(cmd) == 1):
                    k,v = self.get_max_key(self.root)
                    print(k, v)
                elif (cmd[0] == PRINT_CMD and len(cmd) == 1):
                    self.recursive_print(self.root)
                elif (cmd[0] == ADD_CMD and len(cmd) == 2): # here is a kludge for passing tests with 'add 66 ' and 'set 5 '
                    if is_number(cmd[1]):
                        self.add_node(self.root, int(cmd[1]), '')
                    else:
                        raise Exception(ERROR_MSG)
                elif (cmd[0] == SET_CMD and len(cmd) == 2):
                    if is_number(cmd[1]):
                        self.set_node(self.root, int(cmd[1]), '')
                    else:
                        raise Exception(ERROR_MSG)
                else:
                    raise Exception(ERROR_MSG)
            except Exception as error_msg:
                print(error_msg)
        else:
            if (cmd[0] == ADD_CMD and len(cmd) == 3):
                if is_number(cmd[1]):
                    self.root = TreeNode(int(cmd[1]), cmd[2])
                else:
                    print(ERROR_MSG)
            elif (cmd[0] == PRINT_CMD and len(cmd) == 1):
                print(self.root)
            elif (cmd[0] == SEARCH_CMD and len(cmd) == 2):
                print('0')
            elif (cmd[0] == ADD_CMD and len(cmd) == 2): # here is a kludge for passing tests with 'add 66 ' and 'set 5 '
                if is_number(cmd[1]):
                    self.add_node(self.root, int(cmd[1]), '')
                else:
                    print (ERROR_MSG)
            else:
                print(ERROR_MSG)

tree = Frontend()
for i in stdin:
    if i and not i.isspace():
        cmd = i.split()
        tree.execute(cmd)
"""
add 8 10
add
add 4 14
add 7 15
add 9 11
add 3 13
add 5 16
add 88 1
add 11 2
add 6 18
search 11
search 66
search 8
search 8
search 5
search 88
search 2
add 66 
search 10
search 3
set 5 
add 0 
search 66
search 0
search 5
print
"""
