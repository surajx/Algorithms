def min1(arr):
  min_x = arr[0]
  min_idx = 0
  for i in range(1, len(arr)):
    if min_x>arr[i]:
      min_x = arr[i]
      min_idx = i
  return (min_x, min_idx)

def max1(arr):
  max_x = arr[0]
  max_idx = 0
  for i in range(1, len(arr)):
    if max_x<arr[i]:
      max_x=arr[i]
      max_idx = i
  return (max_x, max_idx)

def minmax1(arr):
  """
  Naive algorithm tofinds the minimum and maximum value in the given array
  O(n) runs with 2n-3 comparisons
  Returns (min,max)"""
  min_x, min_idx = min1(arr)
  del arr[min_idx]
  max_x, _ = max1(arr)
  return (min_x, max_x)

def minmax2(arr):
  """
  Efficient algorithm to find the minimum and maximum in a given array.
  O(n) runs with _ comparisons.
  Return (min,max)"""
  #1. Split the array into groups of two.
  #2. Sort each pair (n/2 comparisons)
  #3. Create a list with minimum of all pairs
    # and find the minimum of that list (n/2 - 1 comparisons)
  #4. Do the same with maximum of all pairs (n/2 - 1 comparison)
  # Total 3n/2 - 2 comparison if n was even.
  # If n is odd, then execute the algorithm for n-1 elements and
    # compare the resulting min, max with the n(th) element resulting
    # an additional 2 more comparisond = 3(n-1)/2
  #Hence using this algorithm the min,max values in a given list of n elements
    # can be calculated with at most 3(floor(n))/2 comparisons.
  odd_list = False
  if len(arr)%2!=0:
    odd_list = True
    arr_last = arr[len(arr)-1]
    arr = arr[:len(arr)-1]
  groups = []
  for i in range(0,len(arr),2):
    groups.append(sorted((arr[i],arr[i+1])))
  min_list = []
  max_list = []
  for grp in groups:
    min_list.append(grp[0])
    max_list.append(grp[1])
  min_x,_ = min1(min_list)
  max_x,_ = max1(max_list)
  return (min_x, max_x)




if __name__ == '__main__':
  print minmax1([1,5,44,88,66,55,33,99,90])
  print minmax2([1,5,44,88,66,55,33,99,90])
