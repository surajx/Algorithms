class Vertex:
    pass

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

class Graph:
    def __init__(self, n_v=10, random=True, Adj=None):
        if not random:
            self.Adj = {}
            val_obj_map = {}
            for u in Adj.keys():
                try:
                    u_obj = val_obj_map[u]
                except:
                    u_obj = Vertex()
                    u_obj.value = u
                    val_obj_map[u] = u_obj
                u_neighbour_list = []
                for v in Adj[u]:
                    try:
                        u_neighbour_list.append(val_obj_map[v])
                    except:
                        v_obj = Vertex()
                        v_obj.value = v
                        val_obj_map[v] = v_obj
                        u_neighbour_list.append(v_obj)
                self.Adj[u_obj] = u_neighbour_list
        else:
            self._V = []
            for i in range(n_v):
                v = Vertex()
                v._value = i
                self._V.append(v)
            def getValue(self): return self._value
            Vertex.getValue = getValue
            self._genCompleteGraph(n_v)

    def _genCompleteGraph(self, n_v):
        #TODO: How to store edj matrix eddicientry now storing redudndant data
        #because its a symmetric matrix.
        from random import random
        self.Adj = []
        self._E = []
        for i in range(n_v):
            self.Adj.append([0]*n_v)
        i,j=0,0
        for e in range(n_v*(n_v -1)/2):
            if i==j:
                j += 1
                i = 0
            e_w = round(random(),10)
            self.Adj[i][j] = e_w
            self.Adj[j][i] = e_w
            self._E.append(Edge(self._V[i], self._V[j], e_w))
            i += 1

    def __str__(self):
        if isinstance(self.Adj, dict):
            G_str = ""
            for u in self.Adj.keys():
                G_str += "["+u.value+"]: "
                for v in self.Adj[u]:
                    G_str += v.value + " "
                G_str = G_str.strip() + "\n"
            return G_str.strip()
        else:
            return ''.join([str(y)+'\n' for y in self.Adj])

    def V(self):
        if isinstance(self.Adj, dict):
            return self.Adj.keys()
        else:
            return self._V

    def getAdjOf(self, u):
        if isinstance(self.Adj, dict):
            return self.Adj[u]
        else:
            Adj_V = list(self._V)
            del Adj_V[u.getValue()]
            return Adj_V

    def E(self):
        if isinstance(self.Adj, dict):
            pass
        else:
            return self._E

if __name__ == '__main__':
    G_directed = Graph(random=False, Adj={'v':['u','w'],'u':['w','x'],'w':[],'x':[],
        'a':['b'],'b':['c'],'c':[],'i':['j'],'j':[]})
    print G_directed
    G_random = Graph(5)
    print G_random.V()
    print G_random.getAdjOf(G_random.V()[0])
    from quicksort import quicksort
    def sort_condition(a,b): return a.w<=b.w
    quicksort(G_random.E(),0,len(G_random.E())-1,sort_condition)
    for e in G_random.E():
        print e.w

