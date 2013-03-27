.. erikgraph documentation master file, created by
   sphinx-quickstart on Wed Mar 27 12:38:02 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to erikgraph's documentation!
=====================================

Introduction
=============

A Company asked me to write a class that implements the following specification:

    A class Graph representing an undirected graph structure with weighted edges
    (i.e. a set of vertices with undirected edges connecting pairs of vertices, where each edge has a nonnegative weight).
    In addition to methods for adding and removing vertices, class Graph should define (at minimum) the following instance
    methods

    def neighbor_vertices(self, a):
    """
    Return a sequence of vertices that are neighbors of vertex a (e.g. are joined by a single edge). Raise
    an exception if a is not in the graph.
    """
    pass

    def neighbors(self, a, b):
        """
        Return True if vertices a and b are joined by an edge, and False otherwise. Raise an exception if
        a or b are not in the graph.
        """
        pass

    def minimum_weight_path(self, a, b):
        """
        Return a 2-tuple comprising the minimum-weight path connecting vertices a and b, and the associated minimum weight.
        Return None if no such path exists. Raise an exception if a or b are not in the graph.
        """
        pass

    def minimum_edge_path(self, a, b):
        """
        Return a 2-tuple comprising the minimum-edge path connecting vertices a and b, and the associated minimum number
        of edges (e.g. a path comprising 3 edges is shorter than a path comprising 4 edges, regardless of the edge weights).
        Return None if no such path exists. Raise an exception if a or b are not in the graph.
        """
        pass

This is a classic graph problem, and can be solved using Dijkstra's algorithm.  My implementation runs in O(|V| + |E|)
as all vertices and edges might have to be traversed.

Install
=========

.. code-block:: bash

    $ pip install erikgraph

Run Doctests
=============

From the command line, type:

.. code-block:: bash

    $ python -m doctest /path/to/erikgraph/__init__.py -v

or from an interactive session

.. code-block:: python

    import doctest
    import erikgraph
    doctest.testmod(erikgraph,verbose=True)

    Trying:
    G = Graph(['a'],[('a','b',2),('b','c',1)])
    Expecting nothing
    ok
    Trying:
        'b' in G.data
    Expecting:
        True
    ok
    ...
    ...
    10 items passed all tests:
       4 tests in __init__.Graph.__init__
       3 tests in __init__.Graph.add_edge
       4 tests in __init__.Graph.add_vertex
       4 tests in __init__.Graph.delete_edge
       5 tests in __init__.Graph.delete_vertex
       3 tests in __init__.Graph.get_edge_weight
       9 tests in __init__.Graph.minimum_edge_path
       9 tests in __init__.Graph.minimum_weight_path
       4 tests in __init__.Graph.neighbor_vertices
       4 tests in __init__.Graph.neighbors
    49 tests in 15 items.
    49 passed and 0 failed.
    Test passed.



Using erikgraph
===============

Shortest Path
+++++++++++++

To find the shortest path and its distance, use  :py:meth:`~erikgraph.Graph.minimum_weight_path`.

:py:meth:`~erikgraph.Graph.minimum_edge_path` will ignore edge weight values, and find the path between two nodes
that utilizes the fewest number of total edges.

.. code-block:: python

    from erikgraph import Graph
    G = Graph(edges=[
            ('a','c',10),('b','c',2),('c','f',20),
            ('a','d',1),('d','e',5),('e','f',16),
            ('e','h',1),('h','f',4),('d','h',7),
            ('d','g',2)
        ]
    )
    print G.minimum_weight_path('a','f')
    (11, ['a', 'd', 'e', 'h', 'f'])
    print G.minimum_edge_path('a','f')
    (2, ['a', 'c', 'f']


See the method's API for details, which has plenty of examples.

API
++++

.. automodule:: erikgraph
    :members:
    :undoc-members:

.. toctree::
   :maxdepth: 2




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

