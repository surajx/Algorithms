import Graph

WHITE = "white"
BLACK = "black"
GRAY  = "gray"

def DFS_VISIT(G, u):
    u.color = GRAY
    u.max_sem = 0
    for v in G.getAdjOf(u):
        if v.color == WHITE:
            DFS_VISIT(G, v)
        u.max_sem = max(v.max_sem,u.max_sem)
    u.max_sem += 1
    u.color = BLACK

def TOPOLOGICAL_SORT(G):
    sorted_list = []
    for u in G.V():
        u.color = WHITE
    def DFS_VISIT_TO(G, u):
        u.color = GRAY
        for v in G.getAdjOf(u):
            if v.color == WHITE:
                DFS_VISIT_TO(G, v)
        u.color = BLACK
        sorted_list.insert(0, u)
    for u in G.V():
        if u.color == WHITE:
            DFS_VISIT_TO(G, u)
    return sorted_list

def MIN_SEM(G):
    ordered_vertex_list = TOPOLOGICAL_SORT(G)
    #resetting vertex data
    for u in G.V():
        u.color = WHITE
        u.max_sem = 0
    max_sem = 0
    for v in ordered_vertex_list:
        if v.color==WHITE:
            DFS_VISIT(G,v)
            max_sem = max(max_sem, v.max_sem)
    return max_sem


if __name__ == '__main__':
    G = Graph.Graph({'v':['u','w'],'u':['w','x'],'w':[],'x':[],'z':['y'],'y':['a','b'],
        'a':[],'b':[]})
#       ,'i':['j'],'j':['k','m'],'k':['m'],'m':[]})
#    G = Graph.Graph({'v':['u','w'],'u':['w','x'],'w':[],'x':['w']})
    print "Minimum sem:", MIN_SEM(G)
