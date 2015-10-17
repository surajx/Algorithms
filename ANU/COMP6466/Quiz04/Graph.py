class Vertex:
    pass

class Graph:
    def __init__(self, Adj):
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
    
    def __str__(self):
        G_str = ""
        for u in self.Adj.keys():
            G_str += "["+u.value+"]: " 
            for v in self.Adj[u]:
                G_str += v.value + " "
            G_str = G_str.strip() + "\n"
        return G_str.strip()

    def V(self):
        return self.Adj.keys()

    def getAdjOf(self, u):
        return self.Adj[u]

if __name__ == '__main__':
    G = Graph({'v':['u','w'],'u':['w','x'],'w':[],'x':[],'a':['b'],'b':['c'],
        'c':[],'i':['j'],'j':[]})
    print G
