def quick_sort(elements):
  if len(elements)==1:
    return elements
  pivot_idx = choosePivot(elements)
  (partitioned_elements, updated_pivot_idx) = partition(elements, pivot_idx)
  sorted_left_partition = quick_sort(partitioned_elements[:updated_pivot_idx])
  sorted_right_partition = quick_sort(partitioned_elements[updated_pivot_idx:])
  return sorted_left_partition + sorted_right_partition

def choosePivot(elements):
  return elements[0]

def partition(elements, pivot_idx):
  pass
