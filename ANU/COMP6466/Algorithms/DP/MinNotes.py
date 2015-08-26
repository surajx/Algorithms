def MinNotes(n, D):
  """
  Dynamic programming approach to finding the minimum number of notes of a
  given set of denominations.
  Return Int"""
  #Optimal substructure.
    # M[i] = 0 if i=0
    # M[i] = min{M[i-d1] + 1, M[i-d2] + 1,...}
  M = [0]*(n+1) # Initialize DP table
  for i in range(1, n+1):
    m = float("inf")
    for d in D:
      if i-d<0: continue
      m = min(M[i-d]+1, m)
    M[i] = m
  return M[n]

if __name__ == '__main__':
  print MinNotes(13, [17,10,4,2,1])
