class VertexDoesNotExist(Exception): pass

class Graph(object):
    """
    A Minigraph class.  Implements the following specification:

    A class Graph representing an undirected graph structure with weighted edges
    (i.e. a set of vertices with undirected edges connecting pairs of vertices, where each edge has a nonnegative weight).
    In addition to methods for adding and removing vertices, class Graph should define (at minimum) the following instance
    methods

    :property data: A dictionary who's keys are vertices and values are list 2-tuples containing the key's adjacent
        vertices and the weight connecting them.
    """

    data = {}


    def __init__(self,vertices=[],edges=[]):
        """
        :param vertices: A list of vertices to initialize the graph with.
        :param edges: A list of 3-tuple edges and weights to initialize the graph with.

        >>> G = Graph(['a'],[('b','c',2)])
        >>> 'b' in G.data
        True
        >>> 'c' in G.data
        True
        >>> 'd' in G.data
        False
        """
        self.add_vertices(vertices)
        self.add_edges(edges)

    def add_vertices(self,vertices):
        """
        :param vertices: A list of vertices to add to the graph

        >>> G = Graph()
        >>> G.add_vertices(['a','b','c'])
        """
        self.data = dict(map(lambda v: (v,[]), vertices))

    def add_edges(self,edges):
        """
        Adds each edge in :param:`edges` to the list.  Nodes in edges not already in the graph will be added.

        :param edges: A list of 3-tuples that describe edges to add to the graph.  The first two elements are the
            adjacent vertices, and the third is the weight of the edge.

        >>> G = Graph()
        >>> G.add_edges([('a','b',1),('b','c',2)])
        >>> ('c',2) in G.data['b']
        True
        """
        for v1,v2,weight in edges:
            self.data.setdefault(v1,[]).append((v2,weight))
            self.data.setdefault(v2,[]).append((v1,weight))

    def neighbor_vertices(self, a):
        """
        :return: a sequence of vertices that are neighbors of vertex a (e.g. are joined by a single edge).
        :raises: VertexDoesNotExist if a is not in the graph.

        >>> G = Graph(vertices=['a'],edges=[('b','c',1),('a','c',2)])
        >>> G.neighbor_vertices('c')
        ['b', 'a']
        """
        try:
            return [e[0] for e in self.data[a] if e != a]
        except KeyError:
            raise VertexDoesNotExist, 'The vertex {0} does not exist in this graph'.format(a)

    def neighbors(self, a, b):
        """
        :return: True if vertices a and b are joined by an edge, and False otherwise.
        :raises: VertexDoesNotExist if a or b are not in the graph.

        >>> G = Graph(vertices=['a'],edges=[('b','c',1)])
        >>> G.neighbors('a','b')
        False
        >>> G.neighbors('b','c')
        True
        """
        if b not in self.data: raise VertexDoesNotExist, 'The vertex {0} does not exist in this graph'.format(b)
        try:
            return any(( e[0] == b for e in self.data[a] ))
        except KeyError:
            raise VertexDoesNotExist, 'The vertex {0} does not exist in this graph'.format(a)


    def minimum_weight_path(self, a, b):
        """
        :return: a 2-tuple comprising the minimum-weight path connecting vertices a and b, and the associated minimum weight.
            Return None if no such path exists.
        :raises: VertexDoesNotExist if a or b are not in the graph.
        """
        pass

    def minimum_edge_path(self, a, b):
        """
        :return: a 2-tuple comprising the minimum-edge path connecting vertices a and b, and the associated minimum number
            of edges (e.g. a path comprising 3 edges is shorter than a path comprising 4 edges, regardless of the edge weights).
            Return None if no such path exists. Raise an exception if a or b are not in the graph.
        """
        pass