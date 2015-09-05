def maxProfit(K, P, l):
  R = []
  for aP in P: R.append(aP)
  for i in range(1, len(K)):
    maxRevenue = 0
    for j in range(0,i):
      if K[i]-K[j]>=l:
        maxRevenue = max(maxRevenue, R[j])
    R[i] += maxRevenue
  return max(R)

if __name__ == '__main__':
  print maxProfit([2,5,7,10,16,19,20],[34,23,45,65,23,23,78],3)
  print maxProfit([1,2,3,4,5,6,7],[1,1,1,1,1,1,1],1)
