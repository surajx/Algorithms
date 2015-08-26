def merge_sort(elements):
  if len(elements)<=1:
    return elements
  no_of_elements = len(elements)
  mid_index = no_of_elements//2
  left_half = elements[:mid_index]
  right_half = elements[mid_index:]
  sorted_left_half = merge_sort(left_half)
  sorted_right_half = merge_sort(right_half)
  return merge(sorted_left_half, sorted_right_half)

def merge(list1, list2):
  merged_list = []
  list1_idx=list2_idx=0
  while True:
    try:
      if list1[list1_idx]<list2[list2_idx]:
        merged_list.append(list1[list1_idx])
        list1_idx+=1
      else:
        merged_list.append(list2[list2_idx])
        list2_idx+=1
    except:
      if len(list1)==len(list2):
        if list1_idx>list2_idx:
          merged_list.extend(list2[list2_idx:])
        else:
          merged_list.extend(list1[list1_idx:])
      elif list1_idx>=len(list1):
        merged_list.extend(list2[list2_idx:])
      else:
        merged_list.extend(list1[list1_idx:])
      break
  return merged_list

print merge_sort([9,1,7,8,2,7,7,3,3,6,4,3,5,0,9])
