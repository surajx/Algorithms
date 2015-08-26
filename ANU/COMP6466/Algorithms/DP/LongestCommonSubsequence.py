def LCS(X,Y):
  """
  Computes the length of the Longest common subsequence in x and y
  Returns []"""
  #1. Identify the optimal substructure
    #1.1 When calculating the Longest Common Subsequence (LCS) we first assume that,
      # length of LCS of prefixes of X_n & Y_m, namely, X_i=<x1x2x3...x_i> and
      # Y_j=<y1,y2,y3....y_j> is L[i,j]. If x_i == y_j then L[i,j] = 1 + L[i-1,j-1]
      # because the last character is a part of LCS[X_i, Y_j]. Now if x_i != y_j
      # then the x_i is part of LCS[X_i, Y_j-1] or y_j is part of the LCS[X_i-1, y_j]
  n = len(X)
  m = len(Y)
  L = []
  for i in range(n+1):
    L.append([0]*(m+1))
  for i in range(n+1):
    for j in range(m+1):
      if i==0 or j==0: continue
      if X[i-1]==Y[j-1]:
        L[i][j] = 1 + L[i-1][j-1]
      else:
        L[i][j] = max(L[i-1][j], L[i][j-1])
  #print ''.join([str(y)+'\n' for y in L])
  seq_LCS = [Y[L[n].index(i)-1] for i in range(L[n][m],0,-1)]
  seq_LCS.reverse()
  seq_LCS = ''.join(seq_LCS)
  return seq_LCS

if __name__ == '__main__':
  print LCS("ABCDGH","AEDFHR")
  print LCS("AGGTAB","GXTXAYB")
  print LCS("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA","GTCGTTCGGAATGCCGTTGCTCTGTAAA") #Cormen P391

