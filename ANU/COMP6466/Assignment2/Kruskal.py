from Graph import Graph
from quicksort import quicksort
from DisjointSet import MAKE_SET, FIND_SET, UNION

def MST_Kruskal(G):
    T = []
    for  u in G.V(): MAKE_SET(u)
    def sort_criterion(a,b): return a.w<=b.w
    quicksort(G.E(), key=sort_criterion)
    i=0
    for e in G.E():
        if FIND_SET(e.u)!=FIND_SET(e.v):
            T.append(e)
            UNION(e.u,e.v)
        i+=1
    return T

if __name__=="__main__":
    import timeit
    def Kruskal_for_range(uniform_distribution_range, trials=15):
        print ("#################### Distribution: U["+
                str(uniform_distribution_range[0])+','+
                str(uniform_distribution_range[1]) + "] ####################")
        for n in [10,100,200,500,1000]:
            mst_trial = []
            runtime_trial = []
            for i in range(trials):
                G = Graph(n,dist_range=uniform_distribution_range)
                start_time = timeit.default_timer()
                MST = MST_Kruskal(G)
                runtime_trial.append(timeit.default_timer() - start_time)
                MST_Sum = 0
                for e in MST:
                    MST_Sum += e.w
                mst_trial.append(MST_Sum)
            print ("Expected L(" + str(n) + ") over U[" +
                    str(uniform_distribution_range[0])+ ',' +
                    str(uniform_distribution_range[1]) + "]: " +
                    str(sum(mst_trial)/trials))
            print ("Avg. Running time of Kruskal for n=" + str(n) + ": " +
                    str(round(sum(runtime_trial)/trials,6)) + "s")
            print("###########################" +
                    "###################################")
        print "\n"

    Kruskal_for_range((0,1))
    Kruskal_for_range((0,0.5))

