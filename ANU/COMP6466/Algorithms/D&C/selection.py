from math import ceil

def ithOrder(arr, i):
  """
  Algorithm returns the i(th) smallest element in the array.
  Returns Int"""
  #1. Split the given array into groups of 5
  #2. Sort the groups internally.
  #3. Generate a list of 3rd elements in the groups of 5.
  #4. Find the median of the median elements by recursively
    # calling the ithOrder with i as (no of groups)/2
  #5. once the median is selected as the pivot, partition the array such that
    # all elements smaller than the pivot is to the left of the array and
    # all elements larger than the pivot is to the right.
  #6. Let j be the position of the pivot in the rearragend array.
  #7. If i is equal to j, the i(th) Order statistic of the array is the pivot.
  #8. If i is greater than j then recursively find the (i-j)(th) Order
    # statistic over the array to the right of the pivot.
  #9. If i is less than j then recursively fing the i(th) Order statistic
    # over the array to the left of the pivot.

  if len(arr)==1:# Base case for median selection and ith order selection.
    return arr[0]# Recusion bottoms out here.
  last_group_len = len(arr)%5# Last group which is not a full 5.
  median_list = []
  for l in  range(0, len(arr)-last_group_len, 5):
    grp = []
    for k in range(5):
      grp.append(arr[l+k])
    median_list.append(sorted(grp)[2]) #Selected the third element from a sorted group of 5.
  last_grp = sorted(arr[len(arr)-last_group_len:])
  last_grp_median = last_grp[int(ceil(len(last_grp)/2))-1] # picking the median from the last group
  median_list.append(last_grp_median)
  # Recursively find the median of medians to find the pivot.
  pivot = ithOrder(median_list, int(ceil(len(median_list)/2)))
  arr_new = [pivot]
  j=1
  for l in range(len(arr)):
    if arr[l]<pivot:
      arr_new.insert(0,arr[l]) # insert all values less than the pivot to the left of the new array.
      j+=1
    elif arr[l]>pivot:
      arr_new.append(arr[l]) # insert all values greater than the pivot to the right.
  if i==j: #step 7
    return pivot
  elif i<j: #step 9
    return ithOrder(arr_new[:j-1], i)
  else: #step 8
    return ithOrder(arr_new[j:], i-j)

if __name__ == '__main__':
  print ithOrder([847,45,43,23,76,34,56,34,213,456,87,3,2,6,34,7], 5)
