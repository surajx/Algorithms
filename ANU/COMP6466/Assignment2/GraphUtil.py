from Queue import Queue
from random import choice

WHITE = "white"
BLACK = "black"
GRAY  = "gray"

def BFS_COUNT(G, s):
    for v in G.V():
        v.color = WHITE
    s.color = GRAY
    Q = Queue()
    Q.put(s)
    cnt = 1
    while not Q.empty():
        u = Q.get()
        for v in G.getAdjOf(u):
            if v.color == WHITE:
                v.color = GRAY
                Q.put(v)
        u.color = BLACK
        cnt +=1
    return cnt

