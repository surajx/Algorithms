from Kruskal import MST_Kruskal_constant_weight, MST_Kruskal
from Graph import Graph
import timeit
for n in [1000,2000,3000,4000,5000]:
    G = Graph(n_v=n, g_type="connected", weight_constraint="natural",
            dist_range=(0,20))
    W = range(0,21)
    start_time = timeit.default_timer()
    MST = MST_Kruskal_constant_weight(G, W)
    finish_time = timeit.default_timer() - start_time
    MST_Sum = 0
    for e in MST:
        MST_Sum += e.w
    print ("L(" + str(n) + ") over (0,20): " +
        str(MST_Sum))
    print ("Running time of Weighted Kruskal for n=" + str(n) + ": " +
        str(round(finish_time,6)) + "s")
    print("###########################" +
        "###################################")
    print "\n"
    start_time = timeit.default_timer()
    MST = MST_Kruskal(G)
    finish_time = timeit.default_timer() - start_time
    MST_Sum = 0
    for e in MST:
        MST_Sum += e.w
    print ("L(" + str(n) + ") over (0,20): " +
        str(MST_Sum))
    print ("Running time of Kruskal for n=" + str(n) + ": " +
        str(round(finish_time,6)) + "s")
    print("###########################" +
        "###################################")
    print "\n"
