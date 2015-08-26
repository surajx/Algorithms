def ChainMatrixMult(P):
  """
  Identifies the optimal paranthesization of a chain of matriced defined by P.
  Return ([],[])"""
  #Identifying the optimal substructure
    # Let the scalar multiplication cost for the prefix: A_i..j in A_n be m[i,j]
    # If there is a matrix A_k such that i<=k<j, the prefix A_i..j can be
    # written as A_i..k A_k+1..j. If paranthesizing A_i..j at k minimizes
    # its multiplication cost, then A_i..k and A_k+1..j are optimal.
    # Hence,
    # m[i,j] = min{i<=k<j(m[i,k] + m[k+1,j] + P_i-1*P_j*P_k)}  (if)  i<j
    # m[i,j] = 0  (if)  i=j
  #Overlapping Subproblems
    # If m is defined recursively without memoization then in each recursive
    # branching m[i,j] is calculated repeatedly. Suppose there is a prefix
    # A_i'..j' such that i'<i and i<j'<j. Here the range of k and k' overlaps, i.e.
    # i<=k<j and i'<=k'<j', hence both k and k' can lie between [i,j'].
    # Thus the overlapping subproblems.
  n = len(P)-1
  m = []
  s = []
  for i in range(n):
    m.append([0]*n)
    s.append([-1]*n)
  for l in range(2, n+1): # Calculate all possible paranthesization for chain of length l
    for i in range(0, n-l+1): # The start index for the last chain of length l
                              # is n-l (+1 is to include n-l as the last start index)
      j = l+i-1 # No of elements in prefix A_i..j = j-i+1 = l hence j = l+i-1
      if i>=j: continue
      m[i][j] = float("inf")
      for k in range(i,j):
        tmp = m[i][k] + m[k+1][j] + P[i]*P[j+1]*P[k+1] #Optimal substructure
        if tmp<m[i][j]:
          m[i][j] = tmp
          s[i][j] = k #k+1 to justify the change of idx start from 0 to 1
  #print ''.join([str(y)+'\n' for y in m])
  #print ''.join([str(y)+'\n' for y in s])
  return (s,m[0][n-1])

def Paranthesize(s, i, j, pstr=""):
  """
  Paranthesizes the given chain multiplication.
  Returns String"""
  # k, with is s[i,j] splits the prefix A_i..j optimally, i.e. A_i..j = <A_i..k><A_k+1..j>
  # Hence if i!=j  then the paranthesization for A_i..j would be (A_i..k)(A_k+1..j)
  # Which is (paranthesization for A_i..k)(paranthesization for A_k+1..j)
  # Hence we have a recursive paranthesization definition.
  if i==j:
    pstr = pstr + 'A' + str(i+1)
  else:
    pstr = '(' + Paranthesize(s,i,s[i][j]) + Paranthesize(s,s[i][j]+1,j) + ')'
  return pstr

if __name__ == '__main__':
  P1 = [30,35,15,5,10,20,25]
  P2 = [5,10,3,12,5,50,6]
  print Paranthesize(ChainMatrixMult(P1)[0],0,len(P1)-2)
  print Paranthesize(ChainMatrixMult(P2)[0],0,len(P2)-2)
