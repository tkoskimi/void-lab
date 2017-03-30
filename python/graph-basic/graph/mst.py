"""
This module contains algorithms that solve a minimum spanning tree (MST) problem.

Parameters
----------
None

Returns
-------
None

Long Description
----------------
Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of
the least possible weight that connects any two trees in the forest. It is a
greedy algorithm in graph theory as it finds a minimum spanning tree for a
connected weighted graph adding increasing cost arcs at each step. This
means it finds a subset of the edges that forms a tree that includes every
vertex, where the total weight of all the edges in the tree is minimized.
[Wikipedia]

Todos
-----
1. The implementation is tightly bound to the implementation of the JSON graph

Known Issues
------------
1. It does not return a forest for the non-connected graphs
2. It does not understand directed graphs, but handles them similarly as undirected ones
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from .UnionFind import UnionFind

def kruskal(graph):
    '''Returns a minimum spannig tree for the given graph.'''
    unions = UnionFind()
    for x in graph['nodes']:
        unions[x['id']]
    edges = sorted(graph['edges'], key=lambda x: x['metadata']['value'])
    F = [] # List of edges
    for edge in edges:
        u = edge['source']
        v = edge['target']
        if unions[u] is not unions[v]:
            unions.union(u, v)
            F.append(edge)
    return F
