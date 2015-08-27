# Defining an optimal substructure.
# Suppose L[i,j] is the length of the longest palindromic subsequence of a sequence A, then:
# L[i,j] = max[ L[i+1,j], L[i,j-1] ]
# L[i,j] = L[i+1,j-1] + 2, if A[i]==A[j]
def LPS(A):
  """
  Computes the length of the longest palindromic subsequence of the input sequence
  How:
    Assume the following palindrome S with length 7 ACGTGCA
    The subsequence S[0,7] is a palindrome if S[1,6] is also a palindrome.
    i.e. S[0,7] = ACGTGCA A+S[1,6]+A
    From this inference we can conclude that, if a subsequence has the same first
    and last elements, then it's a palindrome if the inner string is a palindrome.
    Hence, to calculate the length of the longest palindrome we can confirm that
      L[i,j] = L[i+1,j-1] + 2 if S[i]==S[j] This is the idea for the optimal substructure
    Suppose we are identifying all subsequences of lenth 4, then i=0 and j=3 in (ACGT)GCA.
    In the case where S[i]!=S[j],
    the length of the longest palindromic subsequence is the
    maximum of length of two immediate inner subsequences, which are
    (1)S[i+1,j] A(CGT)GCA
    (2)S[i,j-1] (ACG)TGCA
    Which we have when we calculated longest palindrome for all subsequences of length 2.
    i.e. L[i,j] = max{L[i,j-1], L[i+1][j]}
    Formally, the optimal substructure would be:
    if S[i]==S[j]: L[i,j] = L[i+1,j-1] + 2 if S[i]==S[j]
    else         : L[i,j] = max{L[i,j-1], L[i+1][j]}
  Return Int"""
  n=len(A)
  #Initialization of table for length memoization.
  L = [[0]*n for i in range(n)]
  for i in range(n):
    L[i][i]= 1 # since a single character is a palindrome with length 1
  #Consider all subsequences with 2 or more characters.
  for l in range(2,n+1):
    for i in range(0,n-l+1):
      j=l+i-1
      #j-i<2 implies that the subsequence is 2 characters long
      if A[i]==A[j] and j-i<2:
        L[i][j] = 2
      elif A[i]==A[j]:
        L[i][j] = L[i+1][j-1] + 2
      else:
        L[i][j] = max(L[i][j-1], L[i+1][j])
  #print ''.join([str(y)+'\n' for y in L]) #Final Memoized table
  return L[0][n-1]

if __name__ == '__main__':
  import sys
  if len(sys.argv)==2:
    maxLen = LPS(sys.argv[1])
    print "Length of LPS is :", maxLen
  else:
    #Quiz example
    maxLen = LPS("ACGTGTCAAAATCG")
    print "Length of LPS in ACGTGTCAAAATCG:", maxLen
