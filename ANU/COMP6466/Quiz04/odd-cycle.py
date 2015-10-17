import Graph

#Graph exploration stages
WHITE = "white"
BLACK = "black"
GRAY = "gray"

#graph coloring to check if bipartite graph
YELLOW = "yellow"
BLUE = "blue"


def ODD_CYCLE_DETECTOR(G):
    BFS(G,G.V()[0])

def BFS(G, s):
    for u in G.V():
        u.color = WHITE
        u.alt_color = None
    s.color = GRAY
    s.alt_color = YELLOW
    from Queue import Queue
    Q = Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        neighbour_color = YELLOW
        if u.alt_color==YELLOW:
            neighbour_color = BLUE
        for v in G.getAdjOf(u):
            if u.alt_color != v.alt_color:
                if v.color==WHITE:
                    v.color = GRAY
                    v.alt_color = neighbour_color
                    Q.put(v)
            else:
                print "Odd Cycle Detected at:", u.value
                return True
        u.color = BLACK
    print "Did not detect Odd cycle"
    return False

if __name__ == "__main__":
    G = Graph.Graph({'v':['u','w','x'],'u':['v','x'],'w':['x','v'],'x':['u','w','v']})
    ODD_CYCLE_DETECTOR(G)

