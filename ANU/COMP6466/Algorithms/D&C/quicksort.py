from random import randint

def quicksort(arr):
  """
  Sorts the input array using a random pivot.
  Returns []"""
  #1. select a random pivot from 0-len(arr)-1
  #2. partition the array between pivot
  #3. sort the partitions recursively.
  #4. Use insertion sort to when n<20
  if not arr: return []
  rand_idx = randint(0,len(arr)-1)
  pivot = arr[rand_idx]
  arr_new = [pivot]
  j=0
  for i in range(len(arr)):
    if arr[i]<pivot:
      arr_new.insert(0,arr[i])
      j+=1
    elif arr[i]>pivot:
      arr_new.append(arr[i])
  return quicksort(arr_new[:j])+[pivot]+quicksort(arr_new[j+1:])

if __name__ == '__main__':
  print quicksort([10,1,9,2,8,3,7,4,6,5])
