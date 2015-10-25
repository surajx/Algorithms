from random import randint,uniform
import timeit


class Vertex:
    """Representative of a Graph vertex
    Instances of Vertex are expected to have associated with it dynamic
    attributes that feel fit for the context of Graph operation.
    """
    pass

class Edge:
    """Representative of a Graph Edge

    Args:
        u (Vertex): first vertex the edge connects
        v (Vertex): second vertex the edge connects
        w (int)   : weights on the edge.

    Attributes:
        u (Vertex): first vertex the edge connects
        v (Vertex): second vertex the edge connects
        w (int)   : weights on the edge.
    """
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

class Graph:
    """Represents a complete Graph.

    Args:
        n_v (int)            : Number of vertices in the complete Graph
                               (default 10)
        dist_range((int,int)): Distribution range for edge weights.
                               (default (0,1))

    Attributes:
        Adj ([[]]): Adjacency matrix representing the Graph.

    """
    def __init__(self, n_v=10, dist_range=(0,1)):
        """Generates a complete graph with n_v vertices, with each edge
        allocated a random weight uniformly sampled from dist_range.
        Dynamically prepares Verted class for the context.
        """
        self._V = []
        for i in range(n_v):
            v = Vertex()
            v._value = i
            self._V.append(v)
        def getValue(self): return self._value
        Vertex.getValue = getValue
        self._genCompleteGraph(n_v, dist_range)

    def _genCompleteGraph(self, n_v, dist_range):
        """ Populated the Adjacency Matrix with uniformly sampled edge
        weights from dist_range.

        *The method is private and not part of the Graph API*

        Args:
            n_v (int)             : Vertex count.
            dist_range ((int,int)): Distribution range for edge weights.
        """
        self.Adj = []
        self._E = []
        for i in range(n_v):
            self.Adj.append([0]*n_v)
        i,j=0,0
        for e in range(n_v*(n_v -1)/2):
            if i==j:
                j += 1
                i = 0
            e_w = round(uniform(dist_range[0],dist_range[1]), 12)
            self.Adj[i][j] = e_w
            self.Adj[j][i] = e_w
            self._E.append(Edge(self._V[i], self._V[j], e_w))
            i += 1

    def __str__(self):
        """Return the string representation of the Graph"""
        return ''.join([str(y)+'\n' for y in self.Adj])

    def V(self):
        """Return the list of vertices in the Graph"""
        return self._V

    def getAdjOf(self, u):
        """ Return the Adjacent vertices of a given vertex.

        Arg:
            u (Vertex): Given Vertex
        """
        Adj_V = list(self._V)
        del Adj_V[u.getValue()]
        return Adj_V

    def E(self):
        """Returns the list of edges in the Graph"""
        return self._E


"""
Following is the implementation of the Disjoint Set Data Structure
using directed forest and implementing both union by rank and path
compression heuristics.

The data structure is written in such a way as to work with the Dynamic
nature of the Vertex class.
"""
def MAKE_SET(x):
    """Puts the given element into a set of it's own.

    Arg:
        x (Vertex): Given Vertex
    """
    x.p = x
    x.rank = 0

def UNION(x, y):
    """Merges two disjoints sets.

    Args:
        x (Vertex): Given Vertex of Graph
        y (Vertex): Given Vertex of Graph
    """
    _LINK(FIND_SET(x), FIND_SET(y))

def _LINK(x, y):
    """Links two disjoint sets by utilizing the union by rank heuristic.

    *The method is private and not part of the Disjoint set API*

    Args:
        x (Vertex): Given Vertex of Graph
        y (Vertex): Given Vertex of Graph
    """
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank==y.rank:
            y.rank += 1

def FIND_SET(x):
    """Finds the representative of the disjoint set containing
    the given vertex. During the find operation heuristic path
    compression is also applied.

    Arg:
        x (Vertex): the vertex whose disjoint set representative
                    needs to be found.
    """
    if x!=x.p:
        x.p = FIND_SET(x.p)
    return x.p


"""
Quicksort implementation. The implementation can sort objects based on
a key function that accessed the object attribute upon which the given
object list needs to be sorted.
"""
def quicksort(A, key=None):
    """Entry point, sorts the given array in-place

    Args:
        A (Objects|int): array that needs to sorted in-place
        key (function) : a comaprison function that compares the attributes
                         on which the objects in the list needs to be sorted.
                         (defaults to None)
    """
    _quicksort(A, 0, len(A)-1, key)

def _quicksort(A, st_idx, sp_idx, key):
    """Sorts the given array in-place

    Args:
        A (Objects|int): array that needs to sorted in-place
        st_idx (int)   : start index of the array from which elements for
                         comparison are to be considered.
        sp_idx (int)   : stop index of the array to which elements for
                         comparison are to be considered.
        key (function) : a comaprison function that compares the attributes
                         on which the objects in the list needs to be sorted.
    """
    if st_idx < sp_idx:
        p = _partition(A, st_idx, sp_idx, key)
        _quicksort(A, st_idx, p-1, key)
        _quicksort(A, p+1, sp_idx, key)

def _partition(A, st_idx, sp_idx, key):
    """Partitions the array in such a way that the elements to left of the
    randomly chosen pivot element are less than pivot value and elements to
    the right are greater than the pivot value; finally returns the index of
    the pivot element in the partitioned array.

    Args:
        A (Objects|int): array that needs to sorted in-place
        st_idx (int)   : start index of the array from which elements for
                         comparison are to be considered.
        sp_idx (int)   : stop index of the array to which elements for
                         comparison are to be considered.
        key (function) : a comaprison function that compares the attributes
                         on which the objects in the list needs to be sorted.
    """
    p_idx = randint(st_idx, sp_idx)
    pivot = A[p_idx]
    A[p_idx], A[sp_idx] = A[sp_idx], A[p_idx]
    i = st_idx
    for j in range(st_idx, sp_idx):
        if key:
            if key(A[j], pivot):
                A[i], A[j] = A[j], A[i]
                i += 1
        else:
            if A[j] <= pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
    A[i], A[sp_idx] = A[sp_idx], A[i]
    return i

"""
Implementaion of Kruskal's Algorithm for finding the minimum spanning tree
of a given Graph.
"""
def MST_Kruskal(G):
    """Returs the minimum spanning tree of a given Graph G by using the
    disjoint set data structure.

    Args:
        G (Graph): A graph instance.
    """
    T = []
    for  u in G.V(): MAKE_SET(u)
    def sort_criterion(a,b): return a.w<=b.w
    quicksort(G.E(), key=sort_criterion)
    i=0
    for e in G.E():
        if FIND_SET(e.u)!=FIND_SET(e.v):
            T.append(e)
            UNION(e.u,e.v)
        i+=1
    return T

"""
Invocation code for Assignment 2: Question 1.
"""
def Kruskal_for_range(u_dist_range, trials=15):
    """ Prints the folloing details:

    (a) The average L(n) of the weighted sum of the 15 MSTs for each n in
        [10,100,200,500,1000] for the given u_dist_range.
    (b) The average running time of Kruskal's algorithm for
        finding MSTs in the 15 graphs for each n in [10,100,200,500,1000]

    Args:
        u_dist_range ((int,int)): Uniform distrubution range for edge weights.
        trials (int)            : No of trials for each value of n.
    """
    print ("#################### Distribution: U["+
            str(u_dist_range[0])+','+
            str(u_dist_range[1]) + "] ####################")
    for n in [10,100,200,500,1000]:
        mst_trial = []
        runtime_trial = []
        for i in range(trials):
            G = Graph(n,dist_range=u_dist_range)
            start_time = timeit.default_timer()
            MST = MST_Kruskal(G)
            runtime_trial.append(timeit.default_timer() - start_time)
            MST_Sum = 0
            for e in MST:
                MST_Sum += e.w
            mst_trial.append(MST_Sum)
        print ("Expected L(" + str(n) + ") over U[" +
                str(u_dist_range[0])+ ',' +
                str(u_dist_range[1]) + "]: " +
                str(sum(mst_trial)/trials))
        print ("Avg. Running time of Kruskal for n=" + str(n) + ": " +
                str(round(sum(runtime_trial)/trials,6)) + "s")
        print("###########################" +
                "###################################")
    print "\n"

#Generates output for (a) & (b) sub-questions
Kruskal_for_range((0,1))

#Generates output for (c) sub-question
Kruskal_for_range((0,0.5))
