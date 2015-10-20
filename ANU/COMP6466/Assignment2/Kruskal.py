from Graph import Graph
from quicksort import quicksort
from DisjointSet import MAKE_SET, FIND_SET, UNION

def MST_Kruskal(G):
    T = []
    for  u in G.V(): MAKE_SET(u)
    def sort_criterion(a,b): return a.w<=b.w
    quicksort(G.E(),0,len(G.E())-1,sort_criterion)
    i=0
    for e in G.E():
        if FIND_SET(e.u)!=FIND_SET(e.v):
            T.append(e)
            UNION(e.u,e.v)
        i+=1
    return T

if __name__=="__main__":
    for n in [10,100,200,500,1000]:
        mst_trial = []
        for i in range(15):
            G = Graph(n)
            MST = MST_Kruskal(G)
            MST_Sum = 0
            for e in MST:
                MST_Sum += e.w
            mst_trial.append(MST_Sum)
        print sum(mst_trial)/15

