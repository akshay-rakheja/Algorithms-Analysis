"""
ECE606, F'21, Assignment 8, Problem 2(b)
Skeleton solution file.
"""
import math

"""
You are not allowed to import anything else. You are
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""

def getEdges(G):
    edges = set()
    for i in range(0, len(G)):
        for j in range(0, len(G[i])):
            if (G[i][j], i) not in edges:
                edges.add((G[i][j], i))
    return edges

def avgsatisfied(G, k):
    edges = getEdges(G)
    print(edges)
    counter = 0
    runningavg = 0
    print(len(edges))
    # satisfied = 0
    while(counter<5000):
        satisfied = 0
        for edge in edges:
            edge = list(edge)

            u = ((counter) ** edge[0]) % (k+1)
            v = ((counter) ** edge[1]) % (k+1)

            if u != v:
                satisfied = satisfied + 1

        runningavg = runningavg + satisfied
        counter = counter + 1

    print(runningavg/5000)
    return (runningavg/5000)

    """
    You need to implement this method. See the handout for its specs.
    NOTE: you should *NOT* modify the argument G. You should assume
          "read-only" access to it only. Make a copy of it first if you
          feel you need to modify it.
    """
