def LIS(seq):
  """
  Given a sequence of numbers, find the longest increasing subsequence.
  Returns []"""
  #Let equence: X_0..n = 1,4,6,15,9,2,18,7,3,10
  # Optimal Substructure:
    # Length of the LIS of X_0..i is equal to the length of the LIS of X_0..i-1 + 1
    # if X[i] > X[i-1] and
    #
  n = len(seq)
  L = [1]*n
  IDX = []
  for i in range(n):
    maxL = 0
    for j in range(0,i+1):
      if seq[i] > seq[j] and L[j]>maxL:
        maxL=L[j]
    L[i] = maxL + 1
  l_LIS = max(L)
  for i in range(l_LIS,0,-1):
    IDX.append(L.index(i))
  return [seq[IDX[i]] for i in range(len(IDX)-1,-1,-1)]


if __name__ == '__main__':
  print LIS([1,4,6,15,9,2,18,7,3,10])
  print LIS([4,2,6,1,9,0,11,7,12])
  print LIS([10, 22, 9, 33, 21, 50, 41, 60])
