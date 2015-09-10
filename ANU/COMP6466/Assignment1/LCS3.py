def LCS3(X,Y,Z):
  n, m, p = len(X), len(Y), len(Z)
  L = []
  for i in range(n+1):
    L_tmp = []
    for j in range(m+1):
      L_tmp.append([0]*(p+1))
    L.append(L_tmp)
  for i in range(n+1):
    for j in range(m+1):
      for k in range(p+1):
        if i==0 or j==0 or k==0: continue
        if X[i-1]==Y[j-1] and Y[j-1]==Z[k-1]:
          L[i][j][k] = L[i-1][j-1][k-1] + 1
        else:
          L[i][j][k] = max([L[i-1][j][k],L[i][j-1][k],L[i][j][k-1]])
  seq_LCS = backtrack(L,X,Y,Z,n,m,p)
  return seq_LCS

def backtrack(L, X, Y, Z, i, j, k):
  if i==0 or j==0 or k==0:
    return ""
  elif X[i-1]==Y[j-1] and Y[j-1]==Z[k-1]:
    return backtrack(L, X, Y, Z, i-1, j-1, k-1) + X[i-1]
  else:
    if L[i][j-1][k] > L[i-1][j][k]:
      if L[i][j-1][k] > L[i][j][k-1]:
        return backtrack(L, X, Y, Z, i, j-1, k)
      else:
        return backtrack(L, X, Y, Z, i, j, k-1)
    elif L[i][j][k-1] > L[i-1][j][k]:
      return backtrack(L, X, Y, Z, i, j, k-1)
    else:
      return backtrack(L, X, Y, Z, i-1, j, k)

if __name__ == '__main__':
  print LCS3("ABCDGHTGD","TAEDFHRT","ADHGHRRYHJT") #ADHT
