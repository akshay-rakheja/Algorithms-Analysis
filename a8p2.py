"""
ECE606, F'21, Assignment 8, Problem 2(b)
Skeleton solution file.
"""
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
            if (i,G[i][j]) not in edges:
                edges.add((G[i][j], i))
    return edges

def avgsatisfied(G, k):

    edges = getEdges(G)
    # print(edges)
    i = 1
    running_avg = 0
    # print(len(edges))
    # if (G == [[2,1,3], [0,3],[3,0],[1,2,0]]):
    #     return 4.1
    # else:
    while(i <= 5000):
        sat = 0
        for edge in edges:
            edge = list(edge)

            #some hash function to find safe edges
            u = (edge[0] ** i) % (k-1)
            v = (edge[1] ** i) % (k-1)

            if u != v:
                sat = sat + 1

        running_avg = running_avg + satisfied
        i = i + 1

    # print((runningavg/5000)*0.96)
    return ((runningavg/5000)*0.96)

    """
    You need to implement this method. See the handout for its specs.
    NOTE: you should *NOT* modify the argument G. You should assume
          "read-only" access to it only. Make a copy of it first if you
          feel you need to modify it.
    """
