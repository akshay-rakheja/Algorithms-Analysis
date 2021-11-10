"""
ECE606, F'21, Assignment 6, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything. You are
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""

# G = [ [[2, 10], [1, 10], [3, 30]], [[0, 10], [3, 20]] , [[3, 20], [0, 10]], [[1, 20], [2, 20], [0, 30]] ]
#
# e1 = [0,3]
# e2 = [3,2]

def init_source(G, source):  #initializing source vertex
    dists = {}
    parents = {}

    for i,v in enumerate(G):
        dists[i] = float('inf')
        parents[i] = None
    dists[source] = 0
    parents[source] = -1
    return dists, parents


def mst_prim(G, source): #returns a mst using prims algorithm

    Done = set()
    Q, p = init_source(G, source) #dictionary with vertices as keys and distances as values
    # print(Q)
    # print(p)
    while len(Q) != 0:
        u = min(Q, key=Q.get) #extract key with min value (distance)
        # print(u)
        Done.add(u)
        for v in G[u]:
            if v[0] not in Done:
                relax(u, v[0], v[1], Q, p)
        Q.pop(u)
    # print(p)

    return [(i,p[i]) for i in p]


def relax(u, v, w, dists, parents): #relaxes the vertex and its edges
    if dists[v] > w:
        dists[v] = w
        parents[v] = u


def hasmst(G, e):
    """
    You need to implement this method. See the handout for its specs.
    NOTE: you should *NOT* modify either of the arguments G, e. You
          have "read-only" access to them only. If you modify them,
          you'll get an automatic 0 on this problem.
    """
    mst_edges = set()

    for i, v in enumerate(G):
        source = i
        mst_edges.update(mst_prim(G,source)) # adds the edges from all possible mst's
    # print(mst_edges)
    if (e[0], e[1]) in mst_edges or (e[1], e[0]) in mst_edges:
        return True
    else:
        return False

# hasmst(G,e1)









