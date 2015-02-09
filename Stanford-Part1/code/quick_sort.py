def quick_sort(elements):
  if len(elements)==1 or not elements:
    return elements
  pivot_idx = choosePivot(elements)
  (partitioned_elements, updated_pivot_idx) = partition(elements, pivot_idx)
  sorted_left_partition = quick_sort(partitioned_elements[:updated_pivot_idx])
  pivot_ele = partitioned_elements[updated_pivot_idx]
  del partitioned_elements[updated_pivot_idx]
  sorted_right_partition = quick_sort(partitioned_elements[updated_pivot_idx:])
  return sorted_left_partition + [pivot_ele] + sorted_right_partition

def choosePivot(elements):
  return 0

def partition(elements, pivot_idx):
  pivot_ele = elements[pivot_idx]
  del elements[pivot_idx]
  pivot_pos = 0
  for elem_idx in range(0,len(elements)):
    if elements[elem_idx]<pivot_ele:
      elements[elem_idx], elements[pivot_pos] = elements[pivot_pos], elements[elem_idx]
      pivot_pos+=1
  elements.insert(pivot_pos, pivot_ele)
  return (elements, pivot_pos)

print quick_sort([9,3,8,2,5,1,4,7,6])
