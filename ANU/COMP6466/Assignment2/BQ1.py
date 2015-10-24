from Graph import Graph
from Kruskal import MST_Kruskal

def most_vulnerable_edge(G):
    max_diff = 0
    max_diff_vertex = None
    for u in G.V():
        mins = [float("inf"), float("inf")]
        for v in G.getAdjOf(u):
            mins.append(G.getEdge(u,v).w)
            mins.sort()
            mins=mins[:-1]
        if abs(mins[0]-mins[1]) > max_diff:
            max_diff = abs(mins[0]-mins[1])
            max_diff_vertex = u

    min_edge = min([G.getEdge(max_diff_vertex,v) for v in
        G.getAdjOf(max_diff_vertex)], key = lambda e:e.w)
    return min_edge


if __name__=="__main__":
    AdjList = {
            'a':['b','e'],
            'b':['a','e','c'],
            'c':['b','d'],
            'd':['c','e'],
            'e':['a','b','d']
        }
    G = Graph(g_type="user",weight_constraint="natural",dist_range=(1,10),
            Adj=AdjList)
    print G
    for e in G.E():
        print e.u.value + "-----" + e.v.value + ": (" + str(e.w) + ")"
    e_vuln = most_vulnerable_edge(G)
    print ("Most Vuln edge: " + str(e_vuln.u.value) + "----" + 
            str(e_vuln.v.value) + ": " + str(e_vuln.w))
    for e in MST_Kruskal(G):
        print str(e.u.value) + "----" + str(e.v.value) + ": " + str(e.w)
    print "MST before:", sum(e.w for e in MST_Kruskal(G))
    G.removeEdge(e_vuln.u,e_vuln.v)
    del e_vuln
    print "MST after:", sum(e.w for e in MST_Kruskal(G))
    for e in MST_Kruskal(G):
        print str(e.u.value) + "----" + str(e.v.value) + ": " + str(e.w)
    print G

