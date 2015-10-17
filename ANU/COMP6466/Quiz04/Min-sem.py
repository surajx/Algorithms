import Graph

WHITE = "white"
BLACK = "black"
GRAY  = "gray"

time = 0

def DFS_VISIT(G, u):
    global time
    time += 1
    u.d = time #Discovery time
    u.color = GRAY
    u.max_sem = 0
    for v in G.getAdjOf(u):
        if v.color == WHITE:
            v.pi = u
            DFS_VISIT(G, v)
        u.max_sem = max(v.max_sem,u.max_sem)
    u.max_sem += 1
    u.color = BLACK
    time += 1
    u.f = time #Finish time

def TOPOLOGICAL_SORT(G):
    sorted_list = []
    def DFS_TO(G):
        for u in G.V():
            u.color = WHITE
            u.pi = None
        global time
        time = 0
        def DFS_VISIT_TO(G, u):
            global time
            time += 1
            u.d = time #Discovery time
            u.color = GRAY
            u.max_sem = 0
            for v in G.getAdjOf(u):
                if v.color == WHITE:
                    v.pi = u
                    DFS_VISIT_TO(G, v)
                    u.max_sem = max(v.max_sem,u.max_sem)
            u.max_sem += 1
            u.color = BLACK
            time += 1
            u.f = time #Finish time
            sorted_list.insert(0, u)
        for u in G.V():
            if u.color == WHITE:
                DFS_VISIT_TO(G, u)

    DFS_TO(G)
    return sorted_list

if __name__ == '__main__':
#    G = Graph.Graph({'v':['u','w'],'u':['w','x'],'w':[],'x':[],'z':['y'],'y':['a','b'],
#        'a':[],'b':[],'i':['j'],'j':['k','m'],'k':['m'],'m':[]})
    G = Graph.Graph({'v':['u','w'],'u':['w','x'],'w':[],'x':['w']})
    ordered_vertex_list = TOPOLOGICAL_SORT(G)
    #resetting vertex data
    for u in G.V():
        u.color = WHITE
        u.pi = None
        u.d = 0
        u.f = 0
        u.max_sem = 0
    max_sem = 0
    for v in ordered_vertex_list:
        DFS_VISIT(G,v)
        max_sem = max(max_sem, v.max_sem)
    print "Minimum sem:", max_sem
