class Queue:
  mQ = []
  def __init__(self, qData = []):
    self.mQ = qData
  def enQueue(self, v):
    self.mQ.append(v)
  def deQueue(self):
    if len(self.mQ) >= 1: return self.mQ[0]
    else: return None
  def qLen(self):
    return len(self.mQ)

class Graph:
  adjList = []
  def __init__ (self, graphData):
    self.adjList = graphData
  def bredthFirstSearch(self, startVertex):
    q = Queue([startVertex])
    while q.qLen() > 0:
      curVertex = q.deQueue()
      for v in self.adjList[curVertex]:
        q.enQueue(v)

  def depthFirstSearch(self, ):
    pass
  def minCut(self, ):
    pass
  def __str__(self):
    n = len(self.adjList)
    gStr = ""
    for v in range(0,n):
      gStr +=  str(v) + ": " + str(self.adjList[v]) + "\n"
    return gStr.rstrip()

if __name__ == '__main__':
  g = Graph([[1,2], [2,3], [4], [4,5], [5], []])
  print g
