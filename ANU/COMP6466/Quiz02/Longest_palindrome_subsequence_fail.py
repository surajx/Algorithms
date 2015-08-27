# Till the end of days this algorithm should remain to remind me of how I was and how I am.

def isPalindrone(arrayIndices, inputList):
  """
  Checks if the string equivalent of the given array
  of indices is a palindrone or not
  Returns Bool"""
  cadidateString = ''.join(getStringFromIndices(arrayIndices, inputList))
  return cadidateString == cadidateString[::-1]

def getStringFromIndices(arrayIndices, inputList):
  """
  Creates a string from the list of array Indices given.
  Return String"""
  strList = []
  for i in arrayIndices:
    strList.append(inputList[i])
  return strList

def genCombinations(n, i, arr):
  """
  Returns all combinations of current element with the array.
  Return List"""
  import itertools
  combinations = []
  for r in range(1,n-i+1):
    for t in itertools.combinations(arr, r):
      combinations.append([i]+list(t))
  return combinations

def LPS(x):
  """
  Computes the longest palindrome subsequence of the given input sequence.
  return string"""
  inputList = list(x)
  inputList_idx = range(len(inputList))
  length_stage = []
  palindrom_seq = []
  for i in range(len(inputList)):
    length_stage.append(0)
    palindrom_seq.append("")
  for i in range(len(inputList)-1, -1, -1):
    combinations = []
    if i==len(inputList)-1:
      combinations = [inputList_idx[i:]]
    else:
      combinations = genCombinations(len(inputList)-1,i,inputList_idx[i+1:])
    gotPalindrome = False
    for j in combinations:
      if len(j)==1 or (len(j)>length_stage[i+1] and len(j)>length_stage[i] and isPalindrone(j, inputList)):
        length_stage[i]=len(j)
        palindrom_seq[i]=j
        gotPalindrome = True
    if not gotPalindrome:
      length_stage[i]=length_stage[i+1]
  return ''.join(getStringFromIndices(max(enumerate(palindrom_seq), key = lambda tup: len(tup[1]))[1], inputList))

if __name__ == '__main__':
  import sys
  pSubsequence = -1
  if len(sys.argv)==2:
    print "Calculating LPS for a sequence,", len(sys.argv[1]), "long."
    pSubsequence = LPS(sys.argv[1])
    print "One of the Longest palindrome subsequence is :", pSubsequence
  else:
    #Quiz example
    pSubsequence = LPS("ACGTGTCAAAATCG")
    print "(Quiz Example) One of the Longest palindrome subsequence of ACGTGTCAAAATCG:", pSubsequence
  print "Length:", len(pSubsequence)

#ACTGCATTCATGCGCTAAGTACGATAGCTAGCTAGTGATCTTGAGAAACCACACGGACTAGCTAGCTGATTAGCTGGGTAGCTAGTGATCGATACGATCAGCTACGAGCTAAGCGCGACGGAGCTAGCAGCATTTTGCGACGGGCATCCCCAAATTAATAAATCTTCCGCGAGCGCAGCATCGACGGCTACGACGGCGACGAGCGCGCGAGCAGGCAGCGACGCGACGAGCCTACACTATATCGCCATCGCAGCTACGACTCGTAGCTCGACGTATCAGCATCAGCATCCAGCTACTACAGCCGATCATCTCACTGTACATCGTCAGCTAGCTACGATCGACTGGTCGATCACTATACTGCTCTATCTATTATTACTCGAGCGACTCTCATCTGCAGCTTCCTACTGCGCTCTCTCTAGCAGGCATCTTCACAGCGCGCAGATCAGCGGATCTATTACTATCTCGCGCGCACTTCAG
