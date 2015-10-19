class Vertex:
    pass

class Edge:
    def __init__(self, u, v, w=1):
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
            self._genCompleteGraph(n_v)
            self._V = []
            for i in range(n_v):
                v = Vertex()
                v._value = i
                self._V.append(v)
            def getValue(self): return self._value
            Vertex.getValue = getValue

    def _genCompleteGraph(self, n_v):
        #TODO: How to store edj matrix eddicientry now storing redudndant data
        #because its a symmetric matrix.
        from random import uniform
        self.Adj = []
        for i in range(n_v):
            self.Adj.append([0]*n_v)
        i,j=0,0
        for e in range(n_v*(n_v -1)/2):
            if i==j:
                j += 1
                i = 0
            e_w = 0
            while e_w==0:
                e_w = uniform(0.0,1.0)
            self.Adj[i][j] = e_w
            self.Adj[j][i] = e_w
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

if __name__ == '__main__':
    G_directed = Graph(random=False, Adj={'v':['u','w'],'u':['w','x'],'w':[],'x':[],
        'a':['b'],'b':['c'],'c':[],'i':['j'],'j':[]})
    print G_directed
    G_random = Graph(5)
    print G_random.V()
    print G_random.getAdjOf(G_random.V()[0])

