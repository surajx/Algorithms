from Graph import Graph

#the heap based built-in priority queue implementation is bad!
# workaround with sorting.
def Dijkstra(G,s,t):
    INIT_SINGLE_SOURCE(G,s)
    S = []
    Q = list(G.V())
    Q.remove(s)
    Q.sort(key=lambda u:u.d)
    Q.insert(0,s)
    while len(Q)>0:
        u = Q.pop(0)
        S.append(u)
        for v in G.getAdjOf(u):
            w = G.getEdge(u,v).w
            if v.d > u.d + w:
                v.d = u.d + w
                Q.sort(key=lambda u:u.d)
                v.pi = u

def INIT_SINGLE_SOURCE(G,s):
    for u in G.V():
        u.d = float("inf")
        u.pi = None
    s.d = 0

if __name__ == "__main__":
    AdjList = {
            'a':['b','c'],
            'b':['h','i'],
            'c':['d'],
            'd':['e'],
            'e':['f'],
            'h':['g'],
            'i':['f'],
            'g':['f'],
            'f':[]
        }
    G = Graph(g_type="user", Adj=AdjList)
    print G
    import math
    W = [0.1,0.4,0.3,0.8,0.3,0.6,0,0.6,0.2,0.5]
    i=0
    for e in G.E():
        e.w = W[i]
        print e.u.value + "-----" + e.v.value + ": (" + str(e.w) + ")"
        if e.w!=0:
            e.w = -math.log(e.w) # converting to negative log to make summation logs
        else:
            e.w = float("inf")
        print e.u.value + "-----" + e.v.value + ": (" + str(e.w) + ")"
        i+=1
    Dijkstra(G,G.getVertex('a'),G.getVertex('f'))
    t = G.getVertex('f')
    print t.value, math.exp(-t.d)
    while t.pi:
        print t.pi.value, math.exp(-t.d)
        t = t.pi
    t = G.getVertex('f')
    def print_path(t):
        if t.pi!=None:
            print_path(t.pi)
        print t.value
    print_path(t)



