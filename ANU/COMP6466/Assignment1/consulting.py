def getPlan(n,M,S,P):
  SC, PC, plan  = [], [], []
  for c in S: SC.append(c)
  for c in P: PC.append(c)
  def getMinCity(Syd, Per):
    if Syd<=Per: return "S"
    else: return "P"
  plan.append(getMinCity(SC[0],PC[0])+'1')
  for i in range(1,len(S)):
    SC[i] += min(SC[i-1], M+PC[i-1])
    PC[i] += min(PC[i-1], M+SC[i-1])
    plan.append(getMinCity(SC[i], PC[i])+str((i+1)))
  return (plan, min(SC[n-1],PC[n-1]))

if __name__ == '__main__':
  print getPlan(7,2,[1,5,2,7,1,9,4],[3,6,4,1,1,1,5])
