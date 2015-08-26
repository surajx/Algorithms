comparisons = 0

def quick_sort(elements):
  if len(elements)==1 or not elements:
    return elements
  pivot_idx = choosePivot(elements)
  elements[pivot_idx], elements[0] = elements[0], elements[pivot_idx]
  pivot_idx = 0
  (partitioned_elements, updated_pivot_idx) = partition(elements, pivot_idx)
  sorted_left_partition = quick_sort(partitioned_elements[:updated_pivot_idx])
  pivot_ele = partitioned_elements[updated_pivot_idx]
  del partitioned_elements[updated_pivot_idx]
  sorted_right_partition = quick_sort(partitioned_elements[updated_pivot_idx:])
  return sorted_left_partition + [pivot_ele] + sorted_right_partition

def choosePivot(elements):
  #return 0 #Problem 1
  #return -1 #Problem 2
  #Problem 3
  middle = (len(elements)/2 if len(elements)%2==0 else ((len(elements)+1)/2))-1
  pivot_dict = {
    elements[0]:0,
    elements[-1]:-1,
    elements[middle]:middle
  }
  pivot_ele = sorted([elements[0], elements[-1], elements[middle]])[1]
  return pivot_dict[pivot_ele]

def partition(elements, pivot_idx):
  global comparisons
  pivot_ele = elements[pivot_idx]
  del elements[pivot_idx]
  pivot_pos = 0
  for elem_idx in range(0,len(elements)):
    comparisons+=1
    if elements[elem_idx]<pivot_ele:
      elements[elem_idx], elements[pivot_pos] = elements[pivot_pos], elements[elem_idx]
      pivot_pos+=1
  #elements.insert(pivot_pos, pivot_ele)
  elements.insert(pivot_idx, pivot_ele)
  elements[pivot_idx], elements[pivot_pos] = elements[pivot_pos], elements[pivot_idx]
  return (elements, pivot_pos)

with open('QuickSort.txt','r') as file_desc:
  val_list = []
  for value in file_desc:
    val_list.append(int(value))
  print quick_sort(val_list)
  print comparisons
