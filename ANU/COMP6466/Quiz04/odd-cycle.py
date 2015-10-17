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
        u.d = float("inf")
        u.pi = None
    s.color = GRAY
    s.alt_color = YELLOW
    s.d = 0
    s.pi = None
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
                    v.pi = u
                    v.d = u.d + 1
                    Q.put(v)
            else:
                print "Odd Cycle Detected at:", u.value
                return True
        u.color = BLACK
    print "Did not detect Odd cycle"
    return False

if __name__ == "__main__":
    G = Graph.Graph({'v':['u'],'u':['v','x'],'w':['x'],'x':['u','w']})
    ODD_CYCLE_DETECTOR(G)

