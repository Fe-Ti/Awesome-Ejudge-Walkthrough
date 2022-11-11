from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(2**30)
# ~ import gc
# ~ gc.disable()

PROJECT_NAME = 0;
#'uuid:9f781e1d-30a8-46a2-a55c-2fb804bb4a8f'
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.children = set()
        self.parents = set()
        # ~ if children_keys:
            # ~ for child in children_keys:
                # ~ self.inserted_keys.add(child)
                # ~ self.children.add(TreeNode(child))

    # ~ def add_children(self, parent_key, children_keys):
        # ~ for child in children_keys:
            # ~ self.inserted_keys.add(child)
            # ~ self.children.append(TreeNode(child))


class VulnerableDepCollector:
    rec_level = 0
    def __init__(self, vulnerable_libs, dep_tree, libs, project_deps):
        self.vulnerable_libs = vulnerable_libs
        self.dep_tree = dep_tree
        self.libs = libs
        self.project_deps = project_deps
        self.paths = set()

    def search_for_vulnerabilities(self):
        c = 1
        for vl in self.vulnerable_libs:
            vl
            #print(f"\033[1A{c/len(self.vulnerable_libs)*100:1f}",'%')
            self.check_node(vl,'', set())
            c+=1

    def check_node(self, node, path_as_str, path_as_set):
        if node.key == PROJECT_NAME:
            self.paths.add(path_as_str)
            return
        if not node.parents:
            return
        if path_as_str:
            path_as_str = node.key + " " + path_as_str
        else:
            path_as_str = node.key
        path_as_set.add(node.key)
        for parent in node.parents:
            #print(path_as_str)
            if parent.key not in path_as_set:
                self.check_node(parent, path_as_str, path_as_set)
        path_as_set.remove(node.key)
        return

    def print_paths(self):
        string = ''
        for path in self.paths:
            string += path + '\n'
        print(string, end='')

# Reading from stdin as it was a file
vulnerable_lib_keys = set(input().split())
project_deps = set(input().split())

dep_tree = TreeNode(PROJECT_NAME)
libs = {PROJECT_NAME : dep_tree}
for key in project_deps:
    lib = TreeNode(key)
    dep_tree.children.add(lib)
    lib.parents.add(dep_tree)
    libs[key] = lib

vulnerable_libs = set()

for vkey in vulnerable_lib_keys:
    if vkey in libs:
        vlib = libs[vkey]
    else:
        vlib = TreeNode(vkey)
        libs[vkey] = vlib
    vulnerable_libs.add(vlib)

def parse_stdin_str(string):
    global PROJECT_NAME, project_deps, dep_tree, libs
    string = string.split()
    #print('|',string,'|')
    if len(string) > 1:
        lib_key = string[0]
        dep_keys = set(string[1:])
        if lib_key in libs:
            lib = libs[lib_key]
        else:
            lib = TreeNode(lib_key)
            libs[lib_key] = lib
        for dep_key in dep_keys:
            if dep_key in libs:
                dep = libs[dep_key]
            else:
                dep = TreeNode(dep_key)
                libs[dep_key] = dep
            lib.children.add(dep)
            dep.parents.add(lib)
    return 0

for line in stdin:
    parse_stdin_str(line)
# ~ somelist = list(map(parse_stdin_str, stdin))
# ~ print(libs)
# ~ dep_tree = {key: val for (key, val) in dep_map}
# ~ dep_tree = dict(dep_map)
# ~ print(dep_tree)
# ~ tp = TreePrinter()

# ~ tp.print_tree(dep_tree, PROJECT_NAME)

vdc = VulnerableDepCollector(vulnerable_libs, dep_tree, libs, project_deps)
# ~ print('vdc initialized')

vdc.search_for_vulnerabilities()

vdc.print_paths()
