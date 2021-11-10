"""
ECE606, F'21, Assignment 2, Problem 4
Skeleton solution file.
"""

import math

"""
You are not allowed to import anything else. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""
#Took help from Subham biswajit Bal on BST and its construction
# and https://www.geeksforgeeks.org/level-order-tree-traversal/



class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def buildbst(s):
    nodes = []
    for element in s:
        nodes.append(element)
    nodes.sort()
    root = get_root(nodes)
    return traversal(root)


def traversal(root):

    bst = []
    if root is None:
        return
    q = []
    q.append(root)

#    for i in range(len(q)):
    i = 0
    while(len(q)):
        bst.append(q[0].key)
        node = q.pop(0)

        if node.left is not None:
            # q[2*i+1] = node.left
           q.append(node.left)
        if node.right is not None:
        #    q[2*i+2] = node.right
           q.append(node.right)

    return bst

def get_root(nodes):
    if not nodes:
        return None
    mid = (len(nodes)) // 2 #get midpoint
    root = Node(node s[mid]) #making mid the root  of the list of nodes
    root.right = get_root(nodes[mid + 1:]) #right subtree
    root.left = get_root(nodes[:mid]) #left subtree
    return root

