"""
ECE606, F'21, Assignment 4, Problem 1
Skeleton solution file.
"""

"""
You are not allowed to import anything. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""

# G = [[2, 3, 4], [2, 3], [0, 1], [0, 1, 4], [0, 3]]
# T = [[2, 3], [3], [0], [0, 1, 4], [3]]


def anotherst(G, T):
    num_vertices = len(G)
    # visited = set()  # Set to keep track of visited nodes.

    e_G = get_edges(G)
    # e_T = get_edges(T)
    t_prime = []
    real_edges = rm_repeats(e_G)
    num_edges = len(real_edges)
    if num_edges <= num_vertices - 1:
        return None
    else:
        for e in G:  #foreach list of edges for a vertex
            # print(e[0])
            t_prime.append([e[0]])  # Take the first element/node from a sorted adjacency list for each vertex and append it
                                    # as a list to new spanning tree. Since we take only one edge from each vertex (spanning tree)
                                    # it results in a spanning tree with |V|-1 edges. The main reason for this approach is because
                                    # the adjacency list is assumed to be sorted as is assumed in the question.
    return t_prime


def rm_repeats(edges):
    real_edges = []
    for i in edges:
        if i not in real_edges:
            real_edges.append(i)
        if (i[1], i[0]) in real_edges:  # if edge exists in reverse form delete it
            real_edges.remove(i)
    return real_edges

def get_edges(G):
    edges = []
    for i, v in enumerate(G):
        for e in v:
            edges.append((i, e))
    return edges


# anotherst(G, T)

"""
    You need to implement this method. See the handout for its specs.
"""

"""
A Python program to demonstrate the adjacency
list representation of the graph
"""

