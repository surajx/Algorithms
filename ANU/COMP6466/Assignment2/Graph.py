from random import uniform,randint

class Vertex:
    pass

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

class Graph:
    def __init__(self, n_v=10, g_type="complete", weight_constraint="none",
            dist_range=(0,1), Adj=None):
        if g_type=="user":
            self.Adj = {}
            self._E = []
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
                    self._E.append(Edge(u, val_obj_map[v],
                        self._genEdgeWeight(weight_constraint, dist_range)))
                self.Adj[u_obj] = u_neighbour_list
        elif g_type=="complete":
            self._V = []
            for i in range(n_v):
                v = Vertex()
                v._value = i
                self._V.append(v)
            def getValue(self): return self._value
            Vertex.getValue = getValue
            self._genCompleteGraph(n_v, weight_constraint, dist_range)
        elif g_type=="connected":
            self.Adj={}
            self._V = []
            self._E = []
            from random import choice
            for i in range(n_v):
                v = Vertex()
                v.value = i
                self._V.append(v)
                u = choice(self._V)
                if len(self._V)==1:
                    self.Adj[v] = []
                    continue
                while u==v:
                    u = choice(self._V)
                self.Adj[v] = [u]
                self.Adj[u].append(v)
                self._E.append(Edge(v, u,
                    self._genEdgeWeight(weight_constraint, dist_range)))
            for i in range(n_v):
                u = choice(self._V)
                v = choice(self._V)
                if v in self.Adj[u]: continue
                self.Adj[u].append(v)
                self._E.append(Edge(u, v,
                    self._genEdgeWeight(weight_constraint, dist_range)))

    def _genEdgeWeight(self, weight_constraint, dist_range):
        if weight_constraint=="none":
            return round(uniform(dist_range[0],dist_range[1]), 12)
        elif weight_constraint=="natural":
            return randint(dist_range[0],dist_range[1])


    def _genCompleteGraph(self, n_v, weight_constraint, dist_range):
        #TODO: How to store Adj matrix efficiently, now storing redudndant data
        #because its a symmetric matrix.
        self.Adj = []
        self._E = []
        for i in range(n_v):
            self.Adj.append([0]*n_v)
        i,j=0,0
        for e in range(n_v*(n_v -1)/2):
            if i==j:
                j += 1
                i = 0
            e_w = self._genEdgeWeight(weight_constraint, dist_range)
            self.Adj[i][j] = e_w
            self.Adj[j][i] = e_w
            self._E.append(Edge(self._V[i], self._V[j], e_w))
            i += 1

    def __str__(self):
        if isinstance(self.Adj, dict):
            G_str = ""
            for u in self.Adj.keys():
                G_str += "["+str(u.value)+"]: "
                for v in self.Adj[u]:
                    G_str += str(v.value) + " "
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
        return self._E

if __name__ == '__main__':
    AdjList = {'v':['u','w'], 'u':['w','x'], 'w':[], 'x':[], 'a':['b'], 
            'b':['c'], 'c':[], 'i':['j'], 'j':[]}
    G = Graph(n_v=50, g_type="connected", weight_constraint="natural", dist_range=(0,10))
    print G
