from Graph import Graph

def alt_top_sort(G):
    for v in G.V():
        v.in_degree = 0
    for u in G.V():
        for v in G.getAdjOf(u):
            v.in_degree += 1
    S = []
    for v in G.V():
        if v.in_degree==0: S.append(v)
    T = []
    while len(S)>0:
        u = S.pop(0)
        for v in G.getAdjOf(u):
            v.in_degree -= 1
            if v.in_degree == 0:
                S.append(v)
        T.append(u)
    if len(T)!=len(G.V()):
        print "Cycle detected"
        return None
    return T


if __name__ == "__main__":
    AdjList = {
            'a':['b','c','d'],
            'b':['d'],
            'c':['e'],
            'd':['e'],
            'e':[]
        }
    AdjList1 = {
            'v4':['v5'],
            'v5':['v6'],
            'v2':['v3','v4'],
            'v6':[],
            'v1':['v2','v3','v5'],
            'v3':['v5']
        }
    G = Graph(g_type="user",Adj=AdjList1)
    T = alt_top_sort(G)
    if T:   
        for v in T:
            print v.value
